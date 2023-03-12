from .v2ray_api import XUIAPI
from .telegram.telegram import Telegram
from .telegram.configs import *
from .telegram.functions import *
from .telegram.admin_panel import management
from .telegram.change_server_location import *
from .validator.payment_validator import PaymentValidator
from .validator.server_validator import ServerValidator

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from hope.bot.log_api import BotLoger
from hope.payment.models import *
from hope.ray.models import *

from perfectmoney import PerfectMoney
from datetime import timedelta, datetime
from uuid import uuid4
import pytz
from .tronscan import *

User = get_user_model()
logging = BotLoger()


@api_view(('GET', 'POST'))
def webhook(request):
    print(request.data)
    print("="*100)

    data = request.data
    if 'message' in data:
        message_update(data)

    elif 'callback_query' in data:
        callback_query_update(data)
    return Response('Hello')


def message_update(update):
    telegram = Telegram()
    update = update['message']
    text = update.get('text')
    if not text:
        return
    reply_message = update.get('reply_to_message', None)
    user_id = update['from']['id']
    first_name = update['from']['first_name']
    last_name = update['from'].get('last_name', "None")
    username = update['from'].get('username', None)
    chat_id = update['chat']['id']
    message_id = update['message_id']
    user_obj = User.objects.filter(user_id=user_id)
    user = user_obj.first()
    bot = BotUpdateStatus.objects.first()

    if not user:
        user = User.objects.create_user(
            username=str(user_id) if not update["from"].get("username") else update["from"]["username"],
            password=str(user_id),
            first_name=first_name,
            last_name=last_name,
            user_id=user_id,
            step="home"
        )
        user.save()

    if bot.is_update and not user.is_staff:
        return telegram.send_Message(
            chat_id,
            text=MESSAGES["message_bot_updating"]
        )

    if reply_message:
        text_reply = reply_message['text']
        user_user_id = int(text_reply.split("name:")[0].split(":")[1])
        if "user_id" in text_reply and "name" in text_reply and "username" in text_reply:
            return telegram.copy_Message(
                user_user_id,
                chat_id,
                message_id
            )

    if text == '/start':
        user_obj.update(step="Home")
        return telegram.send_Message(
            chat_id,
            MESSAGES["start_message"],
            reply_markup=show_start_home_buttons(user_id)
        )

    if text == "/admin":
        if not user.is_superuser:
            return
        user_obj.update(step='Admin_Pannel')
        return telegram.send_Message(
            chat_id=chat_id,
            text=MESSAGES["message_admin_section"],
            reply_markup=show_admin_keyboard())

    if user.step == 'GET_TRANSACTION_ID':
        py_validator = PaymentValidator(user, UserPayments, Wallet, TronScan, text, MESSAGES)
        status, data = py_validator.main()
        if not status:
            return telegram.send_Message(
                chat_id=chat_id,
                text=data,
                reply_markup=back_to_home_button()
            )
        contract, amount = contract.first()
        exchange = Exchange()
        price = exchange.get_symbol_price(contract.symbol)
        new_balance = (price * 10) * amount
        user.user_balance.balance += new_balance
        user.user_balance.save()
        balance = f"<b>{int(user.user_balance.balance//10):,}</b>"
        return telegram.send_Message(
            chat_id,
            MESSAGES['message_success_charjid'].format(balance),
            reply_markup=back_to_home_button()
        )

    if user.step == 'GET_USER_wallet':
        if len(text) != 34:
            return telegram.send_Message(
                chat_id=chat_id,
                text=MESSAGES['message_user_wallet_invalid_error']
            )
        else:
            telegram.send_Message(
                chat_id,
                MESSAGES['message_success_add_wallet']
            )

        user.user_balance.wallet = text
        user.user_balance.save()
        user_obj.update(step='GET_TRANSACTION_ID')
        logging.addlog("add_wallet.log", f"user id: {user_id}, wallet: {text}")
        balance = f"<b>{int(user.user_balance.balance / 10):,}</b>"
        wallet = Wallet.objects.all()
        walets  = ""
        for w in wallet:
            walets += "<code>" + w.wallet + "</code>" + "\n"
        contract = ContractAddres.objects.all()
        contract_t  = "\nلیست ارز های پشتیبانی شده در شبکه ترون 👇🏻\n"
        for c in contract:
            contract_t = contract_t + "<code>" + c.symbol + "</code>" + "\n"

        return telegram.send_Message(
            chat_id,
            MESSAGES['message_get_transaction_code'].format(balance, CHANNEL_HELP) + walets + contract_t,
            reply_markup=back_to_home_button()
        )

    if user.step.startswith("Admin_Pannel"):
        management(user_obj, user, telegram, chat_id, text, message_id)

    if user.step.startswith("support_admin"):
        if not user.is_active:
            return telegram.send_Message(
                chat_id,
                MESSAGES["message_block_user"],
            )

        if text == '🔚 پایان گفتگو':
            user_obj.update(step="home")
            telegram.send_Message(chat_id, MESSAGES["message_end_support_conversation"],
                                  reply_markup=remove_replay_markup()
                                  )
            return telegram.send_Message(chat_id, MESSAGES["start_message"],
                                         reply_markup=show_start_home_buttons(
                chat_id)
            )

        selected_admin = user.step.split(":")[1]
        response = telegram.forward_Message(
            selected_admin,
            user_id,
            message_id
        )
        if response.get("error_code"):
            return telegram.send_Message(
                chat_id=chat_id,
                text=MESSAGES["message_choice_another_admin"],
                reply_markup=show_support_buttons()
            )
        msg = f"user_id: <code>{chat_id}</code>\nname: <code>{first_name}</code>\nusername: @{username}\n➖➖➖➖➖➖➖➖➖"
        telegram.send_Message(
            chat_id=selected_admin,
            text=msg,
            reply_to_message_id=response['result']['message_id'],
            reply_markup=show_block_unblock_user_buttons(chat_id)
        )
        return telegram.send_Message(
            chat_id=chat_id,
            text=MESSAGES["message_support_send_success"]
        )


def callback_query_update(update):
    telegram = Telegram()
    update = update['callback_query']
    callback_id = update['id']
    callback_message_id = update['message']['message_id']
    callback_chat_id = update['from']['id']
    callback_first_name = update['from']['first_name']
    callback_username = update['from'].get('username', "None")
    callback_data = update['data']
    callback_text = update["message"]["text"]
    user_obj = User.objects.filter(user_id=callback_chat_id)
    user = user_obj.first()
    bot = BotUpdateStatus.objects.filter(id=1)

    if bot.first().is_update and user.is_staff is False:
        return telegram.send_Message(
            callback_chat_id,
            MESSAGES["message_bot_updating"]
        )

    if callback_data == 'my_account_balance':
        if not user.user_balance.wallet:
            user_obj.update(step="GET_USER_wallet")
            return telegram.editMessageText(
                callback_chat_id,
                callback_message_id,
                MESSAGES["message_get_user_wallet"],
                reply_markup=back_to_home_button()
            )
        
        balance = f"<b>{int(user.user_balance.balance / 10):,}</b>"
        wallet = Wallet.objects.all()
        walets  = ""
        for w in wallet:
            walets = walets + "<code>" + w.wallet + "</code>" + "\n"
        contract = ContractAddres.objects.all()
        contract_t  = "\nلیست ارز های پشتیبانی شده در شبکه ترون 👇🏻\n"
        for c in contract:
            contract_t = contract_t + "<code>" + c.symbol + "</code>" + "\n"
        
        telegram.editMessageText(
            callback_chat_id,
            callback_message_id,
            MESSAGES['message_get_transaction_code'].format(balance, CHANNEL_HELP) + walets + contract_t,
            reply_markup=back_to_home_button()
        )        
        user_obj.update(step="GET_TRANSACTION_ID")

    elif callback_data == "back_to_menu":
        user_obj.update(step="home")
        return telegram.editMessageText(
            callback_chat_id,
            callback_message_id,
            MESSAGES["start_message"],
            reply_markup=show_start_home_buttons(callback_chat_id)
        )

    elif callback_data == 'support_section':
        telegram.editMessageText(
            callback_chat_id,
            callback_message_id,
            MESSAGES['message_choice_support'],
            reply_markup=show_support_buttons()
        )
        return telegram.send_AnswerCallbackQuery(callback_id,"✅")

    elif callback_data == 'test_config':
        server_v = ServerValidator(Server, MESSAGES)
        status, data = server_v.has_server()        
        if not status:
            msg = data
            r_key = back_to_home_button()
        else:
            msg = MESSAGES['message_choice_country_test']
            r_key = show_country_buttons(section="test")
            time_now = datetime.now(tz=pytz.UTC)
            weektime = time_now + timedelta(7)
            if user.user_balance.test_date:
                if user.user_balance.test_date > time_now:
                    msg = MESSAGES['message_error_test_config']
                    r_key = show_start_home_buttons(callback_chat_id)

        return telegram.editMessageText(
            callback_chat_id,
            callback_message_id,
            msg,
            reply_markup=r_key
        )

    elif callback_data == "send_to_one_msg":
        user_obj.update(step="Admin_Pannel_Send_One_Msg")
        return telegram.editMessageText(
            callback_chat_id,
            callback_message_id,
            MESSAGES["message_admin_send_to_one_msg"]
        )

    elif callback_data == "send_to_all_msg":
        user_obj.update(step="Admin_Pannel_Send_All_Msg")
        return telegram.editMessageText(
            callback_chat_id,
            callback_message_id,
            MESSAGES["message_admin_send_to_all_msg"]
        )

    elif callback_data in ['show_panels', "back_to_choice_volume"]:
        server_v = ServerValidator(Server, MESSAGES)
        status, data = server_v.has_server()
        if not status:
            msg = data
            r_key = back_to_home_button()
        else:
            msg = MESSAGES['message_choice_volume']
            r_key = show_volume_buttons()

        return telegram.editMessageText(
            callback_chat_id,
            callback_message_id,
            msg,
            reply_markup=r_key
        )

    elif callback_data in ["my_service", "back_to_choice_service"]:
        configs = ProxyConfig.objects.filter(
            user=user,
            is_use=True,
            volume__gt=150
        )
        if configs.count() == 0:
            return telegram.editMessageText(
                callback_chat_id,
                callback_message_id,
                MESSAGES['message_not_service'],
                reply_markup=show_start_home_buttons(callback_chat_id),
            )
        if configs.count() <= 5:
            next_range = 0
        else:
            next_range = 5

        return telegram.editMessageText(
            callback_chat_id,
            callback_message_id,
            MESSAGES["message_list_my_services"],
            reply_markup=show_services_button(configs[:5], callback_chat_id, 0, next_range)
        )

    elif callback_data.startswith("next_service") or callback_data.startswith("previous_service"):
        section, start_range, next_range = callback_data.split(":")
        start_range, next_range = int(start_range), int(next_range)
        configs = ProxyConfig.objects.filter(
            user=user,
            is_use=True,
            volume__gt=150
        )
        if section.startswith("next"):
            start_range = next_range
            next_range += 5
            services = configs[start_range:next_range]
            if next_range >= configs.count():
                next_range = 0
        else:
            if next_range == 0:
                next_range = start_range
            else:
                next_range -= 5
            start_range -= 5
            services = configs[start_range:next_range]

        return telegram.editMessageText(
            callback_chat_id,
            callback_message_id,
            MESSAGES["message_list_my_services"],
            reply_markup=show_services_button(services, callback_chat_id, start_range, next_range)
        )

    elif callback_data.startswith("plan_volume"):
        selected_volume = int(callback_data.split(":")[-1]) * 1024
        return telegram.editMessageText(
            callback_chat_id,
            callback_message_id,
            MESSAGES['message_choice_country'],
            reply_markup=show_country_buttons(volume=selected_volume)
        )

    elif callback_data.startswith("buy_plan"):
        selected_country, selected_volume = callback_data.split("_")[-1].split(":")
        server = get_object_or_404(Server, domain_country=selected_country, down=False)
        xray = XUIAPI(
            use=user.username,
            server=server.ip,
            username=server.username,
            password=server.password
        )
        all_configs_in_server = xray.get_count_config()
        if len(all_configs_in_server) >= 30:
            server.down = True
            server.save()
            telegram.send_AnswerCallbackQuery(
                callback_id, MESSAGES["message_server_max_config"])
            admins = User.objects.filter(is_superuser=True)
            for admin in admins:
                telegram.send_Message(
                    admin.user_id,
                    server_full_config_msg(server)
                )
            return

        plan = get_object_or_404(Plan, volume=selected_volume)
        if user.user_balance.balance < plan.price:
            return telegram.editMessageText(
                callback_chat_id,
                callback_message_id,
                MESSAGES['message_not_balance'],
                reply_markup=show_start_home_buttons(callback_chat_id))
        else:
            if server.is_tunnel:
                user.user_balance.balance -= (plan.price * 2)
            else:
                user.user_balance.balance -= plan.price
            user.user_balance.save()

        uuid = str(uuid4())
        select_config = xray.getSession(24 * 30, plan.volume, uuid)
        config = ProxyConfig(
            proxy_hash=select_config[0],
            server=server,
            volume=selected_volume,
            is_use=True,
            expire_date=datetime.now() + timedelta(days=30),
            user=user,
            uuid=uuid,
            last_num_change=0
        )
        config.save()
        telegram.editMessageText(
            callback_chat_id, callback_message_id,
            show_config_info(select_config, new_volume=plan.volume*1024*1024),
            reply_markup=show_start_home_buttons(callback_chat_id)
        )
        telegram.send_Message(
            CHANNEL_PAYED_CONFIG,
            buy_plan_message_log(
                callback_chat_id, callback_first_name,
                callback_username, datetime.now(),
                plan.price, config.server.name,
                plan.volume, select_config
            )
        )
        return logging.addlog("real_config.log", 
                              f"""user_id: {callback_chat_id}, volume: {selected_volume},
                              MB location: {server.name}:{server.ip}, uuid: {uuid}""")

    elif callback_data.startswith("test_plan"):
        selected_country, selected_volume = callback_data.split("_")[-1].split(":")
        server = get_object_or_404(Server, domain_country=selected_country, down=False)
        uuid = str(uuid4())
        xray = XUIAPI(
            user=user.username,
            server=server.ip,
            username=server.username,
            password=server.password
        )
        select_config = xray.getSession(
            expire_date=1,
            total=150,
            uuid=uuid
        )
        config = ProxyConfig(
            proxy_hash=select_config[0],
            server=server,
            volume=selected_volume,
            is_use=True,
            expire_date=datetime.now() + timedelta(hours=1),
            user=user,
            uuid=uuid,
            last_num_change=0
        )
        config.save()
        weektime = datetime.now(tz=pytz.UTC) + timedelta(7)
        user.user_balance.test_date = weektime
        user.user_balance.save()
        logging.addlog("test_config.log",
                       f"user_id: {callback_chat_id}, location: {server.name}:{server.ip}, uuid: {uuid}")
        telegram.editMessageText(
            callback_chat_id,
            callback_message_id,
            show_config_info(select_config, True)
        )
        return telegram.send_Message(
            callback_chat_id,
            MESSAGES["start_message"],
            reply_markup=show_start_home_buttons(callback_chat_id)
        )

    elif callback_data.startswith("service"):
        _, config_id = callback_data.split("_")[-1].split(":")
        config = get_object_or_404(ProxyConfig, id=config_id)
        server = config.server
        xray = XUIAPI(server.ip, server.username, server.password)
        config_info = xray.get_config_uuid(config.uuid)        
        try:
            text = calculat_volume(
                config.proxy_hash,
                config_info['down'],
                config_info['up'],
                config_info['total'],
                server.name,
                config.expire_date,
                config_info['enable'],
            )
        except Exception as error:
            logging.addlog("show_my_service.log", f"Config data not available, ProxyConfig id is: {config_id}")
            return

        return telegram.editMessageText(
            callback_chat_id,
            callback_message_id,
            text,
            reply_markup=change_config_location_buttons(config.id)
        )

    elif callback_data.startswith("change_location:"):
        data = callback_data.split(":")[1]
        self_config = get_object_or_404(ProxyConfig, id=data)
        if self_config.last_num_change > 3:
            return telegram.send_AnswerCallbackQuery(
                callback_id,
                MESSAGES["message_change_location_limit_error"]
            )

        return telegram.editMessageText(
            callback_chat_id,
            callback_message_id,
            MESSAGES['message_choice_country'],
            reply_markup=show_change_location_country(data)
        )

    elif callback_data.startswith("change_location_country"):
        config_id, country = callback_data.split("_")[-1].split(":")
        new_server = get_object_or_404(Server, domain_country=country, down=False)
        ChangeLocation(
            telegram, user,
            new_server,
            callback_chat_id, callback_message_id,
            str(uuid4()),
            config_id,
            callback_id
        ).main()

    elif callback_data.startswith("delete_service"):
        ip, config_uuid = callback_data.split("_")[-1].split(":")
        service_id = callback_text.split("ID: ")[1].split("\n")[0]
        server = Server.objects.filter(ip=ip).first()
        config = ProxyConfig.objects.filter(uuid=config_uuid)
        xui = XUIAPI(
            server=ip,
            username=server.username,
            password=server.password
        )

        response = xui.delete_config(service_id)
        if response.get("success") == True:
            if config:
                config.first().delete()
            telegram.send_AnswerCallbackQuery(
                callback_id, MESSAGES["message_admin_remove_config_success"],
                cache_time=4
            )
            telegram.editMessageText(
                callback_chat_id,
                callback_message_id,
                callback_text,
                entities=json.dumps(
                    [{'offset': 0, 'length': len(callback_text), 'type': 'strikethrough'}])
            )
            return telegram.send_Message(
                chat_id=callback_chat_id,
                text=MESSAGES["message_admin_section"],
                reply_markup=show_admin_keyboard())
        else:
            telegram.send_AnswerCallbackQuery(
                callback_id, MESSAGES["message_admin_remove_config_err"],
                cache_time=3)

    elif callback_data.startswith("support_admin_id"):
        admin_id = callback_data.split(":")[1]
        user_obj.update(step=f"support_admin:{admin_id}")
        return telegram.send_Message(
            callback_chat_id,
            MESSAGES['message_support_section'],
            reply_markup=bot_end_button_suport()
        )

    elif callback_data.startswith("block_user"):
        __, user_id, status = callback_data.split(":")
        user = get_object_or_404(User, user_id=user_id)
        if status == "block":
            user.update(is_active=False)
        else:
            user.update(is_active=True)
        return telegram.send_AnswerCallbackQuery(
            callback_id,
            MESSAGES["message_admin_user_access"].format(status)
        )

    elif callback_data.endswith("update_bot"):
        status = callback_data.split("_")[0]
        if status == "enable":
            bot.update(is_update=False)
        else:
            bot.update(is_update=True)
        return telegram.send_AnswerCallbackQuery(
            callback_id,
            text=MESSAGES[f"message_admin_{status}_bot_update"]
        )

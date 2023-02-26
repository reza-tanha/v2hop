from .v2ray_api import XUIAPI

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

from hope.bot.log_api import BotLoger
from hope.bot.telegram.telegram import Telegram
from hope.bot.telegram.configs import *
from hope.bot.telegram.functions import *
from hope.bot.telegram.admin_panel import management
from hope.payment.models import *
from hope.ray.models import *

from perfectmoney import PerfectMoney
from datetime import timedelta, datetime
from unidecode import unidecode
from uuid import uuid4
import pytz


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
    text = update['text']
    user_id = update['from']['id']
    first_name = update['from']['first_name']
    last_name = update['from'].get('last_name', "None")
    username = update['from'].get('username', None)
    chat_id = update['chat']['id']
    message_id = update['message_id']
    user_obj = User.objects.filter(user_id=user_id)
    user = user_obj.first()

    if text == '/start':
        user_obj.update(step="Home")
        if not user:
            user = User.objects.create_user(
                username=str(user_id),
                password=str(user_id),
                first_name=first_name,
                last_name=last_name,
                user_id=user_id,
                step="home"
            )
            user.save()        
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

    if user.step == 'GET_VOUCHER_CODE':
        perfect = PerfectMonyPayment.objects.get(
            user=user,
            is_tmp=True
        )
        try:
            text = unidecode(text)
        except:
            pass
        if len(text) != 10:
            telegram.send_Message(
                chat_id,
                MESSAGES['voucher_code_len_invalid']
            )
            return
        perfect.voucher_code = text
        perfect.save()
        user_obj.update(step='GET_VOUCHER_ACTIVE')
        telegram.send_Message(
            chat_id,
            MESSAGES['voucher_active'],
            reply_markup=back_to_home_button()
        )
        return

    if user.step == 'GET_VOUCHER_ACTIVE':
        perfect = PerfectMonyPayment.objects.get(
            user=user,
            is_tmp=True
        )
        try:
            text = unidecode(text)
        except:
            pass
        if len(text) != 16:
            return telegram.send_Message(
                chat_id,
                MESSAGES['voucher_active_len_invalid'],

            )            
        perfect.voucher_active = text
        perfect.save()
        p = PerfectMoney(PERFECTMONEY_USER, PERFECTMONEY_PASSWORD,
                         proxies=PERFECTMONEY_PROXY)
        pay_perfect = p.voucher_activation(
            PERFECTMONEY_USD,
            perfect.voucher_code,
            perfect.voucher_active
        )
        if not pay_perfect:
            telegram.send_Message(
                chat_id,
                MESSAGES['message_error_voucher_active'],
                reply_markup=show_start_home_buttons(chat_id)
            )
            user_obj.update(step='Home')
            return

        logging.addlog("hope/logs/pays.log",
                       f"user id : {user_id}, perfect info {perfect.voucher_code}:{perfect.voucher_active}, {pay_perfect}")

        price_pay = float(pay_perfect.get("VOUCHER_AMOUNT"))
        usdtorial = PriceSettings.objects.all().first()
        user.user_balance.balance += int(price_pay * usdtorial.price)
        user.user_balance.save()
        user_obj.update(step="Home")
        telegram.send_Message(chat_id,
                              MESSAGES['message_success_payement'],
                              reply_markup=show_start_home_buttons(chat_id)
                              )
        perfect.status = True
        perfect.is_tmp = False
        perfect.save()
        return telegram.send_Message(
            CHANNEL_PAYED,
            buy_plan_config_message_log(
                chat_id,
                first_name,
                username,
                datetime.now(),
                int(price_pay * usdtorial.price),
                price_pay,
                perfect.voucher_code,
                perfect.voucher_active),
            parse_mode="html"
        )

    if user.step.startswith("Admin_Pannel"):
        management(user_obj, user, telegram, chat_id, text)


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
    if callback_data == 'my_account_balance':
        telegram.editMessageText(
            callback_chat_id,
            callback_message_id,
            MESSAGES['voucher_code'],
            reply_markup=back_to_home_button()
        )
        user_obj.update(step="GET_VOUCHER_CODE")
        tmp_perfect = PerfectMonyPayment.objects.filter(user=user, is_tmp=True)
        tmp_perfect.delete()
        perfect = PerfectMonyPayment(user=user, is_tmp=True)
        perfect.save()

    elif callback_data == 'back_to_menu':
        telegram.editMessageText(
            callback_chat_id,
            callback_message_id,
            MESSAGES["start_message"],
            reply_markup=show_start_home_buttons(callback_chat_id)
        )

    elif callback_data == 'show_panels':
        telegram.editMessageText(
            callback_chat_id,
            callback_message_id,
            MESSAGES['message_get_volume'],
            reply_markup=show_volume_buttons()
        )

    elif callback_data.startswith("plan_volume"):
        selected_volume = int(callback_data.split(":")[-1]) * 1024
        volume_user = int(callback_data.split(":")[-1]) * 1024
        return telegram.editMessageText(
            callback_chat_id,
            callback_message_id,
            MESSAGES['message_get_country'],
            reply_markup=show_country_buttons(volume=selected_volume)
        )

    elif callback_data.startswith("plan_country"):
        uuid = str(uuid4())
        selected_countr, selected_volume, section = callback_data.split("_")[-1].split(":")
        server = Server.objects.filter(
            domain_country=selected_countr, down=False).first()
        xray = XUIAPI(
            server=server.ip,
            username=server.username,
            password=server.password
        )
        
        all_configs_in_server = xray.get_count_config()
        if len(all_configs_in_server) >= 50:
            server.down=True
            server.save()
            telegram.send_AnswerCallbackQuery(
                callback_id, MESSAGES["message_server_max_config"]
            )
            admins = User.objects.filter(is_superuser=True)
            for adm in admins:
                return telegram.send_Message(
                    adm.user_id,
                    message_admin_server_full_count(server),
                    parse_mode="html"
                )
            return      

        if section == "test":
            time_now = datetime.now(tz=pytz.UTC)
            weektime = time_now + timedelta(7)
            user.user_balance.test_date = weektime
            select_config = xray.getSession(
                expire_date=1, 
                total=150,
                uuid=uuid
            )
            config = ConfigVpn(
                conf=select_config[0],
                server=server,
                volume=selected_volume,
                is_use=True,
                expire_date=datetime.now() + timedelta(hours=1),
                user=user,
                uuid=uuid,
                last_num_change=0
            )
            config.save()
            user.user_balance.save()
            logging.addlog("hope/logs/test_config.log",
                           f"user_id: {callback_chat_id}, location: {server.name}:{server.ip}, uuid: {uuid}")
            return telegram.editMessageText(
                callback_chat_id,
                callback_message_id,
                show_config_info(select_config),
                reply_markup=show_start_home_buttons(callback_chat_id),
                parse_mode="html"
            )

        price = Subscribe.objects.filter(volume=selected_volume).first()
        if user.user_balance.balance < price.price:
            return telegram.editMessageText(
                callback_chat_id,
                callback_message_id,
                MESSAGES['message_not_balance'],
                reply_markup=show_start_home_buttons(callback_chat_id))
        else:
            user.user_balance.balance -= price.price
            user.user_balance.save()

        select_config = xray.getSession(24 * 30, price.volume, uuid)
        config = ConfigVpn(
            conf=select_config[0],
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
            callback_chat_id,
            callback_message_id,
            show_config_info(select_config),
            reply_markup=show_start_home_buttons(callback_chat_id),
            parse_mode="html"
        )
        telegram.send_Message(
            CHANNEL_PAYED_CONFIG,
            buy_plan_message_log(
                callback_chat_id,
                callback_first_name,
                callback_username,
                datetime.now(),
                price.price,
                config.server.name,
                price.volume,
                select_config),
            parse_mode="html"
        )
        return logging.addlog("hope/logs/real_config.log",
                              f"user_id: {callback_chat_id}, volume: {selected_volume}, MB location: {server.name}:{server.ip}, uuid: {uuid}")

    elif callback_data == 'my_service':
        configs = ConfigVpn.objects.filter(
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

        if configs.count() < 5:
            return telegram.editMessageText(
                callback_chat_id,
                callback_message_id,
                "سرویس های شما",
                reply_markup=ServicesButton(configs, callback_chat_id)
            )

        conf_ = []
        counter = 1
        for conf in configs:
            if counter <= 5:
                conf_.append(conf)
                continue
            else:
                telegram.send_Message(
                    callback_chat_id,
                    "سرویس های شما",
                    reply_markup=ServicesButton(conf_, callback_chat_id)
                )
                counter = 1
                conf_ = []

        telegram.send_Message(
            callback_chat_id,
            "سرویس های شما",
            reply_markup=ServicesButton(conf_, callback_chat_id)
        )
        counter = 1
        conf_ = []
        return

    elif callback_data.startswith("service"):
        _, config_id = callback_data.split("_")[-1].split(":")
        config = ConfigVpn.objects.get(id=config_id)
        server = config.server
        xray = XUIAPI(server.ip, server.username, server.password)
        config_info = xray.get_config_uuid(config.uuid)
        text = calculat_volume(
            config.conf,
            config_info['down'],
            config_info['up'],
            config_info['total'],
            server.name,
            config.expire_date,
            config_info['enable'],
        )

        return telegram.editMessageText(
            callback_chat_id,
            callback_message_id,
            text,
            reply_markup=change_config_location_buttons(config.id),
            parse_mode="html"
        )

    elif callback_data == 'test_config':
        time_now = datetime.now(tz=pytz.UTC)
        weektime = time_now + timedelta(7)
        if user.user_balance.test_date:
            if user.user_balance.test_date > time_now:
                return telegram.editMessageText(
                    callback_chat_id,
                    callback_message_id,
                    MESSAGES['message_error_test_config'],
                    reply_markup=show_start_home_buttons(callback_chat_id)
                )
        return telegram.editMessageText(
            callback_chat_id,
            callback_message_id,
            MESSAGES['message_get_country'],
            reply_markup=show_country_buttons(section="test")
        )

    elif callback_data.startswith("change_location:"):
        data = callback_data.split(":")[1]
        self_config = ConfigVpn.objects.get(id=data)
        if self_config.last_num_change > 3:
            return telegram.send_AnswerCallbackQuery(
                callback_id,
                "⛔️ شما فقط 3 بار قادر به عوض کردن کانفیگ خود هستید ⛔️"
            )
            
            
        return telegram.editMessageText(
            callback_chat_id,
            callback_message_id,
            MESSAGES['message_get_country'],
            reply_markup=show_change_location_country(data)
        )

    elif callback_data.startswith("change_location_country"):
        config_id, country = callback_data.split("_")[-1].split(":")
        uuid = str(uuid4())
        new_server = Server.objects.filter(
            down=False, domain_country=country).first()
        config = ConfigVpn.objects.filter(id=config_id).first()
        last_server = config.server
        xray = XUIAPI(
            server=last_server.ip,
            username=last_server.username,
            password=last_server.password
        )
        current_config = xray.get_config_uuid(config.uuid)
        new_volume = current_config['total'] - (current_config['down'] + current_config['up'])
        new_volume = int(new_volume / 1024 / 1024)

        if config.expire_date <= datetime.now().date():
            return telegram.send_AnswerCallbackQuery(
                callback_id, MESSAGES["message_config_expire_error"]
            )

        if new_volume <= 500:  # if volume < 500 mb
            return telegram.send_AnswerCallbackQuery(
                callback_id,
                "حجم شما کمتر از 500 مگابایت است و قابلت تغیر لوکیشن ندارید"
            )

        try:
            xray.delete_config(current_config['id'])
            xray = XUIAPI(
                server=new_server.ip,
                username=new_server.username,
                password=new_server.password
            )
            select_config = xray.getSession(
                current_config['expiryTime'], new_volume, uuid, True)
        except:
            return
        num_change_location = config.last_num_change+1
        new_config = ConfigVpn(
            conf=select_config[0],
            server=new_server,
            volume=new_volume,
            is_use=True,
            expire_date=config.expire_date,
            user=user,
            uuid=uuid,
            last_num_change=num_change_location
        )
        new_config.save()
        config.delete()
        return telegram.editMessageText(
            callback_chat_id,
            callback_message_id,
            show_config_info(select_config),
            reply_markup=show_start_home_buttons(callback_chat_id),
            parse_mode="html"
        )

    elif callback_data.startswith("delete_service"):
        ip, config_uuid = callback_data.split("_")[-1].split(":")
        service_id = callback_text.split("ID: ")[1].split("\n")[0]
        server = Server.objects.filter(ip=ip).first()
        config = ConfigVpn.objects.filter(uuid=config_uuid)
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
                entities=json.dumps([ {'offset': 0, 'length': len(callback_text), 'type': 'strikethrough'}])
            )
            return telegram.send_Message(
                chat_id=callback_chat_id,
                text=MESSAGES["message_admin_section"],
                reply_markup=show_admin_keyboard())
        else:
            telegram.send_AnswerCallbackQuery(
                callback_id, MESSAGES["message_admin_remove_config_err"],
                cache_time=3)

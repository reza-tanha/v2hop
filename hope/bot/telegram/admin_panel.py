from django.db.models import Q
from hope.bot.v2ray_api import XUIAPI
from .functions import *


def management(user_obj: "User", user: dict, telegram: "Telegram", chat_id: int, text: str):
    keys = show_admin_keyboard(True)
    keys.update(show_admin_back_keyboard(True))
    msg = ""

    # Send
    if text == keys.get("config_info"):
        user_obj.update(step="Admin_Pannel_Config_Info")
        msg = MESSAGES["message_admin_get_config_info"]

    elif text == keys.get("user_info"):
        user_obj.update(step="Admin_Pannel_User_Info")
        msg = MESSAGES["message_admin_get_user_info"]

    elif text == keys.get("del_user_service"):
        user_obj.update(step="Admin_Pannel_Delete_Service")
        msg = MESSAGES["message_admin_del_user_service"]

    elif text == keys.get("totall_users"):
        total_users = User.objects.count()
        total_in_use_conf = ConfigVpn.objects.filter(is_use=True).count()
        total_services = Server.objects.count()
        return telegram.send_Message(
            chat_id=chat_id,
            text=MESSAGES["message_admin_get_total_users"].format(
                total_users,
                total_in_use_conf,
                total_services),
            parse_mode='html')

    elif text == keys.get("incr_wallet"):
        user_obj.update(step="Admin_Pannel_Incr_Wallet")
        msg = MESSAGES["message_admin_increase_walet"]

    elif text == keys.get("decr_wallet"):
        user_obj.update(step="Admin_Pannel_Decr_Wallet")
        msg = MESSAGES["message_admin_decrease_walet"]

    elif text == keys.get("back"):
        user_obj.update(step="Admin_Pannel")
        return telegram.send_Message(
            chat_id=chat_id,
            text=MESSAGES["message_admin_section"],
            reply_markup=show_admin_keyboard())

    if text in keys.values():
        return telegram.send_Message(
            chat_id=chat_id,
            text=msg,
            reply_markup=show_admin_back_keyboard(),
            parse_mode='html')

    # Receive
    if user.step.endswith("Config_Info"):
        vmess = text.strip()
        conf = ConfigVpn.objects.filter(Q(conf=vmess) | Q(uuid=vmess)).first()
        if conf:
            config_info = XUIAPI(
                server=conf.server.ip,
                username=conf.server.username,
                password=conf.server.password).get_config_uuid(conf.uuid)
            text = get_amount_used_msg(
                config_info=config_info, config_obj=conf)
        else:
            text = MESSAGES["message_admin_config_not_found_err"]

        return telegram.send_Message(
            chat_id=chat_id,
            text=text,
            parse_mode="html")

    elif user.step.endswith("User_Info"):
        try:
            user = User.objects.filter(user_id=text).first()
            if user:
                balance = user.user_balance
                text = get_user_info_msg(user, balance)
            else:
                text = MESSAGES["message_admin_user_not_found_err"]
        except Exception:
            text = MESSAGES["message_admin_user_not_found_err"]

        return telegram.send_Message(
            chat_id=chat_id,
            text=text,
            parse_mode="html")

    elif user.step.endswith("Delete_Service"):
        user_text = text.strip()
        config = ConfigVpn.objects.filter(
            Q(uuid=user_text) | Q(conf=user_text)).first()
        if config:
            server_ip = config.server.ip
            info = XUIAPI(
                server=server_ip,
                username=config.server.username,
                password=config.server.password
            ).get_one_inbounds_config(config.uuid)
            if info:
                msg = MESSAGES["message_admin_show_config_info"].format(
                    info["id"], server_ip,
                    info["port"], info["protocol"],
                    info["remark"], info["uuid"]
                )
                data = f"{server_ip}:{info['uuid']}"
                return telegram.send_Message(
                    chat_id=chat_id,
                    text=msg,
                    reply_markup=show_admin_del_service_keyboard(data),
                    parse_mode='html'
                )
        return telegram.send_Message(
            chat_id=chat_id,
            text=MESSAGES["message_admin_remove_config_err"],
            reply_markup=show_admin_back_keyboard(),
            parse_mode='html')

    elif user.step.endswith("Wallet"):
        try:
            user_id, mony = text.split(":")
            user = User.objects.filter(user_id=user_id).first()
            if user:
                if user.step.endswith("Incr_Wallet"):
                    user.user_balance.balance += int(mony)
                else:
                    user.user_balance.balance -= int(mony)
                user.user_balance.save()
                text = MESSAGES["message_admin_balance_update"].format(
                    user_id, user.user_balance.balance)
            else:
                text = MESSAGES["message_admin_user_not_found_err"]
        except Exception:
            text = MESSAGES["message_admin_user_not_found_err"]

        return telegram.send_Message(
            chat_id=chat_id,
            text=text,
            parse_mode="html")

from .configs import *
from django.contrib.auth import get_user_model
from hope.account.models import Balance
from hope.ray.models import *
import math
import json
from datetime import datetime

User = get_user_model()

def format_bytes(size):
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'KB', 2: 'MB', 3: 'GB'}
    while size > power:
        size /= power
        n += 1
    return f"{power_labels[n]} {round(size)}"


def show_start_home_buttons(user_id=0):
    user_balance = Balance.objects.get(user__user_id=user_id)
    balance = f"{int(user_balance.balance / 10):,}"
    markup = {
        'inline_keyboard': [
            [
                {'text': '🔷 تست vpn', 'callback_data': 'test_config'},
                {'text': '💰خرید vpn', 'callback_data': 'show_panels'}
            ],
            [
                {'text': f'موجودی : {balance} تومان 💰','callback_data': 'my_account_balance'},
                {'text': f'🛒 سرویس های من', 'callback_data': 'my_service'},

            ],
            [
                {'text': f'📢 کانال راهنما و اطلاع رسانی ',
                 'url': f'https://t.me/{CHANNEL_HELP}'}
            ],
            [
                {'text': f'☎️ ارتباط با پشتیبانی', 'callback_data': f'supported_admin'},
            ],
        ]
    }

    return json.dumps(markup)


def back_to_home_button():
    markup = {
        'inline_keyboard': [
            [
                {'text': '🔙 بازگشت به منو 🔙', 'callback_data': f'back_to_menu'},
            ]
        ]
    }

    return json.dumps(markup)

def bot_update_buttom():
    markup = {
        'inline_keyboard': [
            [
                {'text': 'enable ✅', 'callback_data': f'bot_update_1'},
                {'text': 'update 🔄', 'callback_data': f'bot_update_0'}
            ]
        ]
    }

    return json.dumps(markup)

def bot_ssapport_buttom():
    markup = {
        'inline_keyboard': [
            [
                {'text': '📞 پشتیبان 1', 'callback_data': f'admin_suport:1'},
                {'text': '📞 پشتیبان 2', 'callback_data': f'admin_suport:2'}
            ],
            [
                {'text': '🔙', 'callback_data': 'back_to_menu'},
            ]
        ]
    }
    return json.dumps(markup)

def bot_bluck_unblack_buttom(user_id):
    markup = {
        'inline_keyboard': [
            [
                {'text': 'block ❌', 'callback_data': f'block_user:{user_id}:1'},
                {'text': 'unblock ✅', 'callback_data': f'block_user:{user_id}:0'}
            ]
        ]
    }
    return json.dumps(markup)

def remove_replay_markup():
    markup = {
        'remove_keyboard': True
    }
    return json.dumps(markup)

def bot_end_button_suport():
    markup = {
        'keyboard': [
            ["🔚 پایان گفتگو"]
        ],
        'resize_keyboard': True
    }

    return json.dumps(markup)


def show_volume_buttons():
    """Show volume buttons"""
    subscribe = Subscribe.objects.all()

    inline = [
        [
            {'text': f'⚡️ {int(plan.volume / 1024)} گیگ ماهانه | {int(plan.price / 10):,} تومان',
             'callback_data': f'plan_volume:{int(plan.volume / 1024)}'},
        ]
        for plan in subscribe
    ]
    inline.append(
        [
            {'text': '🔙 بازگشت به منو 🔙', 'callback_data': 'back_to_menu'},
        ]
    )
    markup = {
        'inline_keyboard': inline
    }

    return json.dumps(markup)


def show_country_buttons(volume: str = 0, section="buy"):
    """Show country buttons"""
    countries = Server.objects.filter(down=False)
    if countries:
        inline = [
            [
                {'text': country.name,
                 'callback_data': f"plan_country_{country.domain_country}:{volume}:{section}"}
            ]
            for country in countries
        ]
        inline.append(
            [
                {'text': '🔙 بازگشت به منو 🔙', 'callback_data': 'back_to_menu'},
            ]
        )
        markup = {
            'inline_keyboard': inline
        }

        return json.dumps(markup)


def ServicesButton(configs: list, user_id):
    inline = [
        [
            {'text': f'{conf.server.name}:{conf.id}',
             'callback_data': f'service_{user_id}:{conf.id}'},
        ]
        for conf in configs
    ]
    inline.append([
        {'text': '🔙 بازگشت به منو 🔙', 'callback_data': 'back_to_menu'},
    ]
    )
    markup = {
        'inline_keyboard': inline  # [
    }

    return json.dumps(markup)


def show_config_info(config):
    volume = format_bytes(config[2])
    proxy = config[0]
    text = f"""
        \n🎗  کانفیگ شما :\
        \n\n<code>{proxy}</code>\
        \n\n🎗حجم : {volume}
        \n❗️برای دستگاه های ios فقط از برنامه NapsternetV استفاده کنید.\
        \n\n🆔 @{BOT_USERNAME}
    """
    return text


def buy_plan_config_message_log(user_id, name, username, time_now, price, location, volume, conf):
    """Generate a purchase text message to the management channel,like logs"""
    text = f"""
        \n<b>User :</b> {user_id}\
        \n<b>name :</b> {name}\
        \n<b>username :</b> @{username}\
        \n<b>time :</b> <code>{time_now}</code>\
        \n<b>price :</b> {int(price / 10):,} تومان\
        \n<b>location :</b>  {location}\
        \n<b>volume :</b>  {int(volume / 1024)} GB\
        \n<b>config :</b> <code>{conf}</code>
        """
    return text


def buy_plan_message_log(user_id, name, username, time_now, price, price_d, perfect_code, perfect_active):

    text = f"""
    \n<b>User:</b> {user_id}\
    \n<b>name:</b> {name}\
    \n<b>username:</b> @{username}\
    \n<b>time:</b> <code>{time_now}</code>\
    \n<b>price:</b> {int(price / 10):,} تومان\
    \n<b>price:$</b> {price_d} دلار\
    \n<b>perfect code:</b>  <code>{perfect_code}</code>\
    \n<b>perfect active:</b> <code>{perfect_active}</code>
    """
    return text


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def calculat_volume(conf, down, up, total, location, expire_date, status: bool = False, ):
    status = "فعال 🟢" if status else "غیرفعال 🔴"
    text = f"""<code>{conf}</code>\
        \nا---------------------------------------------------------------------\
        \n<b>🎗 مقدار دانلود : </b>{convert_size(down)}\
        \nا--------------------------------------------------\
        \n<b>🎗 مقدار اپلود : </b>{convert_size(up)}\
        \nا--------------------------------------------------\
        \n<b>🎗حجم کلی : </b>{convert_size(total)}\
        \nا--------------------------------------------------\
        \n<b>🎗 لوکیشن : </b>{location}\
        \nا--------------------------------------------------\
        \n<b>🎗 تاریخ انقضا : </b>{expire_date}\
        \nا--------------------------------------------------\
        \n<b>🎗 وضعیت : </b>{status}\
        \n.
    """
    return text


def message_admin_server_full_count(server, count=50):
    text = f"""
🖥 server : <code>{server.name}</code>
💻 ip : <code>{server.ip}</code>
👤 server user count : <code>{count}</code>
❌ please add new server <code>{server.name}</code>

"""
    return text

def change_config_location_buttons(id):
    markup = {
        'inline_keyboard': [
            [
                {'text': 'تغیر لوکیشن 🔄', 'callback_data': f'change_location:{id}'},
            ],
            [
                {'text': '🔙 بازگشت به منو 🔙', 'callback_data': f'back_to_menu'},
            ]
        ]
    }

    return json.dumps(markup)


def show_change_location_country(id):
    countries = Server.objects.filter(down=False)
    if countries:
        inline = [
            [
                {'text': country.name,
                    'callback_data': f"change_location_country_{id}:{country.domain_country}"}
            ]
            for country in countries
        ]
        inline.append([
            {'text': '🔙 بازگشت به منو 🔙', 'callback_data': 'back_to_menu'},
        ]
        )
        markup = {
            'inline_keyboard': inline
        }

        return json.dumps(markup)


# Admin Section
def show_admin_keyboard(get_keys: bool = False):
    """Show the keyboards of the admin section"""
    key_row_1 = ["📈 Get Config Info", "📉Get User Info"]
    key_row_2 = ["🗑 Del User Service", "🪬 General Info"]
    key_row_3 = ["⬆️ Increase Wallet", "🔽 Decrease Wallet"]
    key_row_4 = ["🔄 Update"]

    markup = {
        'keyboard': [key_row_1, key_row_2, key_row_3, key_row_4],
        'resize_keyboard': True
    }

    if get_keys:
        keys = ["config_info", "user_info", "del_user_service",
                "totall_users", "incr_wallet", "decr_wallet", "bot_update"]
        values = key_row_1 + key_row_2 + key_row_3 + key_row_4
        return dict(zip(keys, values))
    print(markup)
    return json.dumps(markup)


def show_admin_back_keyboard(get_keys: bool = False):
    """Show the back keyboards in admin section"""
    row_key_1 = ["🏛 Back"]
    markup = {
        'keyboard': [row_key_1],
        'resize_keyboard': True
    }

    if get_keys:
        return {"back": row_key_1[0]}

    return json.dumps(markup)


def get_amount_used_msg(config_info, config_obj):
    """Generage config information message for admin section"""
    down, up, total = config_info['down'], config_info['up'], config_info['total']
    status = "Enable 🟢" if config_info['enable'] else "Disable 🔴"

    text = f"""<b>⚡️Config Information:⚡️</b>\
        \n➖➖➖➖➖➖➖➖➖➖➖➖➖\
        \n\n<b>🎗 Download: </b><code>{convert_size(down)}</code>\
        \n➖➖➖➖➖➖➖➖➖➖➖➖➖\
        \n<b>🎗 Upload: </b><code>{convert_size(up)}</code>\
        \n➖➖➖➖➖➖➖➖➖➖➖➖➖\
        \n<b>🎗 Volume: </b><code>{convert_size(total)}</code>\
        \n➖➖➖➖➖➖➖➖➖➖➖➖➖\
        \n<b>🎗 Location: </b><code>{config_obj.server.name}</code>\
        \n➖➖➖➖➖➖➖➖➖➖➖➖➖\
        \n<b>🎗 Expire Time: </b><code>{config_obj.expire_date}</code>\
        \n➖➖➖➖➖➖➖➖➖➖➖➖➖\
        \n<b>🎗 Status: </b><code>{status}</code>\
        \n.
    """
    return text


def show_admin_del_service_keyboard(data):
    """Generate remove service button"""
    markup = {
        "inline_keyboard": [
            [
                {"text": "🗑 Delete Service",
                    "callback_data": f"delete_service_{data}"},
            ]
        ]
    }
    return json.dumps(markup)


def get_user_info_msg(user, balance):
    """Generage user information message for admin section"""
    total_active = user.user_configvpn.filter(expire_date__gte=datetime.now().date()).count()
    total_deactive = user.user_configvpn.filter(expire_date__lte=datetime.now().date()).count()
    balance = f"{int(balance.balance / 10):,}"

    text = f"""<b>⚡️User Information:⚡️</b>\
        \n➖➖➖➖➖➖➖➖➖➖➖➖➖\
        \n\n<b>👤 userID: </b><code>{user.username}</code>\
        \n➖➖➖➖➖➖➖➖➖➖➖➖➖\
        \n\n<b>👤 Name: </b><code>{user.first_name}</code>\
        \n➖➖➖➖➖➖➖➖➖➖➖➖➖\
        \n\n<b>📍 Step: </b><code>{user.step}</code>\
        \n➖➖➖➖➖➖➖➖➖➖➖➖➖\
        \n\n<b>📅  Joined Date: </b><code>{user.date_joined.date()}</code>\
        \n➖➖➖➖➖➖➖➖➖➖➖➖➖\
        \n\n<b>💰 Balance: </b><code>{balance}</code>\
        \n➖➖➖➖➖➖➖➖➖➖➖➖➖\
        \n\n<b>✅ Total Active Service: </b><code>{total_active}</code>\
        \n➖➖➖➖➖➖➖➖➖➖➖➖➖\
        \n\n<b>❌ Total Expired Service: </b><code>{total_deactive}</code>\
        \n➖➖➖➖➖➖➖➖➖➖➖➖➖\
        \n\n<b>🌈 Super User: </b><code>{user.is_superuser}</code>\
        \n.
    """
    return text

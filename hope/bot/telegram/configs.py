import os

CHANNEL_HELP = 'Helpcx'
CHANNEL_SPONSER = 'VPN443IR'
USER_SUPORTE = 'ADM_VPN443IR'
ADMINS_LIST = [219171506, ]
TOKEN = os.environ.get('TOKEN')
PROXY_HTTP = None  # '192.168.138.200:8081'
PROXY_SOCKS = os.environ.get('PROXY')
MESSAGES = {
    "start_message": "💫 سلام خوش آمدید 💫\nلطفا یکی از گزینه ها را انتخاب کنید .\n‌‌‌‌",
    "message_error_test_config": "کاربر گرامی شما قبلا کانفیگ تست خود را دریافت کرده اید . شما هر هفته یک بار میتوانید کانفیگ تست دریافت کنید ❗️❗️\n‌‌‌‌",
    "message_get_volume": "لطفا حجم مورد نیاز خود را انتخاب کنید . \nتوجه کنید این حجم برای یک ماه قابل استفاده است. \n‌‌‌‌",
    "message_get_country": "🎗 لوکیشن دلخواه خود را انتخاب کنید\nلوکیشن های ایران قابلیت دور زدن اینترنت ملی را دارند\nبه همین جهت هزینه انها نسبت به کانفیگ های دیگر کشور ها بیشتر است . \n‌‌‌",
    "voucher_code": "📍لطفا شماره ووچر (e-voucher) را ارسال کنید (10 رقمی)",
    "voucher_active": "📍لطفا کد فعال سازی ووچر (Activation Code) (16 رقم)را ارسال کنید",
    "voucher_code_len_invalid": "💬 شماره ووچر ده رقم است ❌",
    "voucher_active_len_invalid": "📍لطفا کد فعال سازی ووچر (Activation Code) را ارسال کنید (کد 16 رقمی)",
    "message_not_balance": "❌موجودی شما کافی نیست لطفا از منوی کیف پول اکانت خود را شارژ کنید❌",
    "message_not_config_exseist": "❌در حال حاظر کانفیگ مورد نظر شما وجود ندارد بزودی اضافه خواهد شد❌",
    "message_not_service": "❗️شما دارای سرویس فعال نمی باشید",
    "message_file_config": "فایل زیر مجموعه کانفیگ های شما است ✅",
    "message_error_voucher_active": "❗️ووچر ارسالی نامعتبر یا قبلا استفاده شده است.",
    "message_success_payement": "حساب شما شارژ شد ✅",
    "message_config_expire_error":"❌ تاریخ انقضای کانفیگ شما به پایان رسیده است ",
    "message_server_max_config":"ظرفیت سرور مورد نظر تکمیل شده است لطفا از سرور های دیگر استفاده کنید",
    
    
    # Admin
    "message_admin_section": "🐧 Welcome to the admin Section\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nPlease choose one of the following options to CRUD",
    "message_admin_get_config_info": "⚡️⚡️<b>Config Info</b>⚡️\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nPlease send your v2ray config",
    "message_admin_get_user_info": "⚡️⚡️<b>User Info</b>⚡️\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nSend your username/userid",
    "message_admin_del_user_service": "⚡️⚡️<b>Delete User Services</b>⚡️\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nSend the UUID or config hash to remove the service from server/xui\n",
    "message_admin_get_total_users": "⚡️⚡️<b>General Inforamtion</b>⚡️\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n<code>🔘•</code> Members: <code>{}</code>\n➖➖➖➖➖➖➖➖\n<code>🔘•</code> Configs in use: <code>{}</code>\n➖➖➖➖➖➖➖➖\n<code>🔘•</code> Total services: <code>{}</code>\n.",
    "message_admin_increase_walet": "💰💰<b>Increase Wallet</b>💰\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nTo increase user wallet send user id with mony number\n\n❇️ Example:\n💵 userID:mony\n💵 124455:1000",
    "message_admin_decrease_walet": "💰💰<b>Decrease Wallet</b>💰\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nTo increase user wallet send user id with mony number\n\n❇️ Example:\n💵 userID:mony\n💵 124455:1000",
    "message_admin_balance_update": "⚡️⚡️<b>Update User Balance</b>⚡️\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nThe target user balance has been successfully updated ✅\n\n🔘User ID: <code>{}</code>\n🔘Current balance: <code>{}</code>",    
    "message_admin_show_config_info": "♻️<b>Delete Service Info</b>♻️\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n<b>Are you sure you want to delete the following service ⁉️</b>\n\nID: <code>{}</code>\n➖➖➖➖➖➖➖➖\nIP: <code>{}</code>\n➖➖➖➖➖➖➖➖\nPort: <code>{}</code>\n➖➖➖➖➖➖➖➖\nProtocol: <code>{}</code>\n➖➖➖➖➖➖➖➖\nRemark: <code>{}</code>\n➖➖➖➖➖➖➖➖\nUUID: <code>{}</code>",
    "message_admin_uuid_not_found_err": "❌<b>UUID Error<b>❌\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nYour entered uuid was not found, please check again",
    "message_admin_config_not_found_err": "❌<b>Config Hash Error</b>❌\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nYour entered config hash was not found\nplease make sure you are sending a correct config hash",
    "message_admin_user_not_found_err": "❌<b>User Error</b>❌\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nYour entered userID was not found, please try again",
    "message_admin_remove_config_err": "❌<b>Remove Service Error</b>❌\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nThere's a problem we can't remove the service, please try again.",
    "message_admin_remove_config_success": "Your service was successfully removed ✅",
}


PERFECTMONEY_USER = "15226661"
PERFECTMONEY_PASSWORD = "reza2020"
PERFECTMONEY_USD = "U42122089"
PERFECTMONEY_PROXY = None
PERFECTMONEY_PROXY = {"http": "socks5h://"+PROXY_SOCKS,"https": "socks5h://"+PROXY_SOCKS} if PROXY_SOCKS else False
BOT_USERNAME = "VPN443bot"
CHANNEL_PAYED = -1001816163876
CHANNEL_PAYED_CONFIG = -1001813798029

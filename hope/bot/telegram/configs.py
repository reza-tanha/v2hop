import os

CHANNEL_HELP = 'Helpcx'
CHANNEL_SPONSER = 'VPN443IR'
USER_SUPORTE = 'ADM_VPN443IR'
ADMINS_LIST = [219171506, ]
TOKEN = os.environ.get('TOKEN')
PROXY_HTTP = None  # '127.0.0.1:2021'
PROXY_SOCKS = os.environ.get('PROXY')
MESSAGES = {
    "start_message": "💫 <b>سلام به ربات V2Shop  خوش آمدید</b> 💫\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nلطفا برای ادامه روی یکی از گزینه زیر کلیک نمایید 👇🏻\n.",
    "message_error_test_config": "کاربر گرامی شما قبلا کانفیگ تست خود را دریافت کرده اید . شما هر هفته یک بار میتوانید کانفیگ تست دریافت کنید ❗️❗️\n‌‌‌‌",
    "message_choice_volume": "📉 <b>انتخاب میزان ترافیک</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nلطفا حجم مورد نیاز خود را انتخاب نمایید، حجم انتخاب شده فقط برای یک ماه قابل استفاده است",
    "message_choice_country": "🌐 <b>انتخاب لوکیشن VPN</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nلوکیشن دلخواه خود را انتخاب نمایید\n\nلوکیشن های ایران قابلیت دور زدن اینترنت ملی را دارند\nبه همین جهت هزینه انها نسبت به کانفیگ های دیگر کشور ها بیشتر است . \n‌‌‌",
    "message_choice_country_test": "🌐 <b>انتخاب لوکیشن VPN</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nلوکیشن دلخواه خود را انتخاب نمایید\n\n⚠️ در حالت تست قابلیت چینج لوکیشن را ندارید پس لطفا در انتخاب خود دقت نمایید",
    "message_not_config_exseist": "❌در حال حاظر کانفیگ مورد نظر شما وجود ندارد بزودی اضافه خواهد شد❌",
    "message_not_service": "❗️شما دارای سرویس فعال نمی باشید",
    "message_config_expire_error": "❌ تاریخ انقضای کانفیگ شما به پایان رسیده است ",
    "message_server_max_config": "ظرفیت سرور مورد نظر تکمیل شده است لطفا از سرور های دیگر استفاده کنید",
    "message_choice_support": "📨 <b>بخش پشتیبانی</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\nلطفا یکی از پشتیبان های زیر را انتخاب نمایید 👇🏻",
    "message_support_section": "📨 <b>ارسال پیام</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n💬 لطفا پیام خود را بفرستید تا برای ادمین ارسال شود. \n\n⏳ زمان پاسخگویی به سوال شما بین 1 دقیقه الی 2 ساعت  متغیر خواهد بود.\n\n⌛️در صورت دریافت نکردن پاسخ میتوانید پیام خود را برای ادمین دیگر ارسال نمایید.\n\n⚠️ لطفا در طول گفتگو روی هیچ دکمه ای کلیک نکنید و فقط پیام های خود را ارسال نمایید، برای پایان دادن به گفتگو کامند /start یا دکمه 'پایان گفتگو' را کلیک نمایید.",
    "message_choice_another_admin": "📨 <b>بخش پشتیبانی</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\nپشتیبان مورد نظر در دسترس نمیباشد لطفا یکی دیگر از پشتیبان ها را انتخاب نمایید ❌",
    "message_end_support_conversation": "گفتگوی شما به پایان رسید ✅\n\nدرصورت رضایت میتوانید ربات را به دوستان خود معرفی کنید ❤️\n.",
    "message_block_user": "⛔️ <b>مسدود شدن اکانت</b> ⛔️\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nبه دلیل فعالیت های نادرست، اکانت شما مسدود میباشد",
    "message_bot_updating": "♻️ <b>ربات در حال حاضر در دسترس نیست</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nممکن است به دلیل یک خطای فنی باشد که ما در حال تلاش برای رفع آن هستیم، لطفا صبور باشید ❤️",
    "message_reloc_not_enogh_volume_error": "🌐 <b>خطا در تغیر لوکیشن</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nحجم سرویس شما کمتر از 500 مگابایت است و قابلت تغیر لوکیشن ندارید❌",
    "message_list_my_services": "♦️ <b>سرویس های من</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n🔹با کلیک کردن بر روی هر سرویس میتوانید جزئیات سرویس را مشاهد نمایید و همچنین میتوایند لوکیشن سرویس خود را تغیر دهید.\n\n⚠️ دقت داشته باشید که <b>فقط 3 دفعه </b>میتوانید لوکیشن سرویس خود را تغیر دهید.\n\n⚠️ اگر لوکیشن سرویس خود را به لوکیشن ایران یا بلعکس از ایران به خارج تغیر دهید، مابه التفاوت هزینه بر روی موجودی شما اعمال خواهد شد.",
    "message_change_location_limit_error": "⛔️ شما فقط 3 بار قادر به عوض کردن کانفیگ خود هستید ⛔️",

    # Balance
    "message_get_voucher_code": "💸 <b>افزایش موجودی</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n💰 موجودی فعلی:‌ <b>{} تومان</b>\n\n🔸 لطفا برای افزایش موجودی ابتدا کانال راهنما را مشاهد و نحوه خرید پرفکت مانی را یاد بگیرید.\n\n🔹 بعد از خرید پرفکت مانی لطفا شماره 10 رقمی ووچر یا همان e-voucher را ارسال نمایید",
    "message_get_voucher_activate_code": "💸 <b>افزایش موجودی</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nلطفا کد 16 رقمی فعال سازی ووچر یا همان Activation Code را ارسال نمایید",
    "message_voucher_code_type_error": "❌ <b>افزایش موجودی</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nلطفا شماره 10 رقمی ووچر یا همان e-voucher را به درستی ارسال نمایید ❌",
    "message_voucher_code_len_error": "❌ <b>افزایش موجودی</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nلطفا مقدار گفته شده را به درستی وارد نمایید، شماره ووچر ده رقم است ❌",
    "message_voucher_activate_len_error": "❌ <b>افزایش موجودی</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nلطفا کد 16 رقمی فعال سازی ووچر یا همان Activation Code را به درستی ارسال  نمایید ❌",
    "message_not_balance": "❌موجودی شما کافی نیست لطفا از منوی کیف پول اکانت خود را شارژ کنید❌",
    "message_voucher_activate_error": "❌ <b>افزایش موجودی</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n❗️ووچر ارسالی نامعتبر یا قبلا استفاده شده است.",
    "message_success_payement": "حساب شما شارژ شد ✅",

    # Admin
    "message_admin_section": "🐧 Welcome to the admin Section\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nPlease choose one of the following options to CRUD",
    "message_admin_get_config_info": "⚡️ <b>Config Info</b> ⚡️\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nPlease send your v2ray config",
    "message_admin_get_user_info": "⚡️ <b>User Info</b> ⚡️\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nSend your username/userid",
    "message_admin_del_user_service": "⚡️ <b>Delete User Services</b> ⚡️\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nSend the UUID or config hash to remove the service from server/xui",
    "message_admin_get_total_users": "⚡️ <b>General Inforamtion</b> ⚡️\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n<code>🔘•</code> Members: <code>{}</code>\n➖➖➖➖➖➖➖➖\n<code>🔘•</code> Configs in use: <code>{}</code>\n➖➖➖➖➖➖➖➖\n<code>🔘•</code> Total services: <code>{}</code>\n.",
    "message_admin_increase_walet": "💰 <b>Increase Wallet</b> 💰\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nTo increase user wallet send user id with mony number\n\n❇️ Example:\n💵 userID:mony\n💵 124455:1000",
    "message_admin_decrease_walet": "💰 <b>Decrease Wallet</b> 💰\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nTo increase user wallet send user id with mony number\n\n❇️ Example:\n💵 userID:mony\n💵 124455:1000",
    "message_admin_balance_update": "⚡️ <b>Update User Balance</b> ⚡️\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nThe target user balance has been successfully updated ✅\n\n🔘User ID: <code>{}</code>\n🔘Current balance: <code>{}</code>",
    "message_admin_show_config_info": "♻️ <b>Delete Service Info</b> ♻️\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n<b>Are you sure you want to delete the following service ⁉️</b>\n\nID: <code>{}</code>\n➖➖➖➖➖➖➖➖\nIP: <code>{}</code>\n➖➖➖➖➖➖➖➖\nPort: <code>{}</code>\n➖➖➖➖➖➖➖➖\nProtocol: <code>{}</code>\n➖➖➖➖➖➖➖➖\nRemark: <code>{}</code>\n➖➖➖➖➖➖➖➖\nUUID: <code>{}</code>",
    "message_admin_uuid_not_found_err": "❌ <b>UUID Error<b> ❌\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nYour entered uuid was not found, please check again",
    "message_admin_config_not_found_err": "❌ <b>Config Hash Error</b> ❌\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nYour entered config hash was not found\nplease make sure you are sending a correct config hash",
    "message_admin_user_not_found_err": "❌ <b>User Error</b> ❌\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nYour entered userID was not found, please try again",
    "message_admin_remove_config_err": "❌ <b>Remove Service Error</b> ❌\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nThere's a problem we can't remove the service, please try again.",
    "message_admin_remove_config_success": "Your service was successfully removed ✅",
    "message_admin_update_bot": "⚡️ <b>Change Bot Status</b> ⚡️\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nClick on the following buttons to activate or deactivate bot.",
    "message_admin_enable_bot_update": "The bot was activated and made available to all users ✅",
    "message_admin_disable_bot_update": "The bot has been disabled and is only available for admins 🚫",
    "message_admin_user_access": "The user was successfully {}"
}


PERFECTMONEY_USER = "15226661"
PERFECTMONEY_PASSWORD = "reza2020"
PERFECTMONEY_USD = "U42122089"
PERFECTMONEY_PROXY = None
PERFECTMONEY_PROXY = {"http": "socks5h://"+PROXY_SOCKS,
                      "https": "socks5h://"+PROXY_SOCKS} if PROXY_SOCKS else False
BOT_USERNAME = "VPN443bot"
CHANNEL_PAYED = -1001816163876
CHANNEL_PAYED_CONFIG = -1001813798029

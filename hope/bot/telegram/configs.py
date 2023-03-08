import os

PROXY_HTTP = os.environ.get('PROXY_HTTP')
PROXY_SOCKS = "127.0.0.1:2021"#os.environ.get('PROXY')

# Perfect Money
PERFECTMONEY_USER = os.environ.get('PERFECTMONEY_USER')
PERFECTMONEY_PASSWORD = os.environ.get('PERFECTMONEY_PASSWORD')
PERFECTMONEY_USD = os.environ.get('PERFECTMONEY_USD')
PERFECTMONEY_PROXY = {"http": "socks5h://"+PROXY_SOCKS,
                      "https": "socks5h://"+PROXY_SOCKS} if PROXY_SOCKS else False

# Channel
TOKEN = os.environ.get('TOKEN')
BOT_USERNAME = os.environ.get('BOT_USERNAME')
CHANNEL_PAYED = os.environ.get('CHANNEL_PAYED')
CHANNEL_PAYED_CONFIG = os.environ.get('CHANNEL_PAYED_CONFIG')
CHANNEL_HELP = os.environ.get('CHANNEL_HELP')
CHANNEL_SPONSER = os.environ.get('CHANNEL_SPONSER')
USER_SUPORTE = os.environ.get('USER_SUPORTE')
SERVERS_PORT =  os.environ.get('SERVERS_PORT')



MESSAGES = {
    "start_message": "💫 <b>سلام به ربات V2Shop  خوش آمدید</b> 💫\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nلطفا برای ادامه روی یکی از گزینه زیر کلیک نمایید 👇🏻\n.",
    "message_error_test_config": "کاربر گرامی شما قبلا کانفیگ تست خود را دریافت کرده اید . شما هر هفته یک بار می توانید کانفیگ تست دریافت کنید ❗️❗️\n‌‌‌‌",
    "message_choice_volume": "📉 <b>انتخاب میزان ترافیک</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nلطفا حجم مورد نیاز خود را انتخاب نمایید، حجم انتخاب شده فقط برای یک ماه قابل استفاده است",
    "message_choice_country": "🌐 <b>انتخاب لوکیشن VPN</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nلوکیشن دلخواه خود را انتخاب نمایید\n\nلوکیشن های ایران قابلیت دور زدن اینترنت ملی را دارند\nبه همین جهت هزینه انها نسبت به کانفیگ های دیگر کشور ها بیشتر است . \n‌‌‌",
    "message_choice_country_test": "🌐 <b>انتخاب لوکیشن VPN</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nلوکیشن دلخواه خود را انتخاب نمایید\n\n⚠️ در حالت تست قابلیت چینج لوکیشن را ندارید پس لطفا در انتخاب خود دقت نمایید",
    "message_not_config_exseist": "❌در حال حاظر کانفیگ مورد نظر شما وجود ندارد بزودی اضافه خواهد شد❌",
    "message_not_service": "❗️شما دارای سرویس فعال نمی باشید",
    "message_config_expire_error": "❌ تاریخ انقضای کانفیگ شما به پایان رسیده است ",
    "message_server_max_config": "ظرفیت سرور مورد نظر تکمیل شده است لطفا از سرور های دیگر استفاده کنید",
    "message_choice_support": "📨 <b>بخش پشتیبانی</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\nلطفا یکی از پشتیبان های زیر را انتخاب نمایید 👇🏻",
    "message_support_section": "📨 <b>ارسال پیام</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n💬 لطفا پیام خود را بفرستید تا برای ادمین ارسال شود. \n\n⏳ زمان پاسخگویی به سوال شما بین 1 دقیقه الی 2 ساعت  متغیر خواهد بود.\n\n⌛️در صورت دریافت نکردن پاسخ می توانید پیام خود را برای ادمین دیگر ارسال نمایید.\n\n⚠️لطفا در طول گفتگو روی هیچ دکمه ای کلیک نکنید و فقط پیام های خود را ارسال نمایید در غیر اینصورت پیام های بعدی شما برای پشتیبان انتخاب شده ارسال نخواهد شد و باید دوباره دکمه پشتیبانی را کلیک و بعد پشتیبان قبلی خود را انتخاب نمایید تا بتوانید پیام های جدید را راسال کنید\n\nبرای پایان دادن به گفتگو کامند /start یا دکمه 'پایان گفتگو' را کلیک نمایید.",
    "message_choice_another_admin": "📨 <b>بخش پشتیبانی</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\nپشتیبان مورد نظر در دسترس نمی باشد لطفا یکی دیگر از پشتیبان ها را انتخاب نمایید ❌",
    "message_end_support_conversation": "گفتگوی شما به پایان رسید ✅\n\nدرصورت رضایت می توانید ربات را به دوستان خود معرفی کنید ❤️\n.",
    "message_block_user": "⛔️ <b>مسدود شدن اکانت</b> ⛔️\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nبه دلیل فعالیت های نادرست، اکانت شما مسدود می باشد",
    "message_support_send_success": "📨 پیام شما با موفقیت ارسال شد",
    "message_bot_updating": "♻️ <b>ربات در حال حاضر در دسترس نیست</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nممکن است به دلیل یک خطای فنی باشد که ما در حال تلاش برای رفع آن هستیم، لطفا صبور باشید ❤️",
    "message_reloc_not_enogh_volume_error": "🌐 <b>خطا در تغیر لوکیشن</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nحجم سرویس شما کمتر از 500 مگابایت است و قابلت تغیر لوکیشن ندارید❌",
    "message_list_my_services": "♦️ <b>سرویس های من</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n🔹با کلیک کردن بر روی هر سرویس می توانید جزئیات سرویس را مشاهد نمایید و همچنین میتوایند لوکیشن سرویس خود را تغیر دهید.\n\n⚠️ دقت داشته باشید که <b>فقط 3 دفعه </b>می توانید لوکیشن سرویس خود را تغیر دهید.\n\n⚠️ اگر لوکیشن سرویس خود را به لوکیشن ایران یا بلعکس از ایران به خارج تغیر دهید، مابه التفاوت هزینه بر روی موجودی شما اعمال خواهد شد.",
    "message_change_location_limit_error": "⛔️ شما فقط 3 بار قادر به عوض کردن کانفیگ خود هستید ⛔️",

    # Balance
    "message_get_voucher_code": "💸 <b>افزایش موجودی</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n💰 موجودی فعلی:‌ <b>{} تومان</b>\n\n🔸 لطفا برای افزایش موجودی ابتدا کانال راهنما را مشاهد کنید.\n\n🔹 برای شارژ حساب لطفا به ولت زیر مقدار شارژ دلخواه خود را وارد کنید  سپس لینک یا ایدی ترنزاکشن را ارسال کنید \n\n",
    "message_get_voucher_activate_code": "💸 <b>افزایش موجودی</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nلطفا کد 16 رقمی فعال سازی ووچر یا همان Activation Code را ارسال نمایید",
    "message_voucher_code_type_error": "❌ <b>افزایش موجودی</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nلطفا شماره 10 رقمی ووچر یا همان e-voucher را به درستی ارسال نمایید ❌",
    "message_transactionid_len_error": "❌ <b>افزایش موجودی</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n ایدی تراکنش 64 رقم است ❌ \n‌‌‌‌",
    "message_voucher_activate_len_error": "❌ <b>افزایش موجودی</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nلطفا کد 16 رقمی فعال سازی ووچر یا همان Activation Code را به درستی ارسال  نمایید ❌",
    "message_not_balance": "❌موجودی شما کافی نیست لطفا از منوی کیف پول اکانت خود را شارژ کنید❌",
    "message_voucher_activate_error": "❌ <b>افزایش موجودی</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n❗️ووچر ارسالی نامعتبر یا قبلا استفاده شده است.",
    "message_success_payement": "حساب شما شارژ شد ✅",
    "message_transaction_id_invalid": "این تراکنش قبلا ثبت شده است ❌",
    "message_transaction_not_verified": "این تراکنش هنوز در شبکه ترون ثبت نشده یا موفقیت امیز نبوده است ❌",
    "message_get_user_wallat": "💸 برای امنیت پرداخت های خود ابتدا ادرس کیف پول (والت)  ترون خود را ارسال کنید \n‌‌‌",
    "message_get_user_wallat_not_valid": "ولت نامعتبر است 😐 \n‌‌‌",
    "message_success_charjid": "حساب شما با موفقیت شارژ شد ✅\nموجودی جدید : {} تومان \n‌‌‌",

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
    "message_admin_user_access": "The user was successfully {}",
    "message_admin_send_universal_msg": "📢 <b>Send Msg</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nPlease choose one of the following options",
    "message_admin_send_to_all_msg": "📢 Send Msg\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nSend your message to forward to all users",
    "message_admin_send_to_one_msg": "📢 Send Msg\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nSend your message to forward to the user\n\nPlease write your userID in the first line and text msg in the following lines",
    "message_admin_send_msg_success": "📢 Send Msg\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nYour message has been successfully sent ✅",
}

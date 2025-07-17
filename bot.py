import os
os.system("pip install pyTelegramBotAPI")
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# توكن البوت
TOKEN = '8025661564:AAGYlq0ZNGRU0cM8kvzBJm9UrH4AYuhn7s4'
bot = telebot.TeleBot(TOKEN)

# رابط موقع الميني آب ديالك
AI_TOOLS_URL = "https://powerhelper.github.io/miniapp-1xbet/"

# رسالة الترحيب
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id, 
        "👛 مرحبًا بك في محفظتك الإلكترونية!\n"
        "🔗 اضغط على الزر أدناه لفتح المحفظة داخل التطبيق.",
        reply_markup=get_wallet_button()
    )

# زر الدخول إلى المحفظة كميني آب
def get_wallet_button():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(
            text="👀 عرض المحفظة", 
            web_app={"url": AI_TOOLS_URL}  # هادي اللي كتخليها تخدم كميني آب
        )
    )
    return markup

# تشغيل البوت
bot.polling()

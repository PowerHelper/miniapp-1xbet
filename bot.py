import os
os.system("pip install pyTelegramBotAPI")
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# توكن البوت الجديد
TOKEN = '8366050188:AAFdgNUJ0KUGBo7JDYujyCmI4lJcDMQ38OA'
bot = telebot.TeleBot(TOKEN)

# رابط الميني-آب ديالك
MINI_APP_URL = "https://powerhelper.github.io/bot/index.html"  # عوض بالرابط الصحيح ديال GitHub Pages ديالك

# رسالة الترحيب
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "🎮 مرحبًا بك في لعبة الطيارة مع كود برومو خاص بك!\n"
        "🔗 اضغط على الزر أدناه لفتح اللعبة داخل التطبيق.",
        reply_markup=get_game_button()
    )

# زر الدخول إلى الميني-آب
def get_game_button():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(
            text="🚀 ابدأ اللعب", 
            web_app={"url": MINI_APP_URL}
        )
    )
    return markup

# تشغيل البوت
bot.polling()


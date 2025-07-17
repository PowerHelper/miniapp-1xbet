import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8025661564:AAGYlq0ZNGRU0cM8kvzBJm9UrH4AYuhn7s4"
bot = telebot.TeleBot(TOKEN)

# رابط صفحة الميني آب
MINI_APP_URL = "https://yourwebsite.com/index.html"  # هنا دير رابط موقعك فيه index.html

def get_game_button():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(
            text="🚀 العب لعبة الطائرة",
            web_app={"url": MINI_APP_URL}
        )
    )
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🎮 مرحباً بك في لعبة الطائرة على 1XBET!\nاضغط على الزر أدناه للعب واستعمال كود البرومو الخاص بك.",
        reply_markup=get_game_button()
    )

bot.polling()

import telebot
import time
import os

TOKEN = os.environ.get('TOKEN')  # Берет токен из Render
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "✅ Бот работает с новым токеном!")

print("✅ Бот запущен безопасно!")

while True:
    try:
        bot.infinity_polling(timeout=60)
    except Exception as e:
        print(f"Ошибка: {e}")
        time.sleep(5)

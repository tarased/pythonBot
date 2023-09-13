import telebot

# токен бота, которого мы используем
bot = telebot.TeleBot('6535944016:AAEEHR6N_pZeQQNRb-IKRI5vCqQoNmrBOFo')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я твой бот. Как я могу помочь тебе?")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Запуск бота
if __name__ == "__main__":
    bot.polling()
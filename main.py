import telebot



# токен бота, которого мы используем
bot = telebot.TeleBot('6535944016:AAEEHR6N_pZeQQNRb-IKRI5vCqQoNmrBOFo')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я твой бот для постинга")

# Обработчик текстовых сообщений
'''@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)'''

@bot.message_handler(commands=['post'])
def handle_post(message):
    channel_id = '-1001928782688'
    text_to_post = 'YOUR_TEXT'
    bot.send_message(channel_id, text_to_post)


# Запуск бота
if __name__ == "__main__":
    bot.polling()
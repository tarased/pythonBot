import telebot
from telebot import types

# токен бота, которого мы используем
bot = telebot.TeleBot('6535944016:AAEEHR6N_pZeQQNRb-IKRI5vCqQoNmrBOFo')
channel_id = '-1001928782688'
user_state = {}
publicText = ''


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_state[message.chat.id] = None
    markup = types.InlineKeyboardMarkup()
    buttonCreatePost = types.InlineKeyboardButton('Создать пост', callback_data='buttonCreatePost')
    buttonEditPost = types.InlineKeyboardButton('Отредактировать пост', callback_data='buttonEditPost')
    markup.add(buttonCreatePost, buttonEditPost)
    bot.send_message(message.chat.id, 'Привет! Я твой бот для постинга. Выбери опцию:', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'buttonCreatePost':
        bot.send_message(call.message.chat.id, "Какое сообщение вы хотите опубликовать?")
        user_state[call.message.chat.id] = "waiting_for_posttext"
    if call.data == 'buttonPublic':
        bot.send_message(channel_id, publicText)
        bot.send_message(call.message.chat.id, f'Ваше сообщение {publicText} успешно опубликовано')
        user_state[call.message.chat.id] = None


# обработчик текстовых сообщений
@bot.message_handler(func=lambda message: user_state.get(message.chat.id) == "waiting_for_posttext")
def handle_user_text(message):
    global publicText
    user_input_text = message.text
    # bot.send_message(channel_id, user_input_text)
    markup = types.InlineKeyboardMarkup()
    buttonPublic = types.InlineKeyboardButton('Опубликовать', callback_data='buttonPublic')
    buttonAfter = types.InlineKeyboardButton('Отложить пост', callback_data='buttonAfter')
    markup.add(buttonPublic, buttonAfter)
    bot.send_message(message.chat.id, 'Вы желаете опубликовать пост прямо сейчас или отложить его?',
                     reply_markup=markup)
    publicText = user_input_text
    user_state[message.chat.id] = None






@bot.message_handler(commands=['post'])
def handle_post(message):
    text_to_post = 'YOUR_TEXT'
    bot.send_message(channel_id, text_to_post)


# Запуск бота
if __name__ == "__main__":
    bot.polling()

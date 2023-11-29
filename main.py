import telebot

bot = telebot.TeleBot('6707395191:AAG6jCvdV2uBegLro2o-hjC6SB5oJKkqWB8')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'я вас категорически приветствую', parse_mode='Markdown')


@bot.message_handler(commands=['info'])
def main(message):
    bot.send_message(message.chat.id,
                     'привет, меня зовут бот-гоблин, могу расскаазать анекдот и чуть поговорить с тобой')


@bot.message_handler(commands=['joke'])
def main(message):
    bot.send_message(message.chat.id, 'Зима. Подходит один мужик на улице к другому: \n -Огоньку не найдётся?'
                                      'А у первого бензиновая зажигалка, как оказалось, потекла в кармане.Ну, вынул, чиркнул, вся рука тут же в пламени.'
                                      'А второй прикурил от руки и говорит смеясь: \n   -Ну ты *** фокусник ')


bot.polling(none_stop=True, interval=0)

name = ''
surname = ''
age = 0


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
            bot.send_message(message.from_user.id,
                             'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?')
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Запомню : )')
    elif call.data == "no":
        pass


bot.infinity_polling()

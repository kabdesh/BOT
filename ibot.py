#Этот бот, работающий со списком учеников
import telebot
import lesson3

token = "524235729:AAGk6dO_krOoRf8FNBhLlUBGuaj5HNcYVv0"

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def check_message(message):
    if message.text == 'Список студентов' or message.text == 'список' or message.text =='список учеников':
        for student in lesson3.get_list_students():
            bot.send_message(message.chat.id, student[0])
    elif message.text == 'Средняя':
        bot.send_message(message.chat.id,lesson3.get_stud_aver_mark())
    elif message.text.isdigit():
        bot.send_message(message.chat.id,
                         lesson3.get_students_by_number(int(message.text))[0])
        bot.send_message(message.chat.id,
                         lesson3.get_students_by_number(int(message.text))[1])
    else:
        bot.send_message(message.chat.id, "Такой команды я не знаю")
bot.polling(none_stop=True)

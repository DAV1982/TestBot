import telebot
import schedule
import time

token = 'YOUR_TOKEN'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    with open('users.txt', 'a+') as chatids:
        print(message.chat.id, file=chatids)


@bot.message_handler(commands=['letters'])
def letters(message):
    if message.chat.id == 720489006:
        for i in open('users.txt', 'r').readlines():
            bot.send_message(i, 'Привет! Это тестовое сообщение!')
            schedule.every(1).minutes.do(letters)


if __name__ == "__main__":
    bot.polling(none_stop=True)

# .at("18:30", "Europe/Minsk")

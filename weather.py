from pyowm import OWM
import telebot

owm = OWM('b49964bcbfafd8714faaa2113a9ddc39')
mgr = owm.weather_manager()
bot = telebot.TeleBot("6398933517:AAEX2Wbt0Zuues8tLZviuGKxv6299jkTMsU")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature ('celsius')["temp"]

    answer = "Hi!" + "\n\n" + "In " + message.text + " now " + w.detailed_status + "."" \n\n"
    answer += "It`s " + str(temp) + " degrees outside now." "\n\n"

    if temp < 10:
        answer += "The weather in " + message.text + " is cold  so we recommend wearing winter clothes!"
    elif temp <19:
        answer += "The weather in " + message.text + " is normally so we recommend wearing autumn clothes!"
    else:
        answer += "The weather in " + message.text + " is hot so we recommend wearing summer clothes!"

    bot.send_message(message.chat.id, answer)

bot.infinity_polling( none_stop = True)


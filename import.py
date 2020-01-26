import pyowm
import telebot

owm = pyowm.OWM('48015b5020ebadcc49e3b07e13dd0da7', language = "ru")
bot = telebot.TeleBot("920493514:AAHDf1uB2XEzhDQuCDCk1fCW9DEyCQ6cNTU")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]
	answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
	answer += "Температура сейчас в районе " + str(temp) + "\n\n"

	if temp < 10:
		answer += "Сейчас офигеть как холодно одевай подштаны "   
	elif temp < 20:
		answer += "Сейчас холодно одевай шапуню " 
	else: 
		answer += "Температура норм одевай трусы " 

	bot.send_message(message.chat.id, answer)
bot.polling( none_stop = True )

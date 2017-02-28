import telegram

bot = telegram.Bot(token='284691436:AAExrkDmO8RfmfyVYE4LVTNxPixnaUW6F3U')

from telegram.ext import Updater
updater = Updater(token='284691436:AAExrkDmO8RfmfyVYE4LVTNxPixnaUW6F3U')
dispatcher = updater.dispatcher

def easy_start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Salem, Alem!")

def salem(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Aleikum asalam!")


from telegram.ext import CommandHandler
start_handler = CommandHandler('start', easy_start)
dispatcher.add_handler(start_handler)


salem_handler = CommandHandler('salem', salem)
dispatcher.add_handler(salem_handler)

def weather(bot, update):
	import requests
	from bs4 import BeautifulSoup 
	url = 'http://kazhydromet.kz/ru/almaty'
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	wtext = soup.select(".w_map span")[0].text
	bot.sendMessage(chat_id=update.message.chat_id, text=wtext)

weather_handler = CommandHandler('weather', weather)
dispatcher.add_handler(weather_handler)

updater.start_polling()







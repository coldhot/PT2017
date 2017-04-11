import telegram 
import requests 
import re
import json
from telegram.ext import CommandHandler
from bs4 import BeautifulSoup
from telegram.ext import MessageHandler, Filters
from threading import Timer
import time

bot = telegram.Bot(token = '377906628:AAFPT_paSvzoRjUPFJmfZHbn8X2TOYuVhSI')

from telegram.ext import Updater
updater = Updater(token = '377906628:AAFPT_paSvzoRjUPFJmfZHbn8X2TOYuVhSI')
dispatcher = updater.dispatcher

cards = {}

from logic import get_balance

with open('cards.json', 'r') as outfile:
    	cards = json.load(outfile)


while True:
	for user_id in cards.keys():
		for card_number in cards[user_id]:
			balance = get_balance(card_number)
			if balance <= 80:
				bot.sendMessage(chat_id=update.message.chat_id, text= "Баланс вашей карты %s" % card_number + " менее 80 тг. Пожалуйста, не забудьте пополнить баланс.")
	time.sleep(300)

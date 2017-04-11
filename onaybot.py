import telegram 
import requests 
import re
import json
from telegram.ext import CommandHandler
from bs4 import BeautifulSoup
from telegram.ext import MessageHandler, Filters

bot = telegram.Bot(token = '369816812:AAFr9hJ3wT_Lq9InKO9efd0zSxw6Hu3AzE0')

from telegram.ext import Updater
updater = Updater(token = '369816812:AAFr9hJ3wT_Lq9InKO9efd0zSxw6Hu3AzE0')
dispatcher = updater.dispatcher

from logic import *

def start(bot, update):
	text = 'Привет! Чтобы добавить свою карту Онай, наберите команду /new_card.'
	bot.sendMessage(chat_id=update.message.chat_id, text=text)

status = {}
cards = {}


with open('status.json', 'r') as outfile:
    	status = json.load(outfile)
with open('cards.json', 'r') as outfile:
    	cards = json.load(outfile)


def save_status(status):
	with open('status.json', 'w') as outfile:
		json.dump(status, outfile)

def save_cards(cards):
	with open('cards.json', 'w') as outfile:
		json.dump(cards, outfile)

custom_keyboard = [['Единая транспортная карта (ЕТК)'], ['Карта школьника'], ['Карта студента'], ['Социальная карта']]

def new_card(bot, update):
	global status
	user_id = update.message.from_user.id
	status[user_id] = 'choose_type'	
	save_status(status)
	global custom_keyboard
	bot.sendMessage(chat_id=update.message.chat_id, text='Пожалуйста, Выберите вашу карту:', reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard))
	echo(bot, update)

def echo(bot, update):
	global status
	global custom_keyboard
	global cards
	card = update.message.text	
	numberMask = 0	
	if card == 'Единая транспортная карта (ЕТК)':
		numberMask = '96431085033'
	else:
		numberMask = '96439085033'
	del status[user_id]
	save_status(status)
	bot.sendMessage(chat_id=update.message.chat_id, text='Пожалуйста, введите последние 8 цифр вашей онай-карты:', reply_markup = telegram.ReplyKeyboardRemove(custom_keyboard))
	status[user_id] = 'waiting_card'
	save_status(status)	
	user_id = update.message.from_user.id 
	if user_id in status:
		if status[user_id] == 'waiting_card':
			text = numberMask + update.message.text 
			pattern = re.compile('^\d{19}$')
			if pattern.match(text) != None: 	# card is correct, save this card
				card_number = text
				exist = check_card(card_number)
				if exist == True:
					if user_id in cards:
						if card_number not in cards[user_id]:
							cards[user_id].append(card_number)
							bot.sendMessage(chat_id=update.message.chat_id, text='Ваша карта %s успешно сохранена.' % card_number)
							bot.sendMessage(chat_id=update.message.chat_id, text='Для проверки баланса наберите команду /balance.')
							save_cards(cards)
						else:
							bot.sendMessage(chat_id=update.message.chat_id, text='Номер вашей карты уже сохранен.')
					else:
						cards[user_id] = [card_number]
						bot.sendMessage(chat_id=update.message.chat_id, text='Ваша карта %s успешно сохранена' % card_number)
						bot.sendMessage(chat_id=update.message.chat_id, text='Для проверки баланса наберите команду /balance.')
						save_cards(cards)
					del status[user_id]		
					save_status(status)		
				else:
					bot.sendMessage(chat_id=update.message.chat_id, text='Неверный формат карты. Пожалуйста, введите номер карты ещё раз.')
			else:
				bot.sendMessage(chat_id=update.message.chat_id, text='Неверный формат карты. Пожалуйста, введите номер карты ещё раз.')
		elif status[user_id] == 'choose_card':
			for card in cards[user_id]:
				custom_keyboard = []
				custom_keyboard.append([card])
			reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
			bot.sendMessage(chat_id=update.message.chat_id, text="Выберите карту, пожалуйста.", reply_markup=reply_markup)
			card_number = update.message.text
			bal = get_balance(card_number)
			bot.sendMessage(chat_id=update.message.chat_id, text= 'Ваш баланс: %d тг.' % bal, reply_markup=telegram.ReplyKeyboardRemove(custom_keyboard))
		else:
			text = 'Чтобы добавить свою карту Онай, наберите команду /new_card.'
			bot.sendMessage(chat_id=update.message.chat_id, text=text)
	else:
		text = 'Чтобы добавить свою карту Онай, наберите команду /new_card.'
		bot.sendMessage(chat_id=update.message.chat_id, text=text)

def balance(bot, update):
	user_id = update.message.from_user.id
	n = 0
	if user_id in cards:
		n = len(cards[user_id])
		if n == 0:
			text = 'Введите номер вашей онай карты, пожалуйста:'
			bot.sendMessage(chat_id=update.message.chat_id, text=text)
			card_number = update.message.text
			bal = get_balance(card_number)
			bot.sendMessage(chat_id=update.message.chat_id, text= 'Ваш баланс: %d тг.' % bal)
			custom_keyboard = [['Да', "Нет"]]
			bot.sendMessage(chat_id=update.message.chat_id, text= 'Хотите ли сохранить карту?', reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard))
			reply = update.message.text
			if reply == 'Да':
				cards[user_id] = [card_number]
				bot.sendMessage(chat_id=update.message.chat_id, text='Ваша карта %s успешно сохранена' % card_number)
				save_cards(cards) 
		elif n > 1:
			global status
			status[user_id] = 'choose_card'
			custom_keyboard = []
			for card in cards[user_id]:
				custom_keyboard.append([card])
			reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
			bot.sendMessage(chat_id=update.message.chat_id, text="Выберите карту, пожалуйста.", reply_markup=reply_markup)
			card_number = update.message.text
			bal = get_balance(card_number)
			del status[user_id]		
			save_status(status)
			bot.sendMessage(chat_id=update.message.chat_id, text= 'Ваш баланс: %d тг.' % bal, reply_markup = telegram.ReplyKeyboardRemove(custom_keyboard))
		else:
			card_number = cards[user_id][0]
			bal = get_balance(card_number)
			bot.sendMessage(chat_id=update.message.chat_id, text= 'Ваш баланс: %d тг.' % bal)
	else:
		text = 'У вас нет сохраненных карт. Чтобы добавить свою карту Онай, наберите команду /new_card.'
		bot.sendMessage(chat_id=update.message.chat_id, text=text)
		return False	

def delete(bot, update):
	user_id = update.message.from_user.id
	n = 0
	if user_id in cards:
		n = len(cards[user_id])
		if n == 0:
			text = 'У вас нет сохраненных карт. Чтобы добавить свою карту Онай, наберите команду /new_card.'
			bot.sendMessage(chat_id=update.message.chat_id, text=text)
			return False 
		elif n > 1:
			global status
			status[user_id] = 'choose_card'
			custom_keyboard = []
			for card in cards[user_id]:
				custom_keyboard.append([card])
			reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
			bot.sendMessage(chat_id=update.message.chat_id, text="Выберите карту, пожалуйста.", reply_markup=reply_markup)
			card_number = update.message.text
			cards[user_id].remove(card_number)
			save_cards(cards)
			bot.sendMessage(chat_id=update.message.chat_id, text= 'Ваша карта была успешна удалена.', reply_markup = telegram.ReplyKeyboardRemove(custom_keyboard))
		else:
			del cards[user_id]
			save_cards(cards)
			bot.sendMessage(chat_id=update.message.chat_id, text= 'Ваша карта была успешна удалена.')
	else:
		text = 'У вас нет сохраненных карт. Чтобы добавить свою карту Онай, наберите команду /new_card.'
		bot.sendMessage(chat_id=update.message.chat_id, text=text)
		return False	
	

	
new_card_handler = CommandHandler('new_card', new_card)
dispatcher.add_handler(new_card_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
 
balance_handler = CommandHandler('balance', balance)
dispatcher.add_handler(balance_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)


delete_handler = CommandHandler('delete', delete)
dispatcher.add_handler(delete_handler)

updater.start_polling()



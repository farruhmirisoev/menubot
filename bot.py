# -*- coding: utf-8 -*-
import config
import telebot

import json
import time
import datetime

bot = telebot.TeleBot(config.token)


def getTodayMenu():
	
	# get menu list from the json file
	with open('weekmenu.json', encoding='utf-8') as json_data:
	    menu = json.load(json_data)

	weekdayIndex = datetime.datetime.today().weekday()
	todayMenu = menu['weekdays'][weekdayIndex]

	naujin 	  = todayMenu["ujin"]["meal_title"]
	ujin_time = todayMenu["ujin"]["serve_time"]
	naobed    = todayMenu["obed"]["meal_title"]
	obed_time = todayMenu["obed"]["serve_time"]
	day       = todayMenu["day_title"]
	
	menuMessage = '<b>'+ day + '</b>\n<code>'+obed_time+'</code> - <code>obed</code> : '+ naobed + '  \n<code>'+ujin_time+'</code> - <code>ujin:</code> ' + naujin	

	return menuMessage
 

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
	bot.send_message(message.chat.id, getTodayMenu(), parse_mode='HTML')

# bot.send_message(message.chat.id, message.text);

# while True:
# 	bot.send_message(-165111791, 1);
# 	time.sleep(5)

if __name__ =="__main__":
	bot.polling(none_stop=True)
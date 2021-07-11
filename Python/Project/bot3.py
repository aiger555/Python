
# import telebot
# from pytube import YouTube

# TELEGRAM_TOKEN = "1786741150:AAF9gKI8UIThbhCqxeGTovSzBtDwteV3V_M"

# bot = telebot.TeleBot(TELEGRAM_TOKEN)

# url = 'https://www.youtube.com/watch?v=dJ4WArAeNf0'
# ydt = YouTube(url).streams.first().download()
# name_bot="бот"
# bot = telebot.TeleBot(bot)
# @bot.message_handler(commands=['text'])
# def send_welcome(message):
#     url = message.text
#     ydt = YouTube(url).streams.first().download()
#     video = open(ydt, 'rb')
#     bot.send_video(message.chat.id, video)

# bot.polling()

# import requests
# from bs4 import BeautifulSoup

# TELEGRAM_TOKEN = "1786741150:AAF9gKI8UIThbhCqxeGTovSzBtDwteV3V_M"

# bot = telebot.TeleBot(TELEGRAM_TOKEN)

# url = 'https://24.kg/'

# source = requests.get(url)
# main_text = source.text
# soup = BeautifulSoup(main_text, "html.parser")

# news = [zs.text for zs in soup.find_all('div', {'class': 'one'})]
# print(news[:10])
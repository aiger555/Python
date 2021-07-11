# import telebot
# import schedule
# import time
# TELEGRAM_TOKEN = "1737431821:AAHnjLyZhTLnktls3t_J3aa_bc6Lte2gvr8"
# bot = telebot.TeleBot(TELEGRAM_TOKEN)
# # @bot.message_handler(content_types = ['text'])
# def send_text(message):
#          bot.send_message('803478340', 'Что было вчера?')
#          bot.send_message('803478340', 'Что будет сегодня?')
#          bot.send_message('803478340', 'Какие сложност были?')

# schedule.every().day.at("20:35").do(send_text)
# bot.polling()
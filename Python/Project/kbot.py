# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor
# import schedule
# import time

# bot = Bot(token="1786741150:AAF9gKI8UIThbhCqxeGTovSzBtDwteV3V_M")
# dp = Dispatcher(bot)


# @dp.message_handler(commands=['start', 'help'])
# async def first_or_help_commands(message: types.Message):
#     await message.reply("Напиши мне что-нибудь!")

# @dp.message_handler(commands=['aigerim', ])
# async def cutomer_command(message):
#     await message.reply("Hi Aigerim")

# # если не указано, что обрабатывать точно, то по умолчанию обрабатывется текст
# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     await bot.send_message(msg.from_user.id, msg.text)
  

# @dp.message_handler(commands=['gera', ])
# def some_func():
#     print("I am just a lonely func")

# schedule.every().minute.do(some_func)


# while True:
#     schedule.run_pending()
#     time.sleep(1)


# if __name__ == '__main__':
#     executor.start_polling(dp)


# import telebot



# import pandas
# import telebot
# import aioschedule as schedule
# # import parser
 
# class KeneshBot:
#     help_text = '''
#     /fractions - для получения списка фракций
#     /deputies - для получения списка депутатов
#     /fractions {Название Фракции} - для вывода участников фракций. 
#     Пример: /fractions Ата Мекен
#     /deputy {ФИО} - для получения информации о депутате.
#     Пример: /deputy Абдылдаев Шералы Итибаевич
#     /update - Чтобы обновить базу данных о депутатах.
#     '''
#     __fractions = pandas.read_csv('deputies.csv')
#     fractonset = set(__fractions.fractions.to_list())
        
#     def show(self, args):
#         if len(args) <= 0:
#             return '\n'.join(self.fractionset)
#         else:
#             if args == "СДПК":
#                 frac = (f"Парламентская фракция {args}")
#             else:
#                 frac = (f'Парламентская фракция «{args}»')
        
#         if (frac) not in self.fractonset:
#             return f'Фракции с названием: {args} не существует'
#         else:
#             dep = self.__fractions[self.__fractions.fractions == frac]
#             dep = dep[['dep_fio', 'dep_link']][1:10].to_string()
#             return dep
 

 

# TOKEN = '1786741150:AAF9gKI8UIThbhCqxeGTovSzBtDwteV3V_M'
# bot = telebot.TeleBot(TOKEN)
# kbot= KeneshBot()

 
# @bot.message_handler(commands=['start', 'help'])
# def show(message):
#     bot.send_message(message.chat.id, kbot.help_text)
 
# @bot.message_handler(commands=['fractions'])
# def fractions(message):
#     args = message.text[11:]
#     bot.send_message(message.chat.id, kbot.show(args))

# if __name__ == '__main__':
#     bot.polling()
    

# 1
# names = ['aLfred', 'djonataN', 'irOn MAN', 'vasYa']
# new_list = list(map(lambda x:x.upper(), names))
# print(new_list)

# # 2
# numbers = [4, 17, 3, 90, 28, 55]
# lst = list(filter(lambda x: x%2, numbers))
# print(lst)

# # 3 
# from functools import reduce
# numbers = [4, 17, 3, 90, 28, 55]
# new_numbers = reduce(lambda x,y: y*x, numbers, 15)
# print(new_numbers)

# # 4
# palindromes = ['hello', 'sentences where punctuation', 45,'Able was I, ere I saw Elba', 34.0, 78.87, 'found', 'level', '12/11/21', 'radar','stats']
# palindromes = [str(x) for x in palindromes]


# new_spisok = []
# spisok2 = []
# new_spisok = [j.replace(' ', '').replace(',', '').lower() for j in palindromes ]
# new_spisok = [i for i in new_spisok if i == i[::-1]]
# new_spisok = ' '.join(new_spisok)
# print(new_spisok) 
    

# class Card_account():
#     def __init__(self, credit, comission, percentage):
#         self.credit = credit
#         self.comission = comission
#         self.percentage = percentage

#     def get_data(self):
#         return (f'СК - {self.credit}', 
#                 f'СВК - {self.comission}', 
#                 f'проценты по кредиту - {self.percentage}%'
#                 )

#     @property
#     def credit_calc(self):
#         return self.credit + self.comission + self.percentage
    
#     def hello(self):
#         self.hi = 'hi'

        
# def funcs():
#     сard = Card_account(16, 32, 54)
#     сard.hello()
#     print(сard.get_data(),
#             сard.credit_calc,
#             сard.hi
#             )


# funcs()



# txt=input(":")
# mp={} # словарь встречаемости
# while txt!="" : # вводим пока не будет пустой строки
#    words=txt.split()
#    for i in words :
#        if i not in mp :
#            mp[i]=1
#        else :
#            mp[i]+=1
#    txt=input(":")
# ss=list(mp.items()) # преобразуем словарь в список
# ss.sort(key = lambda x : x[1],  reverse=True ) # сортируем список по 2 полю
# for  x  in  ss:
#    print ("({0}  =>  {1})".format (x[0],  x[1]))
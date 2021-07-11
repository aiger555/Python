from abc import ABC, abstractmethod
# class BANK:
#     def __init__(self, card, increased, taking):
#         self.__card = card
#         self.__increased = increased
#         self.__taking = taking

#     def check(self):
#         if self.__card < self.__card:
#             self.__increased += self.__card
#         else:
#             print("Your money is not enough")
#         return self.__card


# bank = BANK(123, 435, 98)
# print(bank.check())

# class Technology(ABC):
#     @abstractmethod
#     def met(self):
#         pass

# class Cellphone(Technology):
#     __name = 'HI'
#     def met(self):
#         return 'My phone\'s model is xiomi'

# class Ipad(Cellphone):
#     def met(self):
#         return  self._Cellphone__name


# c = Cellphone()
# i = Ipad()
# print(c.met())
# print(i.met())

# class Contact:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone

#     def __str__(self):
#         return f'{self.name} - {self.phone}'
    
#     def __add__(self, contact):
#         print('Type name of contact: ')
#         name = input('write: ')
#         print('Type number: ')
#         phone = input('write: ')
#         new = {'name': name, 'phone' : phone}
#         contact.append(new)   
     

#     def __del__(self, contact):
#         print("Type contact number: ")
#         name = input('write: ')
#         for i in contact:
#             if i['name'] == name:
#                 print('Do you want to delete this contact?(y/n): ')
#                 delen = input('write: ')
#                 if delen == 'yes':
#                     contact.remove(i)
#                     print(f'The contact {i.name} was deleted')
  

#     def find(contact):
#         print('Type name of the contact: ')
#         name = input("write: ")
#         for i in contact:
#             if i['name'] == name:
#                 print(f'')


# contact = Contact('Aigerim, +56778')  



# def func(i):
#     lst = [1, 5, 6, 123, 3, 32, 9, 92, 4]
#     if i not in lst:
#         return -1
#     else:
#         return lst.index(i)

# print(func(4))





# from random import randint
 
# # Создание списка,
# # его сортировка по возрастанию
# # и вывод на экран
# a = []
# for i in range(10):
#     a.append(randint(1, 50))
# a.sort()
# print(a)
 
# # искомое число
# value = int(input())
 
# mid = len(a) // 2
# low = 0
# high = len(a) - 1
 
# while a[mid] != value and low <= high:
#     if value > a[mid]:
#         low = mid + 1
#     else:
#         high = mid - 1
#     mid = (low + high) // 2
 
# if low > high:
#     print("No value")
# else:
#     print("ID =", mid)





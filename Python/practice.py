
# class Peasant:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def action(self):
#         return f'My name is {self.name} and I will plow the land'

# class Baron(Peasant):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#     def action(self, obj, order_):
#         if obj.__class__.__name__ == 'Peasant':
#             return f'{obj.name} will {order_}'
#         else:
#             print('I have no rights to give orders to smbody who has higher rank')


# class Feudal_lord(Baron):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#     def action(self, obj, obj2, order_):
#         if obj.__class__.__name__ == 'Peasant' and obj2.__class__.__name__ == 'Baron':
#             return f'{obj.name} and {obj2.name}  will {order_}'
#         else:
#             print('I cannot give order')



# class King(Feudal_lord):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#     def action(self, obj, obj2, obj3, order_):
#         if obj.__class__.__name__ == 'Peasant' and obj2.__class__.__name__ == 'Baron' and obj3.__class__.__name__ == 'Feudal_lord':
#             return f'{obj.name}, {obj2.name} and {obj3.name} will {order_}'
#         else:
#             pass

# # p = Peasant('Pavel', 30)
# # print(p.action())
# # b = Baron('Bairon', 35)
# # print(b.action(p, 'dig up the fields'))
# # f = Feudal_lord('Fedya', 40)
# # print(f.action(p, b, 'prepare to the fighting'))
# # k = King('Petr I', 43)
# # print(k.action(p, b, f, 'prepare to the hunting'))


# # def decree(cl):
# #     if cl.__class__.__name__ == 'King':
# #         print(f'I can order to {f.name}, {b.name}, {p.name}')
# #     elif cl.__class__.__name__ == 'Feudal_lord':
# #         print(f'I can order to {b.name} and {p.name}')
# #     elif cl.__class__.__name__ == 'Baron':
# #         print(f'I can order only to {p.name}')
# #     elif cl == p:
# #         print('I cannot give orders')

# # decree(k)
# # decree(f)
# # decree(b)
# # decree(p)

# import psycopg2
# conn = psycopg2.connect(dbname='Aigerdb', user='Aigerim', 
#                         password='postgres')
# cursor = conn.cursor()

# cursor.execute('''DROP TABLE IF EXISTS scientist;
#         create table scientist (id integer, firstname varchar(100), lastname varchar(100));
#         insert into scientist (id, firstname, lastname) values (1, 'albert', 'einstein');
#         insert into scientist (id, firstname, lastname) values (2, 'isaac', 'newton');
#         insert into scientist (id, firstname, lastname) values (3, 'marie', 'curie');
#         select * from scientist;''')

# rows = cursor.fetchall()

# for i in rows:
#     print(i)

# conn.commit()
# cursor.close()
# conn.close()



# exercise 1
# def func(i):
#         if i % 2 == 1:
#             print(i, 'Weird')
#         elif i >= 6 and i <=20 and i % 2 ==0:
#             print(i, 'Weird')
#         else:
#             print(i, 'Not Weird')
    
# for g in range(1, 101):
#     func(g)



# exercise 2
# def leap_year(year):
#     if year % 4 == 0 and year % 100 != 0:
#         return True
#     elif year % 100 == 0 and year % 400 == 0:
#         return True
#     else:
#         return False
    
# print(leap_year(2014))



# exercise 3
# class Bank:
#     customers = []

#     @classmethod
#     def calculate_profit(cls, years):
#         profit = 0
#         for client in cls.customers:
#             if client.years < years:
#                 profit += client.total_payout - client.credit_amount
#             else:
#                 profit += client.monthly_payout * 12 * years - client.credit_amount
#         return profit

# class Customer:
#   def __init__(self, n, p, y):
#         p = p/100
#         self.credit_amount = n
#         self.percent = p
#         self.years = y
#         self.monthly_payout =  (n * p * (1 + p) ** y) / (12 * ((1 + p) **y) - 1)
#         self.total_payout = (self.monthly_payout * 12) * y
#         Bank.customers.append(self)

# c = Customer(100000, 15, 10)
# print(Bank.calculate_profit(10))


# exercise 4
# lst = [1, 34, 456, 734, 23, 9, 4]
# lst1 = [3, 5]

# def func(lst, lst1):
#     for i in lst:
#         if i > lst1[0] and i < lst1[1]:
#             lst.remove(i)
#             lst.append(0)
#     return lst

# print(func(lst, lst1))



# ***********************************
import string, random

# def random_(len):
#     return ''.join(random.choice(string.digits) for i in range(len))

# code = ['+996777', '+996222', '+996555', '+996500']

# for i in range(1000):
#     print(random.choice(code) + random_(6))
# ************************************

 

# class Phone:
#     beeline = []
#     o = []
#     megakom = []
# https://gist.github.com/eshenkulovilias/e842de3a958ceea00465237ce04c9b76
#     def __init__(self):
#         self.code = ['+996777', '+996222', '+996555', '+996500']
       

#     def phone_number(self, length):
#         generator =  ''.join(random.choice(string.digits) for i in range(length))
#         return random.choice(self.code) + generator

#     def generate_number(self):
#         for i in range(1000):
#             print(self.phone_number(6))


# p = Phone()
# p.generate_number()
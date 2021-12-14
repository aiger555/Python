# # ex.1
# def func(lst):
#     data_type = list(map(type, lst))
#     result = {lst[i]: data_type[i] for i in range(len(lst))}
#     return result
#
#
# print(func([1, 4.7, 'hi', False, None]))
#
# # ex.2
# a=int(input('кол-во строк: '))
# b=int(input('кол-во звездочек на строке: '))
# print(a*'{}\n'.format(b*'*'))
#
#
# # ex3
# a = [1, 54, 3, 6, 8, 90, 4, 2]
# b = [2, 4, 3, 87, 6, 32, 56, 90]
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
# print(c)
#
#
# # ex4
# def counter(digit):
#     result = 0
#     while digit > 0 and digit != float:
#         result += digit % 10
#         digit //= 10
#     return result
#
# print(counter(67))
#
# # ex5
# import psycopg2
# conn = psycopg2.connect(dbname='titanic', user='postgress', password='postgres')
#
# class CSV:
#   
# ()
#     cur.execute("""CREATE TABLE database(
#         id integer,
#         name varchar(50),
#         pol varchar(50),
#         age integer);
#     """)
#     with open(r'exam.csv', 'r') as f:
#         next(f)
#         cur.copy_from(f, 'database', sep='*********')
#
#     conn.commit()
#
#
#     def sorting(self):
#         self.cur.execute("SELECT name FROM database ORDER BY age ASC;")
#         row = self.cur.fetchall()
#         return row
#
#     def adding_row(self):
#         self.cur.execute("ALTER TABLE database ADD column surname VARCHAR(60);")
#         row = self.cur.fetchall()
#         return row
#
#     def updating_row(self):
#         self.cur.execute("UPDATE database SET name='Dante' WHERE id=2;")
#         updating = self.cur.fetchall()
#         return updating
#
#
#     def editing(self):
#         self.cur.execute("ALTER TABLE database ALTER COLUMN age SET NOT NULL;")
#         editted = self.cur.fetchall()
#         return editted
#
#     def find_name(self):
#         self.cur.execute("SELECT name FROM database WHERE pol = 'female';")
#         name = self.cur.fetchall()
#         return name

#  Exam number 5, part 1
# class Calculator:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def __str__(self):
#         return f"{self.brand}{self.model} is ready to work!"
#
#     def __add__(self, other):
#         return self.brand + other, self.model + other
#
#     def __sub__(self, other):
#         return self.brand - other, self.model - other
#
#     def __mul__(self, other):
#         return self.brand * other, self.model * other
#
#     def __div__(self, other):
#         return self.brand / other, self.model / other
#
#     def __floordiv__(self, other):
#         return self.brand // other, self.model // other
#
#     def __mod__(self, other):
#         return self.brand % other, self.model % other
#
# if __name__ == '__main__':
#     c = Calculator(10, 5)
#     print(c.__add__(2))
#     print(c.__sub__(3))
#     print(c.__mul__(4))
#     print(c.__div__(5))
#     print(c.__floordiv__(5))
#     print(c.__mod__(3))
#
# """ Мфгические методы - это методы, которые переопределяют действие по умолчанию, когда над объектом выполняются определённые махинации.
#  Конструктор __init__ - это операция создания объекта, где переопределяют некоторые свойтсва.
#   Абстракция — это наделение объекта характеристиками, которые отличают его от других объектов.
#  Nasledovaniye - Унаследование всеx атрибутов, методов в дочернем классе.
# Инкапсуляция — ограничение доступа к компонентам класса (методам и переменным). Некоторые  компоненты доступны только внутри класса.
# Полиморфизм - разное поведение одного и того же метода в разных классах.
# Экземпляр - это объект класса.
# Объект - это экземпляр класса.
#
# Класс - это некое описание, структура объекта. Например: из дерева делают бумагу.
# В данном случае дерево это класс, а бумага это экземпляр класса.
# Или по чертежу строят дома. Чертеж - класс, дома - экземпляры.
#
# """
# lst = [61, 228, 9]  # lst = [43, 234, 8]
# ls = []
# ls.append(lst[2])
# ls.append(lst[0])
# ls.append(lst[1])
#
# lst = map(str, ls)
# j = ''.join(lst)
# print(j) # У вас есть массив чисел, составьте из них максимальное число. Например: * [61, 228, 9] -> 961228
#
#
# def sum_(a):
#     for x in a:
#        x = x + (x+1)
#     return x
#
#
# def p(a):
#     n = 0
#     while n < len(a):
#         for x in a:
#             summ = x + (x+1)
#             n += 1
#         return summ #У вас есть массив чисел. Напишите два метода, которые вычисляют сумму этих чисел: с for-циклом, с while-циклом *
#
#
# print(sum(i for i in lst if i % 2 == 0)) #Напишите программу, которая принимает список = [122, 456, 656, 678, 807, 237] и
# # возвращает сумму всех четных чисел *
#
# students = {
#     'Aliya': 70,
#     'Stella': 80,
#     'Albina': 85,
#     'Akmaral': 85
# }
# s = {x : 100 for x in students}
# print(s) #Имеется следующий словарь студентов.
# # Как с помощью dict comprehension (генератор словарей) сделать так, ч
# # тобы у всех студентов было по 100 баллов в значениях?




# 2.5

# example = {
# 	   'iceberg': ['cold', 15, {'a', 'b'}, 33.98, 15/2, False],
# 	   'fire': ['hot', 46, ['cha', 'ching'], 81.13],
# 	   'earth': ['solid', 100, (13, 31, 1), 90.01, {'b':'c'}]
# 	   }

# elements = ['fire', 'storm', 'cloud', 'iceberg', 'volcano', 'earth']
 
# def phync(dic, ls):
#     for i in ls:
#         try:
#             plus = 0
#             for j in dic[i]:
#                 try:
#                     plus += j
#                 except TypeError:
#                     continue
#             print(f'{i} = {plus}')
#         except KeyError:
#             print(f'The key {i} doesn\'t exist')
# phync(example, elements)


# # 2.5.2
# from random import randint

# names = ['dhhgfjjhsa.txt', 'hhdsdahffh.txt', 'afdgdhjsds.txt', 
# 	'sggjghddss.txt', 'fjdjgdghdf.txt', 'sjssahjfga.txt', 
# 	'agsgdjhhfj.txt', 'gafadhadda.txt', 'hdagajfhhj.txt', 
# 	'fhjhafhdfa.txt']
# nano = names[randint(0, len(names)) - 1]
# with open(nano, 'w') as new:
#     pass

# def func(f_names):
#     for i in f_names:
#         try:
#             with open(i, 'r+') as f:
#                 f.write('Aigerim')
#         except FileNotFoundError:
#             print(f'The {i} does not exist')

# func(names)



# # homework1
# example = {
# 	   'iceberg': ['cold', 15, {'a', 'b'}, 33.98, 15/2, False],
# 	   'fire': ['hot', 46, ['cha', 'ching'], 81.13],
# 	   'earth': ['solid', 100, (13, 31, 1), 90.01, {'b':'c'}]
# 	   }

# elements = ['fire', 'storm', 'cloud', 'iceberg', 'volcano', 'earth']
 
# def phync(dic, ls):
#     for i in ls:
#         try:
#             plus = 0
#             for j in dic[i]:
#                 try:
#                     plus += j
#                 except TypeError:
#                     continue
#             print(f'{i} = {plus}')
#         except KeyError:
#             print(f'The key {i} doesn\'t exist')
# phync(example, elements)


# # homework2
# from random import randint

# names = ['dhhgfjjhsa.txt', 'hhdsdahffh.txt', 'afdgdhjsds.txt', 
# 	'sggjghddss.txt', 'fjdjgdghdf.txt', 'sjssahjfga.txt', 
# 	'agsgdjhhfj.txt', 'gafadhadda.txt', 'hdagajfhhj.txt', 
# 	'fhjhafhdfa.txt']
# nano = names[randint(0, len(names)) - 1]
# with open(nano, 'w') as new:
#     pass

# def func(f_names):
#     for i in f_names:
#         try:
#             with open(i, 'r+') as f:
#                 f.write('Aigerim')
#         except FileNotFoundError:
#             print(f'The {i} does not exist')

# func(names)


# 2.12
# ex. number 2
# dan_text = """Advertising companies say advertising is necessary and important. 
# It informs people about new products. Advertising hoardings in the street make our environment colorful.
# And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next program in the mini-drama. 
# Advertising can educate, too. 
# Adverts tell us about new, healthy products. 
# And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful.
#  Without advertising, life is boring and colorless.
# But some consumers argue that advertising is a bad thing. 
# They say that advertising is bad for children. 
# Adverts make children ‘pester’ their parents buy things for them. 
# Advertisers know we love our children and want to give them everything.
#  So they use children’s ‘pester power’ to sell their products. 
# Finally, consumers say, if there is advertising there must be rules. 
# Some adverts advertise unhealthy things like cigarettes and make people waste their money."""

# count_s = 0
# count_t = 0
# for letter in dan_text.lower():
#     if letter == 's':
#         count_s += 1
#     elif letter == 't':
#         count_t += 1
# print(f't:{count_s}, t:{count_t}')
  
# text = dan_text.replace('advert', 'ADVERT')
# print(text)
 

# 3
# import random
# students = [
#     {'name': 'John', 'age': 15, 'course': 'python', 'gender': 'Male'},
#     {'name': 'Andrew', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
#     {'name': 'Marcus', 'age': 25, 'course': 'java', 'gender': 'Male'},
#     {'name': 'Agness', 'age': 40, 'course': 'python', 'gender': 'Female'},
#     {'name': 'Don', 'age': 42, 'course': 'java', 'gender': 'Male'},
#     {'name': 'Michael', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
#     {'name': 'Jennifer', 'age': 16, 'course': 'java', 'gender': 'Female'},
#     {'name': 'Angela', 'age': 16, 'course': 'python', 'gender': 'Female'},
#     {'name': 'Eniston', 'age': 34, 'course': 'java', 'gender': 'Male'},
#     {'name': 'Albert', 'age': 33, 'course': 'javascript', 'gender': 'Male'},
#     {'name': 'Nash', 'age': 28, 'course': 'python', 'gender': 'Male'},
#     {'name': 'Nicolas', 'age': 19, 'course': 'java', 'gender': 'Male'},
#     {'name': 'Alexey', 'age': 21, 'course': 'java', 'gender': 'Male'},
#     {'name': 'Martin', 'age': 22, 'course': 'python', 'gender': 'Male'},
#     {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'},
#     {'name': 'Mikel', 'age': 24, 'course': 'python', 'gender': 'Male'},
#     {'name': 'Susanne', 'age': 25, 'course': 'javascript', 'gender': 'Female'},
#     {'name': 'Stevie', 'age': 26, 'course': 'python', 'gender': 'Male'},
#     {'name': 'Mark', 'age': 18, 'course': 'java', 'gender': 'Male'},
#     {'name': 'Johnathan', 'age': 15, 'course': 'python', 'gender': 'Male'},
#     {'name': 'Aidin', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
#     {'name': 'Mirbek', 'age': 25, 'course': 'java', 'gender': 'Male'},
#     {'name': 'Aidana', 'age': 40, 'course': 'python', 'gender': 'Female'},
#     {'name': 'Atay', 'age': 42, 'course': 'java', 'gender': 'Male'},
#     {'name': 'Chyngyz', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
#     {'name': 'Aigerim', 'age': 16, 'course': 'java', 'gender': 'Female'},
#     {'name': 'Jyldyz', 'age': 16, 'course': 'python', 'gender': 'Female'},
#     {'name': 'Emir', 'age': 34, 'course': 'java', 'gender': 'Male'},
#     {'name': 'Emirlan', 'age': 12, 'course': 'javascript', 'gender': 'Male'},
#     {'name': 'Nursultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
#     {'name': 'Aliaskar', 'age': 19, 'course': 'java', 'gender': 'Male'},
#     {'name': 'Aktanbek', 'age': 21, 'course': 'java', 'gender': 'Male'},
#     {'name': 'Adyl', 'age': 14, 'course': 'python', 'gender': 'Male'},
#     {'name': 'Janyl', 'age': 16, 'course': 'python', 'gender': 'Female'},
#     {'name': 'Meerim', 'age': 12, 'course': 'javascript', 'gender': 'Female'},
#     {'name': 'Sultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
# ]
# # 1
# diction = {'python':[], 'java':[], 'javascript': []}
# for i in students:
#    if i['course'] in diction:
#        diction[i['course']].append(i['name'])

# # print(diction)

# # 2
# dic = {x['name']: x['age'] for x in students}
# # print(dic)

# # 3
# names = ['Janyl', 'Nursultan', 'Meerim', 'Emir', 'Susann', 'Marcus', 'Aidin', 
# 'Aigerim', 'Angela', 'Albert', 'Jyldyz', 'Doe', 'Gloria', 'Aliaskar',
#  'Martin', 'John', 'Andrew', 'Steve', 'Johnathan', 'Adyl', 'Chyngyz', 
# 'Michael', 'Atay', 'Mikkel', 'Agnes', 'Aidana', 'Sultan', 'Nash',
#  'Nicolas', 'Mirbek', 'Aktan', 'Emirlan', 'Jennifer', 'Eniston', 'Alex', 'Mark']

 
# def func(lst, dict):
#     for i in lst:
#         try:
#             print(i, '-', dict[i])
#         except KeyError:
#             print('Do not have such name', i)
#             continue

# func(names, dic)


# 2.13 part 2


# class Employee:

#     def __init__(self, id, name, hours):
#         self.id = id
#         self.name = name
#         self.hours = hours
        
#     def count_payment(self):
#         pass

# class Fixed_salary(Employee):
#     def __init__(self, id, name, hours, amount_of_salary):
#         super().__init__(id, name, hours)
#         self.amount_of_salary = amount_of_salary
    
#     def count_payment(self):
#         return self.amount_of_salary


# class Comission(Employee):
#     def __init__(self, id, name, hours, amount_of_salary, amount_of_sales):
#         super().__init__(id, name, hours)
#         self.amount_of_salary = amount_of_salary
#         self.amount_of_sales = amount_of_sales

#     def count_payment(self):
#         return self.amount_of_salary + self.amount_of_sales * 50

    
# class Hourly_Paid(Employee):

#     def __init__(self, id, name, amount_of_salary, hours):
#         super().__init__(id, name, hours)
#         self.amount_of_salary = amount_of_salary
   
#     def count_payment(self):
#         return self.hours * 100


# def calculate_all_salaries(employees):
#     total_sum = 0
#     for employee in employees:
#         salary = employee.count_payment()
#         print('ID-', employee.id, 'NAME:', employee.name, 'SALARY:',employee.amount_of_salary)
#         total_sum += salary

#     print('Sum that spent to workers', total_sum)

# def productive_w(list_of_productivity, list_of_names):
#     most_productivity, most_productive_person = 0, None
#     least_productivity, least_productive_person = 100, None
#     for i in range(len(list_of_productivity) - 1):
#         if list_of_productivity[i] > most_productivity:
#             most_productivity, most_productive_person = list_of_productivity[i], \
#                 list_of_names[i]
#         if list_of_productivity[i] < least_productivity:
#             least_productivity, least_productive_person = list_of_productivity[i], \
#                 list_of_names[i]

#     print(f'Most productive {most_productive_person} his productivity {most_productivity}')
#     print(f'Least productive {least_productive_person} his productivity {least_productivity}')


# def calculate_productivity(employees):
#     hours_in_week = 40
#     list_of_productivity = []
#     list_of_names = []
#     for employee in employees:
#         productivity = employee.hours / hours_in_week * 100
#         print(employee.name, productivity)
#         list_of_productivity.append(productivity)
#         list_of_names.append(employee.name)
#     productive_w(list_of_productivity, list_of_names)

# manager = Fixed_salary(id=1, name='Jake', amount_of_salary=50000, hours=16)
# secretary = Fixed_salary(id=2, name='Lili', amount_of_salary=60000, hours=20)
# saler = Comission(id=3, name='Rose', amount_of_salary=40000, amount_of_sales=25, hours = 10)
# worker = Hourly_Paid(id=4, name='Dora', amount_of_salary=45000, hours = 12)
# secretary_for_change = Hourly_Paid(id=5, name='Dim', amount_of_salary=43000, hours = 10)

# list_of_workers = [manager, secretary, saler, worker, secretary_for_change]
# calculate_all_salaries(list_of_workers)
# calculate_productivity(list_of_workers)




# a = []
# for i in range(8):
#     b = []
#     for j in range(8):
#         b.append(j)
#         a.append(b)

# print(a)
# a = [[x for x in range(8)]  for i in range(8)]
# print(a)
# def dunc(a, b):
#     return a + b
# def dunc(a, b, v):
#     return a + b + v
# def func(*args):
#     return sum(args)

# print(func(1, 2, 3, 4, 5, 56))
# import pyperclip
# pyperclip.copy('Hi, my name is Aigerim')
# # pyperclip.paste()
# profile= {'name': 'Aigerim', 
#      'age': 17, 
#      'balance': 1000
#      }
     
# journal = {
#   'profile1': profile,
# }
# def current_balance(name,age,balance,journal):
#     profile3 = {}
#     profile1['name'] = name
#     profile1['age'] = age
#     profile1['balance'] = balance
#     journal['profile1'] = profile1
#     return journal

# def spendings(profile, job1, job2, *args):
#     lst = []
#     for i in args:
#         lst.append(i)
#     return [job1, job2], lst

# add_profile('john', 23, 1000, 5445)
# calculate_spending(*profile['spending'])
# calculate_spending(*profile['spending'])


# def decor(func):
#     def wrapper(*args):
#         for i in args:
#             if not isinstance(i, int):
#                 raise TypeError('it should be int')
#             else:
#                 pass
#         return func(*args)
#     return wrapper 

# @decor
# def sum_of_args(*args):
#     return sum(args)


# print(sum_of_args(32, 4546, 658))
# print(sum_of_args('sfeg', [23, 4545, 5, 6], 658))

from datetime import datetime
TREES_NUMBER = 100000

def getEfficiency(fruit):
    def outer(method):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            loot = method(*args, **kwargs)
            print(f'Robot spent {datetime.now() - start} time collecting {fruit}.')
            return loot
        return wrapper
    return outer
# class Robot:
#     def __init__(self, name):
#         self.name = name

#     @dec
#     def collectApples(self):
#         loot = [x for x in range(TREES_NUMBER) if x % 3 != 0]
#         return loot

  

# r = Robot('Rp')
# r.collectApples()

def checkIfArgumentsAreIntegers(function):
    def wrapper(*args, **kwargs):
        # args = [self, num1, num2]
        if not isinstance(args[1], int) or not isinstance(args[2], int):
            print("This is not correct question! Give Lootie 2 integers!")
            #raise TypeError('Arguments must be integers.')
        else:
            return function(*args, **kwargs)
    return wrapper  

def check_division_by_Zero(function):
    def wrapper(*args):
        num2 = args[2]
        if num2 == 0:
            raise TypeError('The second number shouldn\'t be zero')
        return function(*args)
        # else:
        #     return function(*args)
    return wrapper

class Robot:
    def __init__(self, name):
        self.name = name

    @getEfficiency('apples')
    def collectApples(self):
        loot = [x for x in range(TREES_NUMBER) if x % 3 != 0]
        return loot
    @getEfficiency('grapes')
    def collectGrapes(self):
        loot = [x for x in range(TREES_NUMBER) if x % 12 != 0]
        return loot
    @getEfficiency('bananas')
    def collectOranges(self):
        loot = [x for x in range(TREES_NUMBER) if x % 6 != 0]
        return loot
    
    @checkIfArgumentsAreIntegers
    def add(self, num1, num2):
        return num1 + num2

    @checkIfArgumentsAreIntegers
    def subtract(self, num1, num2):
        return num1 - num2

    @check_division_by_Zero
    @checkIfArgumentsAreIntegers
    def divide(self, num1, num2):
        return num1 / num2

    @checkIfArgumentsAreIntegers
    def multiply(self, num1, num2):
        return num1 * num2

lootie = Robot('Lootie')
print(lootie.add(1, 5))
print(lootie.subtract(5, 3))
print(lootie.divide(4, 0))
print(lootie.multiply("Lootie", "the Robot"))


collectedApples = lootie.collectApples()
collectedGrapes = lootie.collectGrapes()
collectedOranges = lootie.collectOranges()
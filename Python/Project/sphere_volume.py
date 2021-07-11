
# import math
# pi = math.pi


# def calculate_sphere_volume(r):
#     if type(r) in [int, float]:
#         if r < 0:
#             return 'Radius of sphere can be negative'
#         else:
#             return 4/3*pi*r**3
#     else:
#         raise ValueError

# class Area:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.value = self.width * self.height

#     def __add__(self, other):
#         return self.value + other.value

#     def __reduce__(self, other):
#         return self.value - other.value

#     def __eq__(self, other):
#         return self.value == other.value
    
#     def __gt__(self, other):
#         return self.value == other.value

#     def __ne__(self, other):
#         return self.value != other.value

#     def __ge__(self, other):
#         return self.value >= other.value 

# class Rectangle:
#     def __init__(self, width, height, color):
#         self.color = color
#         self.area = Area(width, height)
#         self.value = self.area.width * self.area.height

#     def __add__(self, other):
#         return self.area.value + other.area.value

#     def __reduce__(self, other):
#         return self.area.value - other.area.value

#     def __eq__(self, other):
#         return  self.area.value == other.area.value

#     def __gt__(self, other):
#         return self.area.value > other.area.value

#     def __ne__(self, other):
#         return self.area.value != other.area.value

#     def __ge__(self, other):
#         return self.area.value >= other.area.value



# a = Area(3, 4)
# r = Rectangle(2, 5, 'red')
# print(a.__add__(r))
# print(a.__reduce__(r))
# print(a.__eq__(r))
# print(a.__gt__(r))
# print(a.__ne__(r))
# print(a.__ge__(r))


# class CharField:

#     def __init__(self, value, max_length):
#         self.value = value
#         self.max_length = max_length
       
# class Author:
#     def __init__(self, user, age):
#         self.user = user
#         self.age = age

# class Post:
#     def __init__(self, title, max_length, body, author):
#         self.title = CharField(value = title, max_length = 30)
#         self.body = CharField(value = body, max_length = 100)
#         self.author = author
#     def __str__(self):
#         return f'Author: {self.author.name}', f'Title: {self.title.title}', f'Body: {self.body.body}'


# us = Author(user = 'Katya', age = 18)
# p = Post(title = 'it is Title', body = 'It is body of the post', author = us)
# p.author.name
# print(p)



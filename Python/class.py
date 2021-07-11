# class Les:
#     width = 50

#     def __init__(self, length, height):
#         self.length =  length
#         self.height = height
#         print(self.length, self.height)

#     def show_length(self):
#         print(f'my length is {self.length}')


# l = Les(50, 40)
# s = Les(100, 60)
# print(l.width)
# print(s.width)

# l.show_length()
# s.show_length()

# Создаем класс Plane
# class Plane:

  
  
#     name = "c800"
#     make = "tezJet"
#     model = 2004
#     surname = "C500"
#     made = "OS"
#     modem = 2006

#     # создаем методы класса

#     def __init__(self, value, key):
#         self.value = value
#         self.key = key



#     def start(self):
#         print ("Подготавливаемся к полету")
#         print(self.value + self.key)
    
#     def stop(self):
#         print ("Взлетаем")


    
        



# plane_a = Plane(309, 56)
# print(plane_a.name)
# print(plane_a.make)
# print(plane_a.model)

# plane_a.start()
# plane_a.stop()
# plane_a.start()

# plane_b = Plane(45, 98)
# print(plane_b.surname)
# print(plane_b.made)
# print(plane_b.modem)
# plane_b.start()

# class hello:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return 'Aika'

#     def __add__(self, other):
#        return self.age - other

    
# h = hello('Aigerim', 17)
# print(h)
# print(h + 12)

class Human:
    def __init__(self, name):
        self.name = name

    def __call__(self, o):
        self.name = o
        return self.name

class People:
    def __init__(self, *human):
        for humans in human:
            print(humans.name)

h1 = Human('sugf')
h1('ysrgf')  #h1.name = 'ysrgf
h = People(h1)
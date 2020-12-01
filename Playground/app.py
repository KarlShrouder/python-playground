# ------(Exceptions)-----------------
# try:
#     age= int(input("Age: "))
#     income = 20000
#     risk = income / age
#     print(age)
# except ValueError:
#     print("Invalid Value")
# except ZeroDivisionError:
#     print("Age cannot be zero")

# --------(Classes)------------------
# class Point:
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# point1 = Point()
# point1.x = 20
# point1.y = 30
# print(f"({point1.x}, {point1.y})")
# point1.draw()
# point1.move()

# ---------(Classes)-----------------------
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
# point = Point(122, 12)
# print(point.x)
# print(point.y)

# --------(Classes Practice)-----------------
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f"{self.name}: Blah")
#
#
# person = Person("Karl")
# person.talk()

# --------(Inheritance)----------------------
# class Mammal:
#     def __init__(self, name):
#         self.name = name
#
#     def walk(self):
#         print(f"*{self.name} is walking*")
#
#
# class Dog(Mammal):
#     def bark(self):
#         print(f"{self.name}: woof!")
#
#
# class Cat(Mammal):
#     def meow(self):
#         print(f"{self.name}: meow!")
#
#
# dogo = Dog("Rokki")
# dogo.walk()
# dogo.bark()
#
# kitty = Cat("Diamond")
# kitty.walk()
# kitty.meow()

# ------------(Modules)--------------------
# import converters
# from converters import kg_to_lbs
#
# kg_to_lbs(150)
#
# print(converters.kg_to_lbs(70))

# -------------(Modules Exercise)-------------------



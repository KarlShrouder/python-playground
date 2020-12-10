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

# ------------(Modules)--------------
# import converters
# from converters import kg_to_lbs
#
# kg_to_lbs(150)
#
# print(converters.kg_to_lbs(70))

# -------------(Modules Exercise)--------
# from utils import find_max
#
# numbers = [12, 14, 11, 3, 7, 54, 65]
# maximum = find_max(numbers)
# print(maximum)

# ------------(Packages)------------------------
# from ecommerce.shipping import cal_shipping
# cal_shipping()

# --------(Generating Rand Values)-----
# import random
#
# for i in range(3):
#     print(random.randint(10, 20))
#
# members = ["Karl", "Dom", "Maggie"]
# leader = random.choice(members)
# print(leader)

# ----(Generating Rand Values Ex.)-----
# import random
#
#
# class Dice:
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def roll():
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second
#
#
# dice = Dice()
# print(dice.roll())

# ---(Files and Directories)-----
# from pathlib import Path
#
# # Absolute Path
# # c:\Program Files\Microsoft
# # /usr/local/bin
#
# # Relative Path
# # from the working directory
#
# path = Path("ecommerce")
# print(path.exists())
#
# path = Path()
# for file in path.glob("*"):
#     print(file)

# --------------(Excel Automation)---------------------
# import openpyxl as xl
# from openpyxl.chart import BarChart, Reference
#
#
# def process_workbook(filename):
#     wb = xl.load_workbook(filename)
#     sheet = wb['Sheet1']
#
#     for row in range(2, sheet.max_row + 1):
#         cell = sheet.cell(row, 3)
#         corrected_price = cell.value * 0.9
#         corrected_price_cell = sheet.cell(row, 4)
#         corrected_price_cell.value = corrected_price
#
#     values = Reference(sheet,
#                        min_row=2,
#                        max_row=sheet.max_row,
#                        min_col=4,
#                        max_col=4)
#
#     chart = BarChart()
#     chart.add_data(values)
#     sheet.add_chart(chart, 'e2')
#
#     wb.save(filename)
#
#
# process_workbook('transactions.xlsx')

# -----------------(Machine Learning)-------------------------------
# 1. Import Data
# 2. Clean Data
# 3. Split the Data into Training/Test Sets (80/20)
# 4. Create a Model (or find one)
# 5. Train the Model
# 6. Make Predictions
# 7. Evaluate and Improve
#
# Libraries
#   * Numpy
#   * Pandas
#   * MatPlotLib
#   * Scikit-Learn

# ----------------------(Pygame Tutorial)----------------------------
import pygame

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Game loop
running = True
while running:

    # Screen RGB
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
            if event.key == pygame.K_UP:
                playerY_change = -0.1
            if event.key == pygame.K_DOWN:
                playerY_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)
    pygame.display.update()

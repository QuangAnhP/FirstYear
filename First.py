
'''
Working with strings:
'''
import random

phrase = "Niceee"
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("e"))
print(phrase.replace("Nice", "-"))

# Working with numbers:

print()
from math import *

my_num = -10
print(str(abs(my_num)) + " is the number")
print(max(pow(2, 4), min(3, 4, round(2.4))))
print(sqrt(4))

# Input:

    # print()
    # name  = input("Enter name: ")
    # age  = input("Enter age: ")
    # print("Hi " + name + "! You are " + age )

    # num1 = input("Enter a number: ")
    # num2 = input("Enter another number: ")
    # result = float(num1) + float(num2)
    # print()
    # print(result)

# Lists:

print()
fruits = ["apple", "banana", "coconut", "watermelon"]
num = [1, 4, 10, 8, 74, 64, 22]

fruits[-1] = "strawberry"
print(fruits[1:3])

num.sort()
num.extend(fruits)
num.append("grape")
num.insert(2, "?")
print(num)
print(num.index(10))

num2 = num.copy()

# Tuples:

print()
cords = ([1, 2], [3, 5], [6, 10])
print(cords[2])

# Functions:
print()

def num():
    print(random.randrange(1, 99))

    # num()


def pick_num(bottom, top):
    return random.randrange(bottom, top)

print(pick_num(1, 100))

# Dictionaries:
abbrev = {
    "exp" : "experience",
    "hp" : "Health Points",
    "pot" : "Health Potions",
}

print()

print(abbrev.get("exp", "Invalid"))

# 2D Lists:
print()
numbers = [
    [1, 2, 3], # row 0, column 0, 1, 2
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(numbers[1][2])

# Try / Except: 

# Try: 
# value = 10 / 0
# print(int(input("Enter a number: ")))
# except ZeroDivisionError as "error":
# print("error")
# except ValueError:
# print("Invalid Input")


# Reading files from somewhere else:

    # variable = open("file name", "r") #r for read, w for (over)write, r+ for both, a for appending

    # print(variable.readable()) #check for readability
    # print(variable.read()) #read the entire file
    # print(variable.readline()) #read first line and move to next
    # print(variable.readlines()) #read the entire file, put into a list
    # print(variable.readlines()[0]) #read first line

    # variable.close()


# Class / Objects:

from main import Student

student1 = Student("Brian", "Math", 3.4, True)
student2 = Student("Jack", "CMPT", 3.7, False)

print(student1.name)
print(student2.eligible())

# Lambda Function:

def myfunc(n):
  return lambda a: a * n  # lambda arguments : expression

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# Iterators: 

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a < 5:
        x = self.a
        self.a += 1
        return x
    else:
        raise StopIteration



myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

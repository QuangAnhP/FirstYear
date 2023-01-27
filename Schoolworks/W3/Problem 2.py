print("\033c")

from random import randint




inputs = []
n = randint(5, 8)

inputs = [float(input("Enter the floats you wish to compare here: ")) for i in range(n)]


max = max(inputs)
min = min(inputs)
print("The largest value is: ", max)
print("The smallest value is: ", min)
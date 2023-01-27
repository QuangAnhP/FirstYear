
# %%
from functools import reduce

n = int(input("Please input the number of integers you would like to enter: "))
'''
For Problem 4:

from random import randint
n = randint(-5, 5)

'''
inputs = []
evens = []
odds = []

def average(list):
    return reduce(lambda a, b: a + b, list) / len(list)

inputs = [int(input("Enter the integers you wish to use here: ")) for i in range(n)]

for i in inputs:
    if i <= 0:
        inputs.remove(i)
    else:
        if i % 2 == 0:
            evens.append(i) 
        if i % 2 != 0:
            odds.append(i)

# %%
even_sum = sum(evens)
even_ave = average(evens)
odds_sum = sum(odds)
odds_ave = average(odds)
all_sum = sum(inputs)
all_ave = average(inputs)

print("The sum of even values is: ", even_sum)
print("The average of even values is: ", even_ave)
print("The sum of odds values is: ", odds_sum)
print("The average of odds values is: ", odds_ave)
print("The sum of all values is: ", all_sum)
print("The average of all values is: ", all_ave)
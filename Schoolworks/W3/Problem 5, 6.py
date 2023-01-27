
# %%
n = int(input("Please input the number of integers you would like to enter: "))
inputs = []
evens = []
odds = []

for i in inputs:
    if i <= 0:
        inputs.remove(i)
    else:
        if i % 2 == 0:
            evens.append(i)
        if i % 2 != 0:
            odds.append(i)

# %%
even_min = min(evens)
even_max = max(evens)
odd_min = min(odds)
odd_max = max(odds)

print("The minimum even value is: ", even_min)
print("The maximum even values is: ", even_max)
print("The minimum odds values is: ", odd_min)
print("The maximum odds values is: ", odd_max)

# %% Strip the given value of all "1" and return an integer

x = input()
result = ""
for i in x:
    if i != "1":
        result += i

if result == "":
    print("0")
else: 
    print(int(result))


# %%
inputs = int(input())
indiv = ""
result = 0
pos = 1

while inputs != 0:
    indiv = inputs % 10
    if indiv != 1:
        result += indiv * pos
        pos *= 10
    inputs //= 10

if result == "":
    print("0")
else:
    print(result)
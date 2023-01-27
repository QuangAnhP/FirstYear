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

print(result)

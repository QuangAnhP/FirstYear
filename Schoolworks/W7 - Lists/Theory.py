# %% Introduction

alist = [1, "2", -3, 10]

print(type(alist))

print(alist[1])

print(len(alist))

print(alist[1:3])

# %% Concatenate + append lists 

list1 = [1, 2, 3]
list2 = [10, 100, -2]
print(list1 + list2)

list1.append(100)

# %% Lists are not immutable:

list1 = [1, 2, 3]
list1[1] = 100
print(list1)

# %% Modifying indices 

from random import randint
alist = [1, 2, 3, 4, 5]
alist = [i * 2 for i in alist]
print(alist)

alist = []
count = 0
while count < 10:
    alist.append(randint(1,10))
    count += 1

print(alist)
maxValue = max(alist)
print(f"The maximum of the values is {maxValue}.")

for i in range(1, len(alist)):
    if alist[i] > maxValue:
        maxValue = alist[i]
print(maxValue)

# %% Reversing list

alist = [2, 10, 5, 9, 12, 101]

for i in range(len(alist) // 2):
    temp = alist[i]
    alist[i] = alist[len(alist) - 1 - i]
    alist[len(alist) - 1 - i] = temp
print(alist)
    # .reverse()

# %% Practice 1:

def cumulativeSum(alist):
    sum = 0
    for i in alist:
        sum += i
    return sum  

cumulativeSum([1, 2, 3, 100])

    # sum()

# %% Practice 2:

def hasDupe(alist):
    for i in alist:
        if alist.count(i) > 1:
            return True
    return False

'''

Alt1:
blist = set(alist)
if len(blist) == (alist): False ...

Alt2:
for i in range(len(alist)):
    for j in range(i+1, len(alist)):
        if alist[i] == alist[j]:
            return True
    return False

'''

# %% Practice 3:

def getPivot(alist):
    for i in range(len(alist)):
        if cumulativeSum(alist[0:i]) == cumulativeSum(alist[i+1: ]):
            return i
    return -1

'''
( cumulativeSum() = sum() )
Alt: 
def ...
    all = sum(alist)
    left = 0
    for i in range(len(alist)):
        if left  == all - left - alist[i]:
            return i
        left += alist[i]
    return -1

'''
# %% Methods of removing indices:

alist = [7, 8, 3, 1, 10, 21]

    # del list[index]

del alist[0]

    # .remove(first instance of x)

alist.remove(21)

    # .pop(index)       (return popped value)

alist.pop(2) 

# %% Practice:

alist = [7, 2, 4, 5, 11, 6]
for i in range(len(alist)-1 , -1, -1):
    if alist[i] % 2 == 0:
        del alist[i]

print(alist)

# %% Alias

a = [8, 5, 2]
b = a
a[1] = 1000
print(a, b)         # => a and b are aliases

print()

a = [8, 5, 2]
b = a.copy()        # same as b = a[:]
a[1] = 1000
print(a, b)

# %% Nested lists:

alist = [[3, 9, 2], ["Hello", 20], [3, 14, 2, 4], 10]

print(alist[1][0])

# %% Practice 1: a 2 by 3 list filled with 1

alist = []
for i in range(3):
    alist.append([])
    for j in range(3):
        alist[i].append(1)
print(alist)

# %% Practice 2:

alist = []
for i in range(4):
    alist.append([])
    for j in range(4):
        alist[i].append(randint(1,5))


sum = 0
for i in range(len(alist)):
    sum += alist[i][i]
print(sum)

# %% Practice 3:


def printList(alist):
    for i in range(len(alist)):
        for j in range(len(alist[0])):
            print(alist[i][j], end = "\t")
        print()

printList([[1, 2, 3], [10, 20, 30]])

# %% Transpose(mxn -> nxm):

def Transpose(alist):
    t = []
    for i in range(len(alist[0])):
        t.append([])
        
        for j in range(len(alist)):
            t[i].append(alist[j][i])
    
    printList(t)

Transpose([[3, 2, 3, 1], [5, 1, 2, 5]])
# %%

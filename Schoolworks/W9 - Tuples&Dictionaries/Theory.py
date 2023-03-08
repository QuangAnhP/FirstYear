# %% Intro: Tuples

atuple = (10, 21, 31, 87, 65)


print(type(atuple))

print(atuple[1])

print(len(atuple))
    # Immutable -> change to list if edits needed:
alist = list(atuple)
print(alist)
atuple = tuple(alist)
print(atuple)

    # Slicing:
print(atuple[2:4])

# %% Editing Tuples:
    
    # Concatenate:
tup1 = (1, 2, 3)
tup2 = (10, 11, 12)
tup3 = tup1 + tup2
print(tup3)

mytup = (10, 21, 31, 101, 201, 301, 12 ,81)
mytup = mytup + (41,)
print(mytup)

    # Remove elements:
mytup = mytup[:4] + mytup[5:]
print(mytup)

    # Loops:
for i in range(len(mytup)):
    print(mytup[i])

print()

for i in mytup:
    print(i)
    
    # Packing and Unpacking:
mytup = (10, 20, 100)
(a, b, c) = mytup
print(a, b, c)

# %% Practice:

alist = [1, 2, 3, 4, 5, 6]
for i in range(len(alist) - 1):
    alist[i], alist[i+1] = alist[i+1], alist[i]
    print(alist)


# %% Intro: Dictionary

inven = {
    "apple": 23,
    "banana": 17,
    "coconut": 0, 
}
print(type(inven))
print(inven["apple"])
print(len(inven))

    # Change existing value:
inven["apple"] = 32

    # Add key-value:
inven["pears"] = 19

    # Remove key-value:
del inven["apple"]

# %% Practice

alist = [2, 4, 5, 10, 21, 31, 40]
def myFunction(alist):
    
    # Creating the dictionary:
    adict = {
        "even": 0,
        "odd": 0,            
    }
    
    # Looping through the list and count odd/ even:
    for i in alist:
        if i % 2 == 0:
            adict["even"] += 1
        else:
            adict["odd"] += 1
    return adict

myFunction(alist)

# %% Practice 2: Show the value of odd/ even instead of the counts

alist = [2, 4, 5, 10, 21, 31, 40]
def ListToDict(alist):
    
    d = {
        "odd": [],
        "even": []
    }

    for i in alist:
        if i % 2 == 0:
            d["even"].append(i)
        else:
            d["odd"].append(i)
    return d

ListToDict(alist)

# %% Accessing/ Looping through dictionaries

d = {
    "apple": 23,
    "orange": 100,
    "banana": 247,
}
    
    # dict.keys(): get all keys
for k in d.keys():
    print(k)

    # dict.values(): get all values
for k in d.values():
    print(k)    

    # dict.items(): get both in a list containing tuples
for k in d.items():
    print(k)

# %% Practice:

def freq(s):
    
    # Dictionary comprehension:
    d = {chr(i):0 for i in range(97, 123)}
    
    # Loop throught the string and add in the right place:
    for i in s:
        if "a" <= i <= "z":
            d[i] += 1

    return d
freq("aaaAABBCdc")

# %% Aliasing

d = {
    "apples": 10,
    "banana": 31
}

d_copy = d.copy()
d_copy["banana"] = 1

test = d
test["apples"] = 100

print(d)
print(d_copy)
print(test)

# %% Practice

from math import sqrt
def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


    # Creating the dictionary:
d = {i: "not Prime" for i in range(2, 21)}
    
    # Alt:
d = {}
for n in range(2, 21):
    if isPrime(n):
        d[n] = "prime"
    else:
        d[n] = "not Prime"

    # Loop through the dictionary and change value if isPrime:
for i in d.keys():
    if isPrime(i) == True:
        d[i] = "Prime"

print(d)

# %% Swaping keys and values in the case above:

def swap(d):
    new_dict = {}
    for k in d:
        if d[k] not in new_dict:
            new_dict[d[k]] = [k]
        else:
            new_dict[d[k]].append(k)
    return new_dict

swap({
    "a": 10,
    "b": 10,
    "C": 11,
    "c": 13
})

swap(d)
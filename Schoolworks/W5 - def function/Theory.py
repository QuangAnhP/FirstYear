# %%
def SayHello(name):
    print("Hello", name)

name = input("Enter your name: ")
SayHello("John")

# %%
def myfunction(a):
    print("Hello", a)
    return 
print(myfunction("John"))

# %%
def minValue(a, b):
    if a < b:
        return a
    else:
        return b

print(minValue(3, 10))

# %% Factorial

def Factorial(n):
    if n == 0:
        return 1
    for i in range(1, n):
        n *= i
    return n

Factorial(5)

# %% Print prime numbers:

from math import sqrt

def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

count = 0
num = 2
while count < 5:
    if isPrime(num):
        print(num)
        count += 1
    num += 1

# %% Reverse + Palindrome


def reverse(n):
    rev = 0
    while n != 0:
        digit = n % 10
        rev = rev*10 + digit    # or use str(n)[::-1]
        n //= 10
    return rev

def palindrome(x):
    if x == reverse(x):
        return True
    else:
        return False
    
palindrome(int(input("Enter the number: ")))

# %% More on palindrome(196-algo):

def algo(n):
    if n == 196:
        return print("Please try again")
    while palindrome(n) == False:
        n += reverse(n)
    return n     

algo(int(input("Enter any number except 196: ")))

# %% Global/Local variable
def myFunction(a): 
    a = 20         # "a" here is a parameter (local)
    print(a)

a = 10             # "a" here is a different variable (global)
myFunction(a)
print(a)

# %% Function + Nested loop (Pascal Triangle): 

def factorial(n):
    if n ==0:
        return 1
    for i in range(1, n):
        n *= i
    return n

n = int(input("Enter the height of the Pascal Triangle: "))

for i in range(n):
    
    # This loop for putting in white space: 
    for j in range(n - i):
        print("", end = "*")

    # This loop for putting in the number:
    for k in range(i+1):                                                                                                                                                                    
        print(factorial(i) // (factorial(i-k)*(factorial(k))), end = "*")
        # Can put the above in another function( ex. Combination(n, r))
    
    print()

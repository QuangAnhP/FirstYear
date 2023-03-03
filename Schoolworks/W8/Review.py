# %% "x+b=c"

def solve(s):
    count = 0
    for i in range(len(s)):
        if s[i] == "=" :
            return int(s[i+1:]) - int(s[2:i])


x = input("Enter a function in the form of x+b=c")
print(solve(x))

# %% Rotate 

def rotate(alist):
    alist.insert( 0, alist[len(alist) - 1])
    alist.pop()
    return alist

alist = [1, 2, 3, 4, 5]
rotate(alist)
print(alist)

# %% format int

def formatInt(n):
    str_of_n = str(n)
    count = 0
    for i in range(len(str_of_n), 0, -1):
        if count == 3:
            str_of_n = str_of_n[:i] + "," + str_of_n[i:]
            count = 0
        count += 1
    return str_of_n


n = int(input("Enter a number: "))
print(formatInt(n))


# %% frequency

def freq(s):
    alist = [0 for i in range(26)]
    for i in s:
       alist[ord(i) - 97] += 1
    return (alist)

s = input("Enter string: ")
print(freq(s))
# %% Intro

message = 'Hello World'

print(message[0])

print(len(message))
print()
    
    # Can also iterate directly to string:
for i in message:
    print(i)

# %% Reversing a string
    
for i in range(len(message) - 1, -1, -1):
    print(message[i])

# %% Slicing strings (start:end:steps)

print(message[4:9])

print(message[20:42])

test = message[20:42]
print(len(test), type(test))  # empty string

# %% Editing index:

new_message = message[0:5] + 'T' + message[7:11]
print(new_message)

# %% Palindrome:

def isPalindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[(len(string) - 1 - i)]:
            return False
    return True

isPalindrome(input("Enter a string: "))

# %% search in string:

def isFound(s, c):
    for i in range(len(s)):
        if c == s[i]:
            return True
    return False

isFound('abcdefgh', 'c')

    # Expand: 
    # if c in s: ...
    # find(): find the location

# %% Remove duplicates:

def removeDupe(string):
    new_string = ''
    for i in range(len(string)):
        if isFound(new_string, string[i]) is False:
            new_string = new_string + string[i]
    return new_string

removeDupe("aadabaadbdca")

# %% Excercise: Replace

def replaceStr(s, old, new):
    result = ''
    i = 0
    while i < (len(s)):
        
        if s[i] == old[0]:
            temp = s[i : i+len(old)]
        
            if temp == old:
                result += new
                i += len(old)    
        
        else:
            result += s[i]
            i += 1
    return result


replaceStr("To be or not to be", "be", "?")

# %% Comparing strings using ASCII:

'''
Dictionary order: 
ex. "abc" and "abd"
Compare a with a, then b with b, then c with d -> "abc" < "abd"

"a" < "A"
"abc" < "abcde"
"apple" > "ape"
"apple" < "Ape"
"Apple" > "ape"
'''

def isEqual(a, b):
    for i in range(max(len(a), len(b))):    # or check for different lenght outside
        if (len(a) != len(b)) or (a[i] != b[i]):
            return False
    return True

isEqual("abcde", "abcde")
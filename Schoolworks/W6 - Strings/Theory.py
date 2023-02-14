# %% Intro

message = 'Hello World'

print(message[0])

print(len(message))

# %% Reverse
    
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

# %% 
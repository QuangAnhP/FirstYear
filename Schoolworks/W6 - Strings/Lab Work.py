# %% Problem 1: 120

# %% Problem 2:

def findChar(s, c):
    for i in range(len(s)):
        if s[i] == c:
            return i
    else: return -1

findChar("abcdefg", "z")

    # basically find() but only for 1 character

# %% Problem 3:

def isUpperCase(s):
    for i in s:
        if i.islower() is True:
            return False
    return True

isUpperCase("ABCDe")


# %% Extra: make "upper()"

def makeUpper(s):
    new_s = ''
    for i in s:
        if 65 <= ord(i) <= 90 and 97 <= ord(i) <= 122:
            new_s += chr(ord(i) - 32)
        else:
            new_s += i
    return new_s

makeUpper("abcd123")

# %% Problem 4: 

def isUpperCaseOnly(s):
    for i in s:
        if (ord(i) < 65) or (ord(i) > 90):
            return False
    return True

isUpperCaseOnly("ABCD2")

# %% Problem 5/6: same format as above (48->57)

# %% Problem 7: 

def containsDisinctCharacters(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True

containsDisinctCharacters("ABCabcdee")

# %% Problem 8: !!!not done

def isContained(s1, s2):
    j = 0
    for i in s1:

        while s2[j] != i:
            j += 1
            
    return True

isContained("abcd", "abcde")
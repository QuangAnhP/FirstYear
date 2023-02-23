# %% Main Program
n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
ans = n1 + n2

# decimalToBinary:

def decimalToBinary(n):
    temp = []
    result = ''
    
    # Putting the remainder of (n % 2)1// into a list:
    while (n >= 1):
        r = int(n % 2)
        temp.append(r)
        print(temp)
        n = (n - r) / 2
    
    # Slicing the list backward to get the binary integer:
    for i in temp[::-1]:
        result += str(i)
    
    return result



# binaryAddition:

def binaryAddition(str1, str2):
    carry = 0
    result = ''
    
    # Find the longer string:
    max_len = max(len(str(str1)), len(str(str2)))
    
    # Add "0" into shorter string to be able to do addition:
    if len(str2) < max_len:
        str2 = "0" * (max_len - len(str2)) + str2
    if len(str1) < max_len:
        str1 = "0" * (max_len - len(str1)) + str1
    
    # Start calculation:
    for i in range(max_len - 1, -1, -1):
        temp = carry
        temp += 1 if str2[i] == '1' else 0
        temp += 1 if str1[i] == '1' else 0
        result = ('1' if temp % 2 == 1 else '0') + result
        carry = 1 if temp > 1 else 0
    
    # Add another "1" at the start if needed:
    return (result if carry == 0 else '1' + result)



# binaryToDecimal:

def binaryToDecimal(binStr):
    binary = int(binStr)
    result = 0
    pos = 0    
    while (binary != 0):
        
        # Access the last digit of binStr and add into Decimal:
        digit = binary % 10
        result +=  digit * (2 ** pos)
        
        # Remove last digit and raise pos (power of 2):
        binary //= 10
        pos += 1
    return result



str1 = decimalToBinary(n1)
print("The binary representation of", n1, "is", str1)

str2 = decimalToBinary(n2)
print("The binary representation of", n2, "is", str2)

str3 = binaryAddition(str1, str2)
print("The binary addition of", n1, "and", n2, "is", str3)

n3 = binaryToDecimal(str3)
print("Converting the binary to decimal gives", n3)


if ans == n3:
    print("Since", ans, "==", n3, ", it seems we did good job.")
else:
    print("Since", ans, "!=", n3, ", something went wrong.")


# %% Alts: Recursive functions(?)
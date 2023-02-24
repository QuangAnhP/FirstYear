# %% Change date format:

def format(date):
    
    dd, mm, yyyy = '', '', ''
    count = 0

    # Loop through the string and get dd, mm, yyyy:
    for i in date:
        if i == '-':
            count += 1
        elif count == 0:
            dd += i
        elif count == 1:
            mm += i
        else:
            yyyy += i

    # Put in the wanted format:
    return (yyyy+ " - " + dd + " - " + mm)


date = input('Enter the date  in the format dd-mm-yyyy: ')

print(format(date))

# %% Word count: (not done, need space after last word to work)

def countWords(message):
    count = 0
    i = 0
    result = 0
    while i < len(message):
        if message[i] != " ":
            count += 1
        if (message[i] == " ") and ((count != 0)):
            result += 1
            count = 0
        i +=  1
    return result

message = input("Enter the message: ")
print(countWords(message))
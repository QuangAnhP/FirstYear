print("\033c")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another number: "))
d = int(input("Enter another number: "))
e = int(input("Enter another number: "))
positive = []
negative = []
sum_pos = 0
sum_neg = 0
# Separate positive and negative numbers:
if a > 0:   
    positive.append(a)
elif a < 0:                         # can't use if cuz appending "0" will affect average
    negative.append(a)  

if b > 0:
    positive.append(b)
elif b < 0:
    negative.append(b)

if c > 0:
    positive.append(c)
elif c < 0:
    negative.append(c)

if d > 0:
    positive.append(d)
elif d < 0:
    negative.append(d)

if e > 0:
    positive.append(e)
elif e < 0:
    negative.append(e)

# Sum and average of Positives:
for i in positive:
    sum_pos += i

ave_pos = sum_pos / len(positive)

# Sum and average of Negative:
for i in negative:
    sum_neg  += i

ave_neg = sum_neg / len(negative)

# Sum and average of All:
sum_all = a + b + c + d + e
ave_all = sum_all / 5

# Print:
print("Sum of positives:", sum_pos)
print("Average of positives:", ave_pos)
print("Sum of negatives:", sum_neg)
print("Average of negatives:", ave_neg)
print("Sum of all:", sum_all)
print("Average of all:", ave_all)

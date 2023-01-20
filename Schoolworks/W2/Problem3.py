print("\033c")

hours = int(input("Enter the number of hours worked in a week: "))
dependents = int(input("Enter the number of dependents: "))
rate = 16.78
overtime = rate * 1.5

# Finding gross pay: 
if hours < 40:
    gross = hours * rate
else: 
    gross = (hours - 40)*overtime + 40*overtime

# Taxes:
SStax = gross  * 6/100
Fedtax = gross * 14/100
Statetax = gross * 5/100

net = gross - (SStax + Fedtax + Statetax + 10)

# Checking for extra health insurance:
if dependents >= 3:
    net -= 35

print("Gross pay:$", gross)
print("Social Security tax:$", SStax)
print("Federal income tax:$", Fedtax)
print("State income tax:$", Statetax)
print("Union dues: $10")
if dependents > 3:
    print("Extra healthcare insurance: $35")
else: 
    print("Extra healthcare insurance: $0")
print()
print("Net pay for the week:$", net)

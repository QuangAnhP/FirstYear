# %%

tax = 0

# Storing values of tax brackets and rates:
def calculate_tax(income):
    tax_brackets = {
        5.06: (0, 45654),
        7.70: (45654.01, 91310),
        10.50: (91310.01, 104835),
        12.29: (104835.01, 127299),
        14.70: (127299.01, 172602),
        16.80: (172602.01, 240716),
        20.50: (240716.01, float("inf"))
    }

    for bracket, (lower, upper) in tax_brackets.items():
        global tax
        rate = bracket / 100
        if income > upper:
            tax += (upper - lower) * rate
        else:
            tax += (income - lower) * rate
            break
    return round(tax, 2)

income = float(input("Enter your taxable income: "))
tax = calculate_tax(income)
final = income - tax
print(f"You owned ${tax} in tax.")
print(f"You will have ${final} after tax.")

# %%
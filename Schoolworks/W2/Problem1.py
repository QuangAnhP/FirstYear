print("\033c")

principalAmount = float(input("Enter your principal amount: "))
timePeriod = float(input("Enter your time period in years: "))
rate = 0

# function to calculate with different rate: 
def rate_calculate(rate):                       
    global totalAmount
    totalAmount = principalAmount * (1 + rate*timePeriod)
    return totalAmount

def calculate_total():
    # Check if given input is valid:
    if principalAmount < 0 or timePeriod < 0:                      
        return "Invalid Input"
    
    # Check the principalAmount:
    if principalAmount < 1000:                                      
        return rate_calculate(0.025)
    elif principalAmount < 10000:
        return rate_calculate(0.020)
    elif principalAmount < 100000:
        return rate_calculate(0.015)
    elif principalAmount >= 100000:
        return rate_calculate(0.010)

# Run the program:
calculate_total()
print(totalAmount)
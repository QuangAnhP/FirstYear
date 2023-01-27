print("\033c")








# Get the number of floats:
n = int(input("Please input the number of float you would like to enter: "))

# Creating a list to store all the float:
inputs = []

inputs = [float(input("Enter the floats you wish to compare here: ")) for i in range(n)]

# Finding the maximum and minimum value in the list:

max = max(inputs)
min = min(inputs)
print("The largest value is: ", max)
print("The smallest value is: ", min)
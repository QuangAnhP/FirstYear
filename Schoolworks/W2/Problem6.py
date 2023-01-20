# %%
from math import pi

s_cost = float(input("Enter the price of the smaller pizza: "))
s_dia = float(input("Enter the diameter of the smaller pizza: "))
l_cost = float(input("Enter the price of the bigger pizza: "))
l_dia = float(input("Enter the diameter of the bigger pizza: "))

# %%
s_area = 4*pi*s_dia / 3
l_area = 4*pi*l_dia / 3

s_ppi = s_cost / s_area
l_ppi = l_cost / l_area

if s_ppi > l_ppi:
    print("The smaller pizza is better")
elif s_ppi < l_ppi:
    print("The bigger pizza is better")
else:
    print("You can just get either")

# %%

# %% Bisection Method:

a = float(input("Enter the left-side value: "))
b = float(input("Enter the right-side value: "))

# %%
def f(x):
    return x**2 - 2

while abs(a - b) > 0.0000001:
    m = (a+b)/2
    if f(m) == 0.0:
        break
    if f(a) * f(m) < 0:
        b = m
    elif f(m) * f(b) < 0:
        a = m
    print(a, ' ,   ', m, ' ,   ',b)

# %%

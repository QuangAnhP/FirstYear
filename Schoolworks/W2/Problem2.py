'''
Program 2 is the faulty because it uses "if"s instead of "elif" 
This can be best explained using examples:

User input 50:
Program 1:
    skip through the first 3 conditionals -> 'D' -> print: Letter Grade = D
Program 2:
    skip through the first 3 conditionals -> 'D' -> print: Letter Grade = D

User input 100:
Program 1:
    get to the first if -> 'A' -> skip all the elif -> print: Letter Grade = A
Program 2:
    get to first if - > 'A' -> get to second if -> ... -> print: Letter Grade = D
'''

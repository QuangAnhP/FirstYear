# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# Used in Theory.py:

class Student:
    def __init__(self, name, major, gpa, is_in_class):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_in_class = is_in_class
    
    def eligible(self):
        if self.gpa >= 3.5:
            return True
        else:  
            return False 
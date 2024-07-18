"""
if (condition-1):
    if(condition-2):
        block of code

if (condition-1):
    if(condition-2):
        block of code
    else:
        block of code
else:
    block of code
"""

age = int(input("Enter your age:"))
if age >= 18:
    weight = float(input("Enter your weight: "))
    if weight >= 50:
        print("You are eligible for donate.")
    else:
        print("You are not eligible for donate.")
else:
    print("You are not eligible for donate.")
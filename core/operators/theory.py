"""Operators are special symbols or keywords that perform operations on operands. Operands are the values or variables upon which the operators act.

a = b + c

a, b, c - Operands
=, + - Operators

Types of Operators:
-----------------------------------------------------------------------------------
1. Arithmetic Operators: Used to perform mathematical operations.

Operators : +, -, /, *, %, //, **

2. Comparison (Relational) Operators: Used to compare two values.

Operators : >, <, >=, <=, ==,!=

3. Logical Operators: Used to combine conditional statements.

Operators : and, or, not

4. Assignment Operators: Used to assign values to variables.

Operators : =, +=, -=, /=, %=, //=, **=

5. Bitwise Operators: Used to perform bit-level operations.

Operators : &, |, ~, ^, <<, >>

6. Identity Operators: Used to compare the memory locations of two objects.

Operators : is, is not

7. Membership Operators: Used to check if a value is present in a sequence (like a list or string).

Operators : in, not in
"""

# Arithmetic Operators



"""

# num1 = 10
# num2 = 20

"""

# 1. Arithmetic Operators: Used to perform mathematical operations.

# Operators : +, -, /, *, %, //, **

num1 = 5

num2 = 2

# print("Addition:", num1 + num2)

# print("Subtraction:", num1 - num2)

# print("Multiplication:", num1 * num2)

# print("Division:", num1 / num2)

# print("Modulus:", num1 % num2)

# print("Floor Division:", num1 // num2)

# print("Exponentiation:", num1 ** num2)


# Comparison (Relational) Operators

# Operators : >, <, >=, <=, ==,!=

# print("num1 > num2:", num1 > num2)

# print("num1 < num2:", num1 < num2)

# print("num1 >= num2:", num1 >= num2)

# print("num1 <= num2:", num1 <= num2)

# print("num1 == num2:", num1 == num2)

# print("num1!= num2:", num1!= num2)


# Logical Operators

# Operators : and, or, not

# A B C and or
# T T T T   T
# F T T F   T
# T F T F   T
# T T F F   T
# F F F F   F

# A not
# T F
# F T

# Example :

c1 = True
c2 = False
c3 = 34 < 56 # True
c4 = (34 != 34) # False
c5 = 0 # False
c6 = 1 # True

# print("c1 and c2:", c1 and c2) # False

# print("c1 or c2:", c1 or c2) # True

# print("not c1:", not c1) # False

# print("c3 and c4:", c3 and c4) # False


# # Assignment (shorthand) operators

# x = 10

# # x = x + 20

# # x += 20 

# # print(x)

# identity operators | value, type, location

# x = 10
# y = "10"

# print(x is y)
# print(x is not y)

# membership operators

name = "Python"

# print('J' in name)
# print('t' in name)
# print('T' in name)
# print('tho' in name)
# print('to' not in name)

# Bitwise operators

x = 7
y = 5

# print("Binary AND:", x & y)
# print("Binary OR:", x | y)
# print("Binary OR:", ~ y)
# print("Binary OR:", x ^ y)
x = x << 3
x = x << 1
print(x)
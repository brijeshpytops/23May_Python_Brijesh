"""
String: immutable

What is string?

A string is a sequence of characters. In Python, a string is a collection of characters enclosed in single quotes (') or double quotes (").

sytnax :

string_name = "value"
"""

# Sample code to demonstrate string declaration

my_string = "Hello, World!"
my_string = 'Hello, World!'
my_string = '''Hello, World!'''
my_string = """Hello, World!"""
my_string = str()

# print(type(my_string))

code = "python"
# print(len(code))

# print(code)

# indexing (+/-)
# p 0 -6
# y 1 -5
# t 2 -4
# h 3 -3
# o 4 -2
# n 5 -1

# print(code[-4])
# print(code[2])

# slicing (+/-)
# print(code[2:5])
# print(code[-2:-5:-1][::-1])

# print(code[-4:-1]) # positive


# concat:

# fname = "brijesh"
# lname = "gondaliya"

# print(fname + " " + lname)

# replica

# print(code * 3)

# num = 10

# for row in range(1, num+1):
#     print(" "*(num-row), " *"*row)

# for ch in code:
#     print(chr(ord(ch)))

# string methods
# print(dir(code))

name = "TopS TEchNolOGy PvT. LTd."
# print(name.lower())
# print(name.upper())
# print(name.capitalize())
# print(name.title())
# print(name.swapcase())

# space = "     python code    "
# print(space.rstrip())
# print(space.lstrip())
# print(space.strip())
# print(space.replace(" ", ""))

# print("TopS TEchNolOGy PvT. LTd.".lower().find("Tech".lower()))

# print("TopS TEchNolOgy PvT. LTd.".lower().startswith("tops"))

# print("TopS TEchNolOgy PvT. LTd.".lower().endswith(".ltd."))

center = "python"
# print(center.center(20, '*'))

# print('name : "brijesh gondaliya"')
# print("name : 'brijesh gondaliya'")
# print("name :\"brijesh gondaliy\"")
# print('\'')


# password = "#%#$%#$%"

# print(not password.isalnum())
# print(password.isalpha())
# print(password.isdigit())

# is_upper = False
# is_lower = False
# is_digit = False
# is_spe_ch = False
# is_8_plus = False

# password = input("Enter a password: ")

# if len(password) >= 8:
#     is_8_plus = True
#     for ch in password:
#         if ch.isupper():
#             is_upper = True

#         if ch.islower():
#             is_lower = True

#         if ch.isdigit():
#             is_digit = True

#         if not ch.isalnum():
#             is_spe_ch = True

# if is_upper and is_lower and is_digit and is_spe_ch and is_8_plus:
#     print("Valid password")
# else:
#     print("Invalid password")


# name = "python"
price = 399.256765367450
pages = 345

# print("my book name is python and its price and page is 399.20 and 345.")
# print(f"my book name is {name} and its price and page is {price} and {pages}.")
# print("my book name is {} and its price and page is {} and {}.".format(name, price, pages))
# print("my book name is {0} and its price and page is {1} and {2}.".format(name, price, pages))
# print("my book name is {1} and its price and page is {2} and {3}.".format(name,name, price, pages))
# print("my book name is %s and its price and page is %.2f and %d." % (name, price, pages))


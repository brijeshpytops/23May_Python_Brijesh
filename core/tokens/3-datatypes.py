"""
Data types are classifications that specify which kind of value a variable can hold. Understanding data types is fundamental to writing effective Python code.

1] Numeric Types: 
int: Integer type, used for whole numbers.
    Examples: 10, -5, 0

float: Floating-point number type, used for decimal numbers.
    Examples: 3.14, -2.71828, 0.0

complex: Complex number type, used for complex numbers with a real and an imaginary part.
    Examples: 1+2j, -3+4j, 0+0j

2] Sequence Types:

str: String type, used for storing textual data.
    Examples: "Hello, World!", "Python is awesome!"

list: List type, used for storing multiple values in a single variable.
    Examples: [1, 2, 3, 4, 5], ["apple", "banana", "cherry"]

tuple: Tuple type, similar to a list but immutable.
    Examples: (1, 2, 3, 4, 5), ("apple", "banana", "cherry")

3] Mapping Types:

dict: Dictionary type, used for storing key-value pairs.
    Examples: {"name": "John", "age": 30}, {"fruit": "apple", "color": "red"}

4] Boolean Type:
    bool: Boolean type, used for storing boolean values.
    Example: is_active = True, False

5] Set Types:

set: Set type, used for storing unique values.
    Examples: {1, 2, 3, 4, 5}, {"apple", "banana", "cherry"}

frozenset: Immutable set type.
    frozen_numbers = frozenset([1, 2, 3, 4, 5])

6] Binary Types :

bytes: Binary data type, used for storing binary data.
    Examples: b"Hello, World!", b"\x48\x65\x6c\x6c\x6f, \x57\x6f\x72\x6c\x64!"

bytearray: Mutable binary data type.
    byte_array = bytearray(b"Hello, World!")

7] None Type:
    None: Represents the absence of a value.
    Example: my_variable = None
    
"""

# age = 45
# print(type(age)) # <class 'int'>

# name = "John Doe"

# print(type(name)) # <class 'str'>

# is_active = True

# print(type(is_active)) # <class 'bool'>

# numbers = [1, 2, 3, 4, 5]

# print(type(numbers)) # <class 'list'>

# person = {"name": "John Doe", "age": 45}

# print(type(person)) # <class 'dict'>

# my_variable = None

# print(type(my_variable)) # <class 'NoneType'>

# numbers_set = {1, 2, 3, 4, 5}

# print(type(numbers_set)) # <class 'set'>

# numbers_frozenset = frozenset([1, 2, 3, 4, 5])

# print(type(numbers_frozenset)) # <class 'frozenset'>

# binary_data = b"Hello, World!"

# print(type(binary_data)) # <class 'bytes'>

# byte_array = bytearray(b"Hello, World!")

# print(type(byte_array)) # <class 'bytearray'>


# There are two types of type conversion

# 1) Implicit Conversion: Python automatically converts one data type to another when necessary.

# a = 10
# b = 10.5
# a = a + b
# c = a + b
# print(c)

# a = 10
# b = 2
# print(a/b)

# 2) Explicit Conversion: You need to convert one data type to another using built-in functions.

# a = 10

# # Convert int to float

# b = float(a)
# print(b)

# x = "dhjgnfhcdhjg"
# y = int(x)
# print(y)

x = "10"
y = int(x)
z = float(y)
print(z)
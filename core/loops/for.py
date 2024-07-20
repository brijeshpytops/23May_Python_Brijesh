"""
syntax:

for var in sequence:
    block of code
"""

# for ch in "python":
#     print(ch)

# for num in range(1, 11):
#     print(num)

# for num in range(10, 0, -1):
#     print(num)

# for num in range(1, 11):
#     if num % 2 == 0:
#         print(num, "Even")
#     else:
#         print(num, "Odd")

# code = "python"

# i = iter(code)

# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# code = "python"
# for index in range(len(code)):
#     print(index, code[index])

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# num = 5

# for row in range(1, num+1):
#     for col in range(num-row, 0, -1):
#         print(" ", end=" ")
#     for col in range(1, row+1):
#         print("*", end=" ")
#     print()
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print(" ", end=" ")
#     for col in range(num-row, 0, -1):
#         print("*", end=" ")
#     print()

num = 5

for row in range(1, num+1):
    for col in range(num-row, 0, -1):
        print(" ", end=" ")
    for col in range(1, row+1):
        if col == 1:
            print(row, end=" ")
        else:
            print(" ", end=" ")
    print()

# print("brijesh", end=' ')
# print("r.", end=' ')
# print("G.")
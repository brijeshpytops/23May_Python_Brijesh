# """
# function:

# What is function?

# A function is a block of code that performs a specific task. It takes input values, performs a series of operations, and produces an output value.

# syntax:

# def function_name(parameters):
#     block of code

# function call

# function_name(arguments)

# """

# # a = 10
# # b = 20

# # c = a + b

# # print(c)

# # d = 30
# # e = 40

# # f = d + e

# # print(f)

# # def add(num1, num2):
# #     print(num1 + num2)

# # add(10, 20)
# # add(30, 40)

# # function: types of parameters
# # 1] positional para
# def add(num1, num2, num3):
#     print(num1 + num2)

# # add(10, 20, 30)


# # 2] default/keyword para
# def bill(potato, tomato=120):
#     """
#     This function will return total of product price.
#     """
#     print(tomato + potato)

# # bill(30, 50)

# # 3] variable length para
# # *args
# # **kwargs

# # def add(*nums):
# #     # print(type(nums))
# #     print(sum(nums))

# #     total = 0
# #     for num in nums:
# #         total += num
# #     print(total)

# # add(1,2,3,4,5,5,101990786,8623)

# # **kwargs

# # def person_info(**kwargs):
# #     for key, value in kwargs.items():
# #         print(f"{key}: {value}")

# # person_info(name="John Doe", age=30, city="New York", deprt="IT")


# # function: return statement

# # def calculate_sum(num1, num2):
# #     return num1 + num2, num1 - num2

# # result1, result2 = calculate_sum(10, 20)
# # print(result1 )

# x = 20 # global

# def test():
#     global x  # this line makes x a global variable
#     x = 10.2 # local var
#     print(x)

# # test()
# # print(x)

# # function: recursion

# # 1 + 2 + 3 + 4 ...
# # (1 + 2) + (2 + 3) + ....
# # (1 * 2) + (2 * 3) + ....
# # (1 * 2 * 3 ...)
# # [1, 4, 9, 16, 25..]
# # 0 1 1 2 3 5 8..

# # def sum_of_n_nums(num):
# #     if num == 1:
# #         print(num, end=" ")
# #         return 1
# #     else:
# #         print(f"({num} + {num+1})", end=" ")
# #         return (num + (num + 1) ) + sum_of_n_nums(num-1)

# # print(sum_of_n_nums(int(input("Enter a number: "))))


# # function: lambda
# # cube = lambda x:x*x*x

# # print(cube(3))

# # decorators

# def swap_case(func):
#     def wrapper():
#         result = func()
#         print(result.swapcase())
#         return result.swapcase()
#     return wrapper

# def upper_case(func):
#     def wrapper():
#         result = func()
#         return result.upper()
#     return wrapper
# @swap_case
# @upper_case
# def test():
#     return input("Enter something....")

# # print(test())

# nums = [1,2,3,4,5]
# # print(list(map(lambda x:x*x, nums)))
# def even(num):
#     if(num%2!=0):
#         return num
# print(list(filter(even, nums)))


# def outer():
#     def inner():
#         return "i am from inner function"
#     return inner()

# print(outer())


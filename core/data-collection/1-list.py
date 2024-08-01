"""
List - mutable, odered, allow duplicate values, indexed, sliced

syntax:

list_name = []
list_name = list()

list_name = [value1, value2,..., valueN]

"""

# stu1 = 56
# print(stu1)
# stu2 = 78
# print(stu2)

# students = [56, 78, 98, 45, 78, 78]

# for stu in students:
#     print(stu)

mix = [1,2,4.5, 65.6, "python", 3 + 54653j]

# print(type(mix))

# print(len(mix))

# nums = [1,2,3,4,5,6,7,8,9,10]
# print(nums)

mummy_items = ['milk', 'butter-milk']
bajuvad_aunty = ['milk', 'pen']
# del bajuvad_aunty
apdi_product = ['drink']
sister = ['chocolate']

# mix = mummy_items + bajuvad_aunty + apdi_product * 2 + sister
# print(mix)

# indexing
# mix[-1] = 'book'
# print(mix)
# print(mix)

# slicing
# print(mix[2:4])

# del mix[-1]
# print(mix)

# list methods
# print(dir([]))
# '', '', '', '', '', '', '', '', '', 

nums = [1,2,3,4,5,1,2,1,3,1,1,2,1,1,1]

# new = [10]
# nums.append(new)
# nums.extend(new)
# nums.insert(1, new)
# nums.pop()
# nums.remove(4)
# nums.clear()

# print(nums.index(4))

# print(nums.count(1))

x = 10
y = 10

# print(id(x) == id(y))

# copy_nums = nums.copy()
# print(id(nums))
# print(id(copy_nums))

# 'reverse', 'sort'
# nums.sort(reverse=True)

# nums.reverse()
# print(nums)

# nested_list = [1,2,[3,4,[5, 6,7,[8,9,10,[11]]]]]
# print(len(nested_list))
# print(nested_list[-1][-1][-1][-1][-1])

# users = [
#     ['brijesh', 'gondaliya', 28, 'brijesh@gmil.com', '6536256234'],
#     ['raj', 'shah', 22, 'raj@gmil.com', '6536256756234'],
# ]
# for user in users:
#     for data in user:
#         print(data)

users = []

is_first_time = True
flag = True
while(flag):
    if is_first_time:
        is_first_time = False
    else:
        yesNo = input("You want to continue? [y/n]").lower()
        if yesNo == 'y':
            flag = True
        else:
            flag = False
            break

    name = input("Enter your name: ")
    user = [name]
    users.append(user)

print(users)
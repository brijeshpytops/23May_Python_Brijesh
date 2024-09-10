nums = [1,2,3]
nums.append(4)
# print(nums)

code = "python"
l_code = list(code)
# l_code.reverse()
# print(l_code)
# l_str = ''.join(list(code)[::-1])
# print(l_str)


nums = [1,2,3,4,5,6]
alpha = ['a', 'b', 'c', 'd', 'e']
print(list(zip(nums, alpha)))


pairs = [(1,2), (3,4), (5,6)]
nums, alpha = zip(*pairs)
print(nums)
print(alpha)
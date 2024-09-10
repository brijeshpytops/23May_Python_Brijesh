# class Math:
#     def add(self, a, b):
#         return a + b
    
#     def add(self, a, b, c):
#         return a + b + c
    
# obj = Math()
# print(obj.add(10, 20, 30))


# x = 10
# x = 20
# print(x)

# Achive method overloding
# class Math:
#     def add(self, a = None, b = None, c = None):
#         if a != None and b != None and c != None:
#             return a + b + c
#         elif a != None and b != None:
#             return a + b
        

# obj = Math()

# print(obj.add(10, 20, 30))

# print(obj.add(10, 20))


# method overriding

class information:
    def get_info(self):
        return "This is an information class"
    
class Student(information):
    def get_info(self):
        print(super().get_info())
        return "This is a student class"
    
obj = Student()

print(obj.get_info())
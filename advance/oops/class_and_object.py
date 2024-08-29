# # table

# # length = 3
# # base = 5
# # height = 3

# # def find_area_of_table():
# #     return length * base * height

# # print(length)
# # print(base)
# # print(height)
# # print(find_area_of_table())

# """
# syntax:

# class class_name:
#     data member [attributes and properties]

#     membrer function [function or method or behavior]


# syntax of object

# object_name = class_name()
# """

# class table:
#     # data member [attributes and properties]
#     length = 3
#     base = 5
#     height = 3

#     # membrer function [function or method or behavior]
#     def find_area_of_table(self):
#         return self.length * self.base * self.height
    
# t1 = table()
    
# print(t1.length)
# print(t1.base)
# print(t1.height)
# print(t1.find_area_of_table())

# nums = []
# nums = list()
# nums.append(fdsg)

class Auth:
    class Regiter:
        username = "admin"
        email = "admin@gmail.com"
        password = "admin123"
        confirm_password = "admin123"

        def check_password(self):
            if self.password == self.confirm_password:
                return True
            else:
                return False
            
        def is_email_valid(self):
            return True

        def is_username_available(self):
            return True


        def regiter_user(self):
            if self.check_password():
                if self.is_email_valid() and self.is_username_available():
                    print("User registered successfully")
                else:
                    print("Failed to register user")
            else:
                print("Passwords do not match")



    # class login:
    #     pass

    # class forgot_password:
    #     pass

# auth = Auth()
# register = auth.Regiter()
# register.regiter_user()

# Auth().Regiter().regiter_user()
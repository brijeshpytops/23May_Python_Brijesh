# class Auth:
#     class Register:
#         def __init__(self, username, email, password, confirm_password):
#             self.username = username
#             self.email = email
#             self.password = password
#             self.confirm_password = confirm_password

#         def check_password(self):
#             if self.password == self.confirm_password:
#                 return True
#             else:
#                 return False
            
#         def is_email_valid(self):
#             if "@gmail.com" in self.email:
#                 return True
#             else:
#                 return False
            
#         def save_to_database(self):
#             if self.check_password() and self.is_email_valid():
#                 # Save data to database
#                 print(f"User {self.username} saved successfully.")
#             else:
#                 print("Failed to save user.")

# brijesh = Auth().Register("brjiesh07", "brijesh@gmail.com", "12345", "1234")

# brijesh.save_to_database()

# class ATM:
#     def __init__(self, account_number, pin):
#         self.account_number = account_number # public
#         self.__pin = pin # private
#         self.balance = 0

#     def validate_pin(self, entered_pin):
#         if entered_pin == self.pin:
#             return True
#         else:
#             return False

#     def deposit(self, amount):
#         print("Pin is ", self.__pin)
#         self.balance += amount
#         print(f"Deposited {amount}. New balance is {self.balance}.")

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew {amount}. New balance is {self.balance}.")
#         else:
#             print("Insufficient balance.")

# brijesh = ATM("111222333444", "1111")

# brijesh.deposit(1000)

# # brijesh.withdraw(500)

# print(brijesh.account_number)

# # print(brijesh.__pin) # Throws error

# print(brijesh._ATM__pin) # [name mangling syntax: obj._classname__varname]


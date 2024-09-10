import re

# print(dir(re))

# data = "dg jbdsmfjgxcmyuc ccyu, 23-12-1996 dg jbdsmfjgxcmyuc ccyu, 2-10-2000 dg jbdsmfjgxcmyuc ccyu, 3/4/2001 dg jbdsmfjgxcmyuc ccyu,"

# pattern = r"\b\d{1,2}[-/]\d{1,2}[-/]\d{4}\b"

# matches = re.findall(pattern, data)
# print(matches)

# print(r"brijesh go\ndaliya")

# data = "brijesh.gondaliy07@gmail.com"

# email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
# res = re.search(email_pattern, data)
# print(res.group())



mobile_number = "+91 98765 43210"
if re.match(r"^\+(?:[0-9] ?){6,14}[0-9]$", mobile_number):
    print("Valid mobile number")
else:
    print("Invalid mobile number")
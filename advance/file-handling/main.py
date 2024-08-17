file =  open('sample1.txt', 'w')

print(file.tell())

file.seek(6)
print(file.tell())
# print(file.read())
file.write("\nhello")


# file.write(input("Enter something...."))

# print(file.read())
# print(file.read(6))
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readlines())

# lines = ['This is a line - 1\n', 'This is a line - 2\n', 'This is a line - 3\n', 'This is a line - 4\n', 'This is a line - 5\n', 'This is a new line']
# file.writelines(lines)

# file.write("\nthis is a 8 line")
# file.close()

import os
import uuid

# os.system("type nul > test.csv")
# os.rename('example.pdf', f'{str(uuid.uuid4())}.pdf')
# os.remove(r'C:\Brijesh_Work\batch\23May_Python_Brijesh\advance\file-handling\491dec04-0d9b-4af7-803c-b8f653e359ff.pdf')
# os.mkdir('test')
# os.rmdir('test')
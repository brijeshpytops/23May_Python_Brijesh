"""
Identifiers rules:

1. [a-z, A-Z, 0-9, _]
2. Identifier names cannot start with a number. For example : 1level = "start"
3. Identifier names are case sensitive. For example : level1 and LEVEL1 are different identifiers.
4. Python keywords cannot be used as identifiers. For example : for, while, if, else, etc.
5. Identifiers should be descriptive and meaningful. For example : my_variable_name, my_function_name, etc.
6. White space are not allowed. For example : first name, last name
7. special characters are not allowed : for example, @name, #tops

Here is a sample code to demonstrate identifiers rules:

valid identifiers:
    my_variable_name,
    my_function_name,
    level1, level_1,
    PI, gravity,
    _my_variable_name

Invalid identifiers
    1_my_variable_name
    for, while, if, else,
    my_function_name@,
    my_function_name#tops

naming conventions rules :

1. (snack_case) lowercase with words separated by underscores : my_variable_name, my_function_name - function, variable
2. (camelCase) capitalize the first letter of each word : myVariableName, myFunctionName, class
3. (PascalCase) capitalize the first letter of each word : MyVariableName, MyFunctionName, class
"""

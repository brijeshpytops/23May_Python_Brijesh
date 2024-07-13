"""
Keyword : A keyword in Python is a special, reserved word that has a predefined meaning within the language. These keywords cannot be used as variable names, function names, or any other identifiers in your code. They form the building blocks of Python's syntax, dictating how the code is structured and interpreted.

Here are some key characteristics of keywords:

Predefined: Their meaning is fixed and cannot be changed by the programmer.
Case-sensitive: if is different from If.
Limited set: There are a specific number of keywords in Python (35 in Python 3.11). You can find the complete list using the keyword.kwlist attribute in your code.
Essential for syntax: They define the control flow, data types, and other core functionalities.

Why keywords are important:

Clarity and Consistency: They ensure that everyone writing Python code understands the same meaning for these reserved words.
Structure and Control: Keywords provide the framework for how your code executes, controlling the flow and behavior.
Preventing Errors: Using reserved words for other purposes would lead to syntax errors.

step-1] open your cmd
step-2] write "python" and hit enter

C:\Users\pc>python
Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>

step-3] write help() and hit enter
>>> help()
Welcome to Python 3.12's help utility! If this is your first time using
Python, you should definitely check out the tutorial at
https://docs.python.org/3.12/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To get a list of available
modules, keywords, symbols, or topics, enter "modules", "keywords",
"symbols", or "topics".

Each module also comes with a one-line summary of what it does; to list
the modules whose name or summary contain a given string such as "spam",
enter "modules spam".

To quit this help utility and return to the interpreter,
enter "q" or "quit".

help>

step-4] write "Keywords" and hit enter
help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not


False: Boolean value representing "not true"
None: Represents the absence of a value
True: Boolean value representing "true"
and: Logical operator that returns True only if both operands are True
as: Used for aliasing variables or associating a value with a pattern in a for loop
assert: Checks a condition and raises an AssertionError if it's False (for debugging)
async: Declares an asynchronous function that can be used with awaitawait: Pauses execution of an asynchronous coroutine until it's ready
break: Exits the current loop prematurely
class: Defines a blueprint for creating objects (used with object-oriented programming)
continue: Skips to the next iteration of the current loop
def: Defines a function that encapsulates a block of code
del: Deletes a variable or object reference
elif: Alternative condition in an if statement (else if)
else: Executes code if none of the preceding conditions in an if statement are True
except: Handles exceptions (errors) that may occur during code execution
finally: Executes code always, regardless of exceptions (often used for cleanup)
for: Creates a loop that iterates over a sequence
from: Imports specific items from a module
global: Declares a variable that is accessible from within a nested function
if: Executes code conditionally based on a Boolean expression
import: Imports modules that provide functionality
in: Checks if a value is present within a sequence (like a list or string)
is: Identity operator that checks if two objects are the same object in memory
lambda: Creates a small, anonymous function (often used for short, inline functions)
nonlocal: Modifies a variable from an enclosing function's scope
not: Logical operator that inverts the truth value of an operand
or: Logical operator that returns True if at least one operand is True
pass: Empty statement (used as a placeholder when no code is needed)
raise: Raises an exception to signal an error
return: Exits a function and optionally sends a value back
try: Starts a block of code where exceptions may occur
while: Creates a loop that continues as long as a condition is True
with: Used for context managers (like opening and closing files)
yield: Pauses a generator function and returns a value (used for iterators)
"""
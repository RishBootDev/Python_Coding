# ------------------------------------------------------------
# 1. WHAT IS A FUNCTION?
# ------------------------------------------------------------
# A function is a reusable block of code that performs a task.
# Functions help us avoid repeating the same code.
#
# Syntax:
# def function_name(parameters):
#     statements
#     return value
#
# def       -> keyword used to define a function
# function_name -> name of the function
# parameters   -> inputs accepted by the function
# return       -> sends a result back to the caller


# ------------------------------------------------------------
# 2. BASIC FUNCTION
# ------------------------------------------------------------

def greet():
    print("Hello, Python!")

greet()

# Output:
# Hello, Python!


# ------------------------------------------------------------
# 3. FUNCTION WITH PARAMETERS
# ------------------------------------------------------------
# Parameters are variables written in the function definition.
# Arguments are actual values passed when calling the function.

def greet_user(name):
    print("Hello", name)

greet_user("Rishabh")

# Output:
# Hello Rishabh


# ------------------------------------------------------------
# 4. FUNCTION WITH MULTIPLE PARAMETERS
# ------------------------------------------------------------

def add(a, b):
    print(a + b)

add(10, 20)

# Output:
# 30


# ------------------------------------------------------------
# 5. RETURN STATEMENT
# ------------------------------------------------------------
# return sends a value back to the caller.
# print() displays a value but does not return it.
# Code after return in the same execution path is not executed.

def add(a, b):
    return a + b

result = add(10, 20)
print(result)

# Output:
# 30


# ------------------------------------------------------------
# 6. PRINT VS RETURN
# ------------------------------------------------------------

def using_print():
    print(100)

def using_return():
    return 100

a = using_print()
b = using_return()

print("a =", a)
print("b =", b)

# Output:
# 100
# a = None
# b = 100


# ------------------------------------------------------------
# 7. FUNCTION RETURNING MULTIPLE VALUES
# ------------------------------------------------------------
# Python can return multiple values as a tuple.
# You can unpack the returned values into separate variables.

def calculate(a, b):
    return a + b, a - b, a * b

addition, subtraction, multiplication = calculate(10, 5)

print(addition)
print(subtraction)
print(multiplication)

# Output:
# 15
# 5
# 50


# ------------------------------------------------------------
# 8. DEFAULT ARGUMENTS
# ------------------------------------------------------------
# A default argument is used when the caller does not provide
# a value for that parameter.
# Parameters with defaults must generally follow required ones.

def greet(name, message="Welcome"):
    print(message, name)

greet("Rishabh")
greet("Rishabh", "Good morning")

# Output:
# Welcome Rishabh
# Good morning Rishabh


# ------------------------------------------------------------
# 9. POSITIONAL ARGUMENTS
# ------------------------------------------------------------
# Values are assigned to parameters according to their positions.

def student(name, age):
    print(name, age)

student("Rishabh", 21)

# Output:
# Rishabh 21


# ------------------------------------------------------------
# 10. KEYWORD ARGUMENTS
# ------------------------------------------------------------
# Values are assigned using parameter names.
# Keyword arguments can be provided in a different order.

def student(name, age):
    print(name, age)

student(age=21, name="Rishabh")

# Output:
# Rishabh 21


# ------------------------------------------------------------
# 11. MIXING POSITIONAL AND KEYWORD ARGUMENTS
# ------------------------------------------------------------
# Positional arguments must come before keyword arguments
# when making a normal function call.

def introduce(name, age, city):
    print(name, age, city)

introduce("Rishabh", age=21, city="Bhopal")

# Output:
# Rishabh 21 Bhopal


# ------------------------------------------------------------
# 12. ARBITRARY POSITIONAL ARGUMENTS: *args
# ------------------------------------------------------------
# *args collects extra positional arguments into a tuple.
# The name args is conventional; another name is allowed.

def add_all(*args):
    print(args)
    print(sum(args))

add_all(10, 20, 30, 40)

# Output:
# (10, 20, 30, 40)
# 100


# ------------------------------------------------------------
# 13. ARBITRARY KEYWORD ARGUMENTS: **kwargs
# ------------------------------------------------------------
# **kwargs collects extra keyword arguments into a dictionary.

def show_details(**kwargs):
    print(kwargs)

show_details(name="Rishabh", age=21, city="Bhopal")

# Output:
# {'name': 'Rishabh', 'age': 21, 'city': 'Bhopal'}


# ------------------------------------------------------------
# 14. USING *args AND **kwargs TOGETHER
# ------------------------------------------------------------
# *args collects positional arguments.
# **kwargs collects keyword arguments.
# The standard order is regular parameters, *args, then **kwargs.

def display(*args, **kwargs):
    print("Arguments:", args)
    print("Keyword arguments:", kwargs)

display(10, 20, 30, name="Rishabh", age=21)

# Output:
# Arguments: (10, 20, 30)
# Keyword arguments: {'name': 'Rishabh', 'age': 21}


# ------------------------------------------------------------
# 15. UNPACKING ARGUMENTS USING * AND **
# ------------------------------------------------------------
# * unpacks an iterable into positional arguments.
# ** unpacks a dictionary into keyword arguments.

def add(a, b, c):
    return a + b + c

numbers = [10, 20, 30]
print(add(*numbers))

details = {"a": 10, "b": 20, "c": 30}
print(add(**details))

# Output:
# 60
# 60


# ------------------------------------------------------------
# 16. POSITIONAL-ONLY PARAMETERS: /
# ------------------------------------------------------------
# Parameters before / can only be supplied positionally.
# This syntax is available in Python 3.8 and later.

def divide(a, b, /):
    return a / b

print(divide(10, 2))

# Output:
# 5.0

# divide(a=10, b=2) would raise TypeError.


# ------------------------------------------------------------
# 17. KEYWORD-ONLY PARAMETERS: *
# ------------------------------------------------------------
# Parameters after * must be passed using their names.

def create_user(name, *, age, city):
    print(name, age, city)

create_user("Rishabh", age=21, city="Bhopal")

# Output:
# Rishabh 21 Bhopal

# create_user("Rishabh", 21, "Bhopal") would raise TypeError.


# ------------------------------------------------------------
# 18. COMBINING /, *args, AND KEYWORD-ONLY PARAMETERS
# ------------------------------------------------------------

def example(a, b, /, *args, c, **kwargs):
    print(a, b)
    print(args)
    print(c)
    print(kwargs)

example(1, 2, 3, 4, c=5, name="Rishabh")

# Output:
# 1 2
# (3, 4)
# 5
# {'name': 'Rishabh'}


# ------------------------------------------------------------
# 19. VARIABLE SCOPE: LOCAL VARIABLES
# ------------------------------------------------------------
# A local variable is created inside a function.
# It is normally accessible only within that function.

def show():
    x = 10
    print(x)

show()

# Output:
# 10

# print(x) outside the function would raise NameError.


# ------------------------------------------------------------
# 20. GLOBAL VARIABLES
# ------------------------------------------------------------
# A global variable is defined outside functions.
# A function can read a global variable without declaring global.

x = 100

def show_global():
    print(x)

show_global()

# Output:
# 100


# ------------------------------------------------------------
# 21. MODIFYING GLOBAL VARIABLES USING global
# ------------------------------------------------------------
# Use global when assigning to a module-level variable
# from inside a function.

count = 0

def increment():
    global count
    count += 1

increment()
increment()

print(count)

# Output:
# 2


# ------------------------------------------------------------
# 22. NONLOCAL VARIABLES
# ------------------------------------------------------------
# nonlocal modifies a variable in an enclosing function scope.
# It is useful with nested functions and closures.

def outer():
    x = 10

    def inner():
        nonlocal x
        x += 5

    inner()
    print(x)

outer()

# Output:
# 15


# ------------------------------------------------------------
# 23. NESTED FUNCTIONS
# ------------------------------------------------------------
# A function can be defined inside another function.

def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()

outer()

# Output:
# Outer function
# Inner function


# ------------------------------------------------------------
# 24. RECURSION
# ------------------------------------------------------------
# Recursion occurs when a function calls itself.
# Every recursive solution needs a base case to stop recursion.

def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))

# Output:
# 120

# factorial(5)
# = 5 * factorial(4)
# = 5 * 4 * factorial(3)
# = 5 * 4 * 3 * factorial(2)
# = 5 * 4 * 3 * 2 * factorial(1)
# = 120


# ------------------------------------------------------------
# 25. RECURSION: FIBONACCI SERIES
# ------------------------------------------------------------

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))

# Output:
# 8

# This basic recursive approach repeats calculations.
# Memoization or dynamic programming can improve performance.


# ------------------------------------------------------------
# 26. LAMBDA FUNCTIONS
# ------------------------------------------------------------
# A lambda is a small anonymous function.
# It can contain only one expression.
#
# Syntax:
# lambda parameters: expression

square = lambda x: x * x

print(square(5))

# Output:
# 25


# ------------------------------------------------------------
# 27. LAMBDA WITH MULTIPLE PARAMETERS
# ------------------------------------------------------------

add = lambda a, b: a + b

print(add(10, 20))

# Output:
# 30


# ------------------------------------------------------------
# 28. LAMBDA WITH CONDITIONAL EXPRESSIONS
# ------------------------------------------------------------

check = lambda n: "Even" if n % 2 == 0 else "Odd"

print(check(10))
print(check(7))

# Output:
# Even
# Odd


# ------------------------------------------------------------
# 29. HIGHER-ORDER FUNCTIONS
# ------------------------------------------------------------
# A higher-order function takes another function as an argument
# or returns a function as its result.

def apply_operation(func, a, b):
    return func(a, b)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print(apply_operation(add, 10, 20))
print(apply_operation(multiply, 10, 20))

# Output:
# 30
# 200


# ------------------------------------------------------------
# 30. FUNCTIONS AS RETURN VALUES
# ------------------------------------------------------------
# A function can return another function.

def outer():
    def inner():
        return "Hello from inner"

    return inner

func = outer()
print(func())

# Output:
# Hello from inner


# ------------------------------------------------------------
# 31. map() FUNCTION
# ------------------------------------------------------------
# map(function, iterable) applies a function to every item.
# In Python 3, map returns an iterator.
# list() converts the result to a list.

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

print(result)

# Output:
# [2, 4, 6, 8, 10]


# ------------------------------------------------------------
# 32. map() WITH A NORMAL FUNCTION
# ------------------------------------------------------------

def square(n):
    return n * n

numbers = [1, 2, 3, 4]

result = list(map(square, numbers))

print(result)

# Output:
# [1, 4, 9, 16]


# ------------------------------------------------------------
# 33. filter() FUNCTION
# ------------------------------------------------------------
# filter(function, iterable) keeps items for which the function
# returns a truthy value.

numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)

# Output:
# [2, 4, 6]


# ------------------------------------------------------------
# 34. REDUCE() FUNCTION
# ------------------------------------------------------------
# reduce() repeatedly combines items into a single result.
# It must be imported from functools.

from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda a, b: a + b, numbers)

print(result)

# Output:
# 15

# Step-by-step:
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15


# ------------------------------------------------------------
# 35. SORTING USING A KEY FUNCTION
# ------------------------------------------------------------
# key specifies a function that determines sorting order.

numbers = [5, -2, 8, -10, 3]

print(sorted(numbers, key=abs))

# Output:
# [-2, 3, 5, 8, -10]

# Sorting is based on absolute values.


# ------------------------------------------------------------
# 36. CLOSURES
# ------------------------------------------------------------
# A closure is an inner function that retains access to variables
# from its enclosing function even after that function returns.

def multiplier(factor):
    def multiply(n):
        return n * factor

    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(10))
print(triple(10))

# Output:
# 20
# 30


# ------------------------------------------------------------
# 37. DECORATORS
# ------------------------------------------------------------
# A decorator takes a function and returns a modified function.
# @decorator_name is shorthand for function = decorator_name(function).

def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper

@decorator
def greet():
    print("Hello")

greet()

# Output:
# Before function
# Hello
# After function


# ------------------------------------------------------------
# 38. DECORATOR USING *args AND **kwargs
# ------------------------------------------------------------
# This pattern lets the wrapper accept different argument types.

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is starting")
        result = func(*args, **kwargs)
        print("Function has finished")
        return result

    return wrapper

@decorator
def add(a, b):
    return a + b

print(add(10, 20))

# Output:
# Function is starting
# Function has finished
# 30


# ------------------------------------------------------------
# 39. functools.wraps
# ------------------------------------------------------------
# wraps preserves useful metadata such as the original function's
# name and docstring when creating decorators.

from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper

@decorator
def greet():
    """Print a greeting."""
    print("Hello")

print(greet.__name__)
print(greet.__doc__)

# Output:
# greet
# Print a greeting.


# ------------------------------------------------------------
# 40. GENERATOR FUNCTIONS
# ------------------------------------------------------------
# A generator function uses yield instead of returning all values
# at once. It produces values lazily, when requested.
# Its execution can resume from where it last yielded a value.

def generate_numbers():
    yield 1
    yield 2
    yield 3

for n in generate_numbers():
    print(n)

# Output:
# 1
# 2
# 3


# ------------------------------------------------------------
# 41. GENERATOR WITH A LOOP
# ------------------------------------------------------------

def count_up_to(n):
    for i in range(1, n + 1):
        yield i

print(list(count_up_to(5)))

# Output:
# [1, 2, 3, 4, 5]


# ------------------------------------------------------------
# 42. FUNCTION DOCSTRINGS
# ------------------------------------------------------------
# A docstring describes what a function does.
# It is written as a string immediately after the function header.

def square(n):
    """Return the square of a number."""
    return n * n

print(square.__doc__)
print(square(4))

# Output:
# Return the square of a number.
# 16


# ------------------------------------------------------------
# 43. TYPE HINTS
# ------------------------------------------------------------
# Type hints document expected input and output types.
# Python generally does not enforce these annotations at runtime.

def add(a: int, b: int) -> int:
    return a + b

print(add(10, 20))
print(add.__annotations__)

# Output:
# 30
# {'a': <class 'int'>, 'b': <class 'int'>,
#  'return': <class 'int'>}


# ------------------------------------------------------------
# 44. OPTIONAL PARAMETERS USING None
# ------------------------------------------------------------
# None is commonly used to represent an absent optional value.
# Avoid mutable default arguments such as [] or {}.

def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items

print(add_item("Apple"))
print(add_item("Banana"))

# Output:
# ['Apple']
# ['Banana']


# ------------------------------------------------------------
# 45. WHY MUTABLE DEFAULT ARGUMENTS CAN BE DANGEROUS
# ------------------------------------------------------------
# Default values are evaluated once when the function is defined.
# A shared list or dictionary can retain changes between calls.

def add_item_bad(item, items=[]):
    items.append(item)
    return items

print(add_item_bad("Apple"))
print(add_item_bad("Banana"))

# Output:
# ['Apple']
# ['Apple', 'Banana']

# Prefer the None pattern demonstrated in section 44.


# ------------------------------------------------------------
# 46. PASSING A LIST TO A FUNCTION
# ------------------------------------------------------------
# Lists are mutable. A function can modify the original list
# by changing its contents.

def add_number(numbers):
    numbers.append(4)

values = [1, 2, 3]
add_number(values)

print(values)

# Output:
# [1, 2, 3, 4]


# ------------------------------------------------------------
# 47. PASSING AN IMMUTABLE VALUE TO A FUNCTION
# ------------------------------------------------------------
# Reassigning a local parameter does not reassign the caller's
# variable. Python passes object references by assignment.

def change_value(n):
    n = 100

x = 10
change_value(x)

print(x)

# Output:
# 10


# ------------------------------------------------------------
# 48. EXCEPTION HANDLING INSIDE A FUNCTION
# ------------------------------------------------------------
# Use try and except to handle errors that may occur.
# Raise exceptions when a function cannot perform its task.

def divide(a, b):
    if b == 0:
        raise ValueError("Divisor cannot be zero")

    return a / b

print(divide(10, 2))

try:
    print(divide(10, 0))
except ValueError as e:
    print(e)

# Output:
# 5.0
# Divisor cannot be zero


# ------------------------------------------------------------
# 49. FUNCTION WITH A DOCSTRING AND VALIDATION
# ------------------------------------------------------------

def calculate_average(numbers):
    """Return the average of a non-empty collection of numbers."""

    if not numbers:
        raise ValueError("The list cannot be empty")

    return sum(numbers) / len(numbers)

print(calculate_average([10, 20, 30]))

# Output:
# 20.0


# ------------------------------------------------------------
# 50. RECURSION WITH MEMOIZATION
# ------------------------------------------------------------
# Memoization stores previously calculated results.
# It avoids repeating expensive recursive calculations.

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))

# Output:
# 55


# ------------------------------------------------------------
# 51. FUNCTION ANNOTATIONS WITH LISTS
# ------------------------------------------------------------
# Modern Python supports built-in generic types such as list[int].
# This syntax is available in Python 3.9 and later.

def get_squares(numbers: list[int]) -> list[int]:
    return [n * n for n in numbers]

print(get_squares([1, 2, 3, 4]))

# Output:
# [1, 4, 9, 16]


# ------------------------------------------------------------
# 52. FUNCTION ANNOTATIONS WITH OPTIONAL VALUES
# ------------------------------------------------------------
# In Python 3.10+, int | None indicates an integer or None.

def find_value(numbers: list[int], target: int) -> int | None:
    for n in numbers:
        if n == target:
            return n

    return None

print(find_value([10, 20, 30], 20))
print(find_value([10, 20, 30], 40))

# Output:
# 20
# None


# ------------------------------------------------------------
# 53. FUNCTION ALIASES
# ------------------------------------------------------------
# Functions are objects and can be assigned to other variables.

def greet():
    print("Hello")

say_hello = greet

say_hello()

# Output:
# Hello


# ------------------------------------------------------------
# 54. LAMBDA WITH SORTED()
# ------------------------------------------------------------
# Sort a list of tuples according to the second element.

students = [
    ("Rishabh", 85),
    ("Aman", 92),
    ("Rahul", 78)
]

result = sorted(students, key=lambda student: student[1])

print(result)

# Output:
# [('Rahul', 78), ('Rishabh', 85), ('Aman', 92)]


# ------------------------------------------------------------
# 55. ANY() AND ALL() WITH FUNCTIONS OR GENERATORS
# ------------------------------------------------------------
# any() returns True if at least one item is truthy.
# all() returns True if every item is truthy.

numbers = [2, 4, 6, 8]

print(any(n % 2 != 0 for n in numbers))
print(all(n % 2 == 0 for n in numbers))

# Output:
# False
# True


# ------------------------------------------------------------
# 56. PARTIAL FUNCTIONS
# ------------------------------------------------------------
# functools.partial creates a new function with some arguments
# already supplied.

from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))
print(cube(3))

# Output:
# 25
# 27


# ------------------------------------------------------------
# 57. MAIN GUARD: if __name__ == "__main__"
# ------------------------------------------------------------
# This block executes when the file is run directly.
# It does not execute when the file is imported as a module
# by another Python file.

def main():
    print("Program starts here")
    print("Result:", add(10, 20))

if __name__ == "__main__":
    main()

# Output:
# Program starts here
# Result: 30
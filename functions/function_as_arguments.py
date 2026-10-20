# Function that takes two parameters and returns their sum
def function1(param1, param2):
    # Add the two parameters and return the result
    return param1 + param2

# Function that takes another function as an argument and calls it with given parameters
def function2(func, x, y):
    # Call the passed function 'func' with parameters x and y
    return func(x, y)

# Passing function1 as an argument to function2
result = function2(function1, 5, 3)  # This will call function1(5, 3) -> 5 + 3
print(result)  # Output: 8


# Example

# Function to add two numbers
def add(x, y):
    return x + y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function that takes an operation (another function) and applies it to two numbers
def calculate(operation, a, b):
    return operation(a, b)  # Calls the function passed as 'operation' with a and b

# Using 'calculate' with different operations
result1 = calculate(add, 5, 3)        # Calls add(5, 3) -> 8
result2 = calculate(multiply, 5, 3)   # Calls multiply(5, 3) -> 15

# Printing the results
print(result1)  # Output: 8
print(result2)  # Output: 15
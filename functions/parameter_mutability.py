##  Mutable objects like lists allow changes inside functions, while immutable objects like integers remain unchanged, ensuring that functions handle data as intended.

# Function to add a number to the list
def add_number(numbers):
    numbers.append(10)  # Adds 10 to the list 'numbers'

# List of numbers
my_numbers = [1, 2, 3]
add_number(my_numbers)  # Calls the function to add 10 to the list
print(my_numbers)  # Outputs: [1, 2, 3, 10] - The original list is modified

# Immutable integers

# Function to increment the number
def increment(number):
    number += 1  # Tries to modify the local variable 'number'

# Initial number
my_number = 5
increment(my_number)  # Function does not modify the original number
print(my_number)  # Outputs: 5 - The original number remains unchanged 
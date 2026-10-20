# lambda functions are small anonymous functions defined 
# using the lambda keyword. They can have any number of arguments
# but only one expression. They are commonly used for short operations or as arguments
# to higher order functions

# syntax : lambda arguments : expression

def addition(a, b) :
    return a + b


#print(addition(2, 3))

subtraction = lambda a, b : a - b

print(subtraction(4, 3))

print(type(subtraction))   ## output : <class 'function'>


#Using map() with Lambda Functions

# List of numbers
numbers = [1, 2, 3, 4]

# Using map() and a lambda function to square each number in the list
squared_numbers = list(map(lambda x: x ** 2, numbers))

# Print the result of squaring each number
print(squared_numbers)  # Output: [1, 4, 9, 16]

#Using filter() with Lambda Functions

# list of numbers
numbers = [1, 2, 3, 4, 5]

# Using filter() and a lambda function to filter even numbers from the list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Print the list of even numbers
print(even_numbers)  # Output: [2, 4]

#Using sorted() with Lambda Functions

# List of words
words = ['apple', 'banana', 'cherry']

# Sorting the list of words by their length using sorted() and a lambda function
sorted_words = sorted(words, key=lambda x: len(x))

# Print the sorted list based on word length
print(sorted_words)  # Output: ['apple', 'banana', 'cherry']

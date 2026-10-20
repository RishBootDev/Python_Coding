# lambda for giving last element of the list

last_element = lambda list: list[-1]

list = [1, 2, 3, 4]
print(last_element(list))

# list of numbers
numbers = [11, 12, 13, 14, 15]

# Use a list comprehension with a lambda function to square each number
squared_numbers = [lambda x=x: x * x for x in numbers]

# Call each lambda function in the 'squared_numbers' list and print the result
print([f() for f in squared_numbers]) 
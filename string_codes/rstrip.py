# Removing trailing spaces
my_string = "Hello, World!   "
cleaned_string = my_string.rstrip()
print(cleaned_string)  # Output: Hello, World!

# Removing specific trailing characters
another_string = "Hello, World!!!"
result = another_string.rstrip('!')
print(result)          # Output: Hello, World
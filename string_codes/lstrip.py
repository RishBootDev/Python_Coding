# Removing leading spaces
my_string = "   Hello, World!"
cleaned_string = my_string.lstrip()
print(cleaned_string)  # Output: Hello, World!

# Removing specific leading characters
another_string = "***Hello, World!"
result = another_string.lstrip('*')
print(result)          # Output: Hello, World!
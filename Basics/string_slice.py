# string[start:end:step]  # start is inclusive, end is exclusive

my_string = "Hello, World!"
full_slice = my_string[:]  # Slicing the whole string
print(full_slice)  # Output: Hello, World!

# Empty slicing 
my_string = "Hello World"
empty_slice = my_string[12:15]
print(empty_slice)  # Output: ''

my_string = "Hello World"
empty_slice = my_string[5:5]
print(empty_slice)  # Output: ''

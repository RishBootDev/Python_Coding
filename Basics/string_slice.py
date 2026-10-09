# string[start:end:step]  # start is inclusive, end is exclusive

my_string = "Hello, World!"
full_slice = my_string[:]  # Slicing the whole string
print(full_slice)  # Output: Hello, World!

# Empty slicing 
my_string = "Hello, World"
empty_slice = my_string[12:15]
print(empty_slice)  # Output: ''

empty_slice = my_string[5:5]
print(empty_slice)  # Output: ''

print(my_string[0:5])       # Outputs: 'Hello' (from index 0 to 4)
print(my_string[7:12])      # Outputs: 'World' (from index 7 to 11)
print(my_string[:5])         # Outputs: 'Hello' (start defaults to 0)
print(my_string[7:])         # Outputs: 'World!' (end defaults to the string's length)
print(my_string[::2])        # Outputs: 'Hlo ol!' (every second character)

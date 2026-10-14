# Generally the user input is captured in python using the 
# input() function

a = input("Please enter something")

# convert the input to the other data structure
a = int(input("Please enter only integers : "))

# capturing multiple inputs
first, second = input("Please enter something : ").split()
print(first)
print(second)

# capturing multiple inputs using map 
# User enters their favorite color and fruit on one line
string_inputs = input().split()      # input: Blue Mango

# User enters their favorite number and lucky number on another line
numeric_inputs = map(int, input().split())      # input: 7 21

# Assigning values
favorite_color, favorite_fruit = string_inputs[0], string_inputs[1]  
favorite_number, lucky_number = numeric_inputs  

# Displaying the results
print(f"Your favorite color is {favorite_color} and your favorite fruit is {favorite_fruit}.")
print(f"Your favorite number is {favorite_number} and your lucky number is {lucky_number}.")
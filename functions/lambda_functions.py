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

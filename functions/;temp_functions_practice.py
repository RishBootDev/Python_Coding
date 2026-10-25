
def solve(func, a , b):
    return func(a, b)

def add(a, b):
    return a + b

def mult(a, b):
    return a*b

def subtract(a, b):
    return a - b

# this is the result
addition = solve(add, a=23, b=3)
multiplication = solve(mult, a=4, b=4)

print(addition)
print(multiplication)

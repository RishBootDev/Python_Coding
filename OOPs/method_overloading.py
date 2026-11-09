# actually in python methods with same name and different parameter list are not allowed
# in a class method name is unique and no 2 methods have same name

class MyClass:
    def add(self, a, b=0, c=0):
        return a + b + c

# Creating an instance of MyClass
my_object = MyClass()

# Calling the add method with different parameter lists
result1 = my_object.add(1)
result2 = my_object.add(1, 2)
result3 = my_object.add(1, 2, 3)

print(result1)  # Output: 1
print(result2)  # Output: 3
print(result3)  # Output: 6
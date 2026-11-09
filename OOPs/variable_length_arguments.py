class MyClass:
    def add(self, *args):
        return sum(args)

# Creating an instance of MyClass
my_object = MyClass()

# Calling the add method with different numbers of arguments
result1 = my_object.add(1)
result2 = my_object.add(1, 2)
result3 = my_object.add(1, 2, 3)

print(result1)  # Output: 1
print(result2)  # Output: 3
print(result3)  # Output: 6
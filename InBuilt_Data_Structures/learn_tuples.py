# Tuples creation

my_tuple = ()

print(my_tuple)
print(type(my_tuple))

# we also have a tuple method to create tuples
numbers = tuple([1,2,3,4])
print(numbers)


# this is the mixed tuple
mixed = (1, 2, 3, 4, "Hello", 56.6)

print(mixed)

# indexing in tuple is same as that of list and string

# tuple operations
# 1. concatenation tuple

ccn = numbers + mixed
print(ccn)
print(type(ccn))  # output is :  <class 'tuple'>
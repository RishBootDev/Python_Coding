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

# 2. Replication
ppn = numbers * 3
print(ppn)

# 3. Immutable nature of Tuples
lst = [1,2,3,4,5]
print(lst)        # output : [1, 2, 3, 4, 5]
lst[0] = 99
print(lst)        # output : [99, 2, 3, 4, 5]

# but this concept is not valid in for tuple

tup = (1,2,3,4,5)

#tup[0] = 99    -> this will give error -> Traceback (most recent call last):
#  File "D:\Python_Coding\InBuilt_Data_Structures\learn_tuples.py", line 40, in <module>
#    tup[0] = 99
#    ~~~^^^
#TypeError: 'tuple' object does not support item assignment

# Packing 

packed_tuple = 1, "Hello", 3.14

print(packed_tuple)  # output : (1, 'Hello', 3.14)

# Unpacking the tuple
a, b, c = packed_tuple

print(a)
print(b)
print(c)

# unpacking with *
numbers = (1, 2, 3, 4, 5, 6)
first, *middle, last = numbers

print(first)  # output : 1
print(middle) # output : [2, 3, 4, 5]   -> this list of inner elements
print(last)   # output : 6

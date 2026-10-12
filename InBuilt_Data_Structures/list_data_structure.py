# lists are ordered , mutable collection of items 
# they can contain items of different types as well

list = []

print(type(list))

# elements in the list
names = ["Rishabh", "Rishi", "Rajesh"]

print(names)

# mixed list
m = [1, 2, 3, 4, "Rishabh"]

# accessing list elements
temp = [1, 2, 3, 4, 4, 5, 6]
print(temp[0])
print(temp[1])
print(temp[-1])

# slicing list
print(temp[1:])
print(temp[1:4])
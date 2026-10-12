# iterating with index

fruits = ["apple", "banana", "mango", "pears", "grapes"]

for idx, fruit in enumerate(fruits):
    print(idx, fruit)

# list comprehension

list = []
for x in range(10):
    list.append(x**2)

print(list)

temp = [x**2 for x in range(10)]

print(temp)


# the syntax of the list comprehension

# basic syntax [expression  for item in iterable]

square = [num ** 2 for num in range(10)]
print(square)

# with conditional logic  [expression    for item in iterable    if condition]

even_square = [num ** 2 for num in range(10) if num % 2 == 0]
print(even_square)

# Nested list comprehensions  [expression   for item1 in iterable1  for item2 in iterable2]

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

pair = [[i, j] for i in list1 for j in list2]
print(pair)


## list comprehension with function calls
words = ["hello", "world", "python", "list", "comprehension"]
lengths = [len(word) for word in words]
print(lengths)    # output will be : [5, 5, 6, 4, 13]

## All the types of list comprehension examples in python 

# 1. BASIC LIST COMPREHENSION

arr = [i for i in range(5)]
print(arr)  # [0, 1, 2, 3, 4]

arr = [i for i in range(1, 11)]
print(arr)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

arr = [i * i for i in range(1, 6)]
print(arr)  # [1, 4, 9, 16, 25]

arr = [i ** 3 for i in range(1, 6)]
print(arr)  # [1, 8, 27, 64, 125]

arr = [i * 2 for i in range(1, 6)]
print(arr)  # [2, 4, 6, 8, 10]

arr = list(range(1, 6))
print(arr)  # [1, 2, 3, 4, 5]


# 2. LIST COMPREHENSION WITH IF CONDITION

arr = [i for i in range(1, 11) if i % 2 == 0]
print(arr)  # [2, 4, 6, 8, 10]

arr = [i for i in range(1, 11) if i % 2 != 0]
print(arr)  # [1, 3, 5, 7, 9]

arr = [i for i in range(1, 11) if i > 5]
print(arr)  # [6, 7, 8, 9, 10]

arr = [i for i in range(1, 21) if i % 3 == 0]
print(arr)  # [3, 6, 9, 12, 15, 18]

nums = [-5, 3, -2, 8, 0, 7]
arr = [i for i in nums if i > 0]
print(arr)  # [3, 8, 7]

arr = [i for i in nums if i < 0]
print(arr)  # [-5, -2]

arr = [i for i in range(1, 31) if i % 2 == 0 and i % 3 == 0]
print(arr)  # [6, 12, 18, 24, 30]


# 3. LIST COMPREHENSION WITH IF-ELSE

arr = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 6)]
print(arr)  # ['Odd', 'Even', 'Odd', 'Even', 'Odd']

nums = [-3, 5, -1, 8, -7]
arr = [i if i > 0 else 0 for i in nums]
print(arr)  # [0, 5, 0, 8, 0]

marks = [35, 80, 22, 67, 90]
arr = ["Pass" if m >= 40 else "Fail" for m in marks]
print(arr)  # ['Fail', 'Pass', 'Fail', 'Pass', 'Pass']

nums = [-5, 3, -8, 2]
arr = [i if i >= 0 else -i for i in nums]
print(arr)  # [5, 3, 8, 2]

arr = ["Positive" if i > 0 else "Negative" if i < 0 else "Zero"
       for i in [-3, 0, 5]]
print(arr)  # ['Negative', 'Zero', 'Positive']


# 4. STRING LIST COMPREHENSION

arr = [ch.upper() for ch in "python"]
print(arr)  # ['P', 'Y', 'T', 'H', 'O', 'N']

arr = [word.lower() for word in ["HELLO", "WORLD"]]
print(arr)  # ['hello', 'world']

arr = [ch for ch in "programming" if ch in "aeiou"]
print(arr)  # ['o', 'a', 'i']

arr = [ch for ch in "cat" if ch not in "aeiou"]
print(arr)  # ['c', 't']

text = "PyTHon"
arr = [ch for ch in text if ch.isupper()]
print(arr)  # ['P', 'T', 'H']

text = "a1b2c3"
arr = [ch for ch in text if ch.isdigit()]
print(arr)  # ['1', '2', '3']

words = ["Java", "Python", "C++"]
arr = [len(word) for word in words]
print(arr)  # [4, 6, 3]

words = ["Java", "Python", "C++", "Spring"]
arr = [word for word in words if len(word) > 4]
print(arr)  # ['Python', 'Spring']


# 5. LIST COMPREHENSION ON AN EXISTING LIST

nums = [1, 2, 3, 4, 5]

arr = [i * i for i in nums]
print(arr)  # [1, 4, 9, 16, 25]

arr = [i * 2 for i in nums]
print(arr)  # [2, 4, 6, 8, 10]

arr = [i for i in nums if i > 3]
print(arr)  # [4, 5]

arr = [i * i for i in nums if i % 2 == 0]
print(arr)  # [4, 16]

words = ["Java", "Python", "Spring"]
arr = [word[0] for word in words]
print(arr)  # ['J', 'P', 'S']

words = ["Java", "", "Python", "", "C++"]
arr = [word for word in words if word]
print(arr)  # ['Java', 'Python', 'C++']


# 6. NESTED LIST COMPREHENSION

matrix = [[1, 2], [3, 4], [5, 6]]
arr = [num for row in matrix for num in row]
print(arr)  # [1, 2, 3, 4, 5, 6]

arr = [num for row in matrix for num in row if num % 2 == 0]
print(arr)  # [2, 4, 6]

arr = [(i, j) for i in range(2) for j in range(2)]
print(arr)  # [(0, 0), (0, 1), (1, 0), (1, 1)]

arr = [i * j for i in range(1, 4) for j in range(1, 4)]
print(arr)  # [1, 2, 3, 2, 4, 6, 3, 6, 9]

matrix = [[0 for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr = [matrix[i][i] for i in range(3)]
print(arr)  # [1, 5, 9]

arr = [row[1] for row in matrix]
print(arr)  # [2, 5, 8]


# 7. MULTIPLE CONDITIONS

arr = [i for i in range(1, 16) if i > 5 and i % 2 == 0]
print(arr)  # [6, 8, 10, 12, 14]

arr = [i for i in range(1, 16) if i % 2 == 0 or i % 3 == 0]
print(arr)  # [2, 3, 4, 6, 8, 9, 10, 12, 14, 15]

words = ["apple", "ant", "banana", "avocado"]
arr = [word for word in words if len(word) > 3 and word.startswith("a")]
print(arr)  # ['apple', 'avocado']

arr = [i for i in range(1, 21) if 5 <= i <= 10]
print(arr)  # [5, 6, 7, 8, 9, 10]


# 8. USING BUILT-IN FUNCTIONS

nums = [1, 2, 3, 4, 5]
arr = [str(i) for i in nums]
print(arr)  # ['1', '2', '3', '4', '5']

nums = ["10", "20", "30"]
arr = [int(i) for i in nums]
print(arr)  # [10, 20, 30]

nums = [1.234, 2.567, 3.891]
arr = [round(i, 2) for i in nums]
print(arr)  # [1.23, 2.57, 3.89]

nums = [-10, -5, 3, 8]
arr = [abs(i) for i in nums]
print(arr)  # [10, 5, 3, 8]

words = ["Java", "Python", "C++"]
arr = [(i, word) for i, word in enumerate(words)]
print(arr)  # [(0, 'Java'), (1, 'Python'), (2, 'C++')]

names = ["Aman", "Riya", "Raj"]
marks = [80, 90, 75]
arr = [(name, mark) for name, mark in zip(names, marks)]
print(arr)  # [('Aman', 80), ('Riya', 90), ('Raj', 75)]


# 9. SET AND DICTIONARY COMPREHENSION

nums = [1, 2, 2, 3, 3, 4]
result = {i * i for i in nums}
print(sorted(result))  # [1, 4, 9, 16] (sets are unordered)

result = {i: i * i for i in range(1, 5)}
print(result)  # {1: 1, 2: 4, 3: 9, 4: 16}

result = {i: i * i for i in range(1, 11) if i % 2 == 0}
print(result)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

data = {"a": 1, "b": 2, "c": 3}
result = {value: key for key, value in data.items()}
print(result)  # {1: 'a', 2: 'b', 3: 'c'}


# 10. ADVANCED EXAMPLES FOR DSA

nums = [1, 2, 2, 3, 1, 4]
seen = set()
result = [x for x in nums if x not in seen and not seen.add(x)]
print(result)  # [1, 2, 3, 4]

s = "abc"
result = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
print(result)  # ['a', 'ab', 'abc', 'b', 'bc', 'c']

nums = [1, 2, 3]
result = [nums[i:j] for i in range(len(nums)) for j in range(i + 1, len(nums) + 1)]
print(result)  # [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]

nums = [1, 2, 3, 4]
result = [(x, y) for x in nums for y in nums if x + y == 5]
print(result)  # [(1, 4), (2, 3), (3, 2), (4, 1)]

matrix = [[1, 2, 3], [4, 5, 6]]
result = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
print(result)  # [[1, 4], [2, 5], [3, 6]]

matrix = [[1, 5, 3], [9, 2, 4], [6, 8, 7]]
result = [max(row) for row in matrix]
print(result)  # [5, 9, 8]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [sum(row) for row in matrix]
print(result)  # [6, 15, 24]

a = [1, 2]
b = ["A", "B"]
result = [(x, y) for x in a for y in b]
print(result)  # [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]


# 11. NORMAL FOR LOOP VS LIST COMPREHENSION

result = []
for i in range(1, 6):
    result.append(i * i)

print(result)  # [1, 4, 9, 16, 25]

result = [i * i for i in range(1, 6)]
print(result)  # [1, 4, 9, 16, 25]


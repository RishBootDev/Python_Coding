# the syntax of the list comprehension

# basic syntax [expression  for item in iterable]

square = [num ** 2 for num in range(10)]
print(square)

# with conditional logic  [expression    for item in iterable    if condition]

even_square = [num ** 2 for num in range(10) if num % 2 == 0]
print(even_square)
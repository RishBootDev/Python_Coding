# Slicing of list
arr = [10, 20, 30, 40, 50, 60]

# 1. Basic slicing
print(arr[0:3])       # [10, 20, 30]
print(arr[1:4])       # [20, 30, 40]
print(arr[2:5])       # [30, 40, 50]
print(arr[0:6])       # [10, 20, 30, 40, 50, 60]
print(arr[0:1])       # [10]
print(arr[3:4])       # [40]
print(arr[4:4])       # []
print(arr[4:2])       # []

# 2. Omitting start or stop
print(arr[:3])        # [10, 20, 30]
print(arr[:4])        # [10, 20, 30, 40]
print(arr[2:])        # [30, 40, 50, 60]
print(arr[4:])        # [50, 60]
print(arr[:])         # [10, 20, 30, 40, 50, 60]
print(arr[0:])        # [10, 20, 30, 40, 50, 60]
print(arr[:0])        # []

# 3. Negative indexing
print(arr[-1])        # 60
print(arr[-2])        # 50
print(arr[-3])        # 40
print(arr[-3:])       # [40, 50, 60]
print(arr[:-1])       # [10, 20, 30, 40, 50]
print(arr[:-2])       # [10, 20, 30, 40]
print(arr[-4:-1])     # [30, 40, 50]
print(arr[-5:-2])     # [20, 30, 40]
print(arr[-4:])       # [30, 40, 50, 60]
print(arr[-6:])       # [10, 20, 30, 40, 50, 60]
print(arr[-6:-3])     # [10, 20, 30]

# 4. Slicing with positive step
print(arr[::1])       # [10, 20, 30, 40, 50, 60]
print(arr[::2])       # [10, 30, 50]
print(arr[::3])       # [10, 40]
print(arr[1::2])      # [20, 40, 60]
print(arr[::4])       # [10, 50]
print(arr[1:5:2])     # [20, 40]
print(arr[0:6:2])     # [10, 30, 50]
print(arr[1:6:3])     # [20, 50]
print(arr[2:6:2])     # [30, 50]
print(arr[0:5:1])     # [10, 20, 30, 40, 50]

# 5. Reversing with negative step
print(arr[::-1])      # [60, 50, 40, 30, 20, 10]
print(arr[::-2])      # [60, 40, 20]
print(arr[5:2:-1])    # [60, 50, 40]
print(arr[5:1:-1])    # [60, 50, 40, 30]
print(arr[4:0:-1])    # [50, 40, 30, 20]
print(arr[3::-1])     # [40, 30, 20, 10]
print(arr[:2:-1])     # [60, 50, 40]
print(arr[-1::-1])    # [60, 50, 40, 30, 20, 10]
print(arr[-2::-1])    # [50, 40, 30, 20, 10]
print(arr[-1:-4:-1])  # [60, 50, 40]

# 6. Out-of-range indices
print(arr[0:100])     # [10, 20, 30, 40, 50, 60]
print(arr[10:])       # []
print(arr[-100:3])    # [10, 20, 30]
print(arr[2:100])     # [30, 40, 50, 60]
print(arr[-100:100])  # [10, 20, 30, 40, 50, 60]
print(arr[100:200])   # []
print(arr[100:0:-1])  # [60, 50, 40, 30, 20, 10]

# 7. Extracting individual elements as lists
print(arr[2:3])       # [30]
print(arr[2:4])       # [30, 40]
print(arr[2:2])       # []
print(arr[2:])        # [30, 40, 50, 60]

# 8. List of strings
names = ["Aman", "Riya", "Raj", "Neha", "Vikram"]

print(names[1:4])     # ['Riya', 'Raj', 'Neha']
print(names[:2])      # ['Aman', 'Riya']
print(names[2:])      # ['Raj', 'Neha', 'Vikram']
print(names[::-1])    # ['Vikram', 'Neha', 'Raj', 'Riya', 'Aman']
print(names[::2])     # ['Aman', 'Raj', 'Vikram']

# 9. Copying a list using slicing
temp = arr[:]
print(temp)           # [10, 20, 30, 40, 50, 60]

# 10. Replacing elements using slice assignment
arr = [10, 20, 30, 40, 50, 60]
arr[1:3] = [99, 88]
print(arr)            # [10, 99, 88, 40, 50, 60]

# 11. Deleting elements using slicing
arr = [10, 20, 30, 40, 50, 60]
del arr[1:4]
print(arr)            # [10, 50, 60]

# 12. Slicing with a negative step and negative indices
arr = [10, 20, 30, 40, 50, 60]
print(arr[-2:-5:-1])  # [50, 40, 30]
print(arr[-3:-6:-1])  # [40, 30, 20]
print(arr[-2::-2])    # [50, 30, 10]
print(arr[:-4:-1])    # [60, 50, 40]

# 13. Step cannot be zero
# print(arr[::0])     # ValueError: slice step cannot be zero
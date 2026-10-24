## some common exceptions in python 
# 1. ZeroDivisionError
# 2. FileNotFoundError
# 3. ValueError
# 4. TypeError

# in python to handle the exceptions gracefully we use try - except block

try:
   # a = b 
    result = 12/0
except NameError as ex:
    print(ex)

except ZeroDivisionError as ex:
    print(ex)



# all the exceptions in python are derived from this class Exception 

try:
    result = 2/0

except Exception as ex:
    print(ex)

# try , except and else block

try:
    num = int(input("Please enter the number:  "))
    result = 10/num
except ValueError as ex:
    print("It is not a valid number")
except ZeroDivisionError as ex:
    print("You can't divide by zero")
except Exception as ex:
    print(ex)
else:
    print(f"the result is {result}")



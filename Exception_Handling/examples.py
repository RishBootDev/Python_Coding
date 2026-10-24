# try, except, else , finally blocks

try:
	number = int(input("Enter a number: "))
	result = 10 / number
except ValueError:
	print("Please enter a valid integer.")
except ZeroDivisionError:
	print("Cannot divide by zero.")
else:
	print(f"Result: {result}")
finally:
	print("Execution finished.")


# File handling with exception handling
filename = input("Enter the file path to read: ")

try:
	with open(filename, "r", encoding="utf-8") as file:
		contents = file.read()
except FileNotFoundError:
	print("The file was not found.")
except PermissionError:
	print("You do not have permission to read this file.")
except OSError as error:
	print(f"An error occurred while reading the file: {error}")
else:
	print("File contents:")
	print(contents)
finally:
	print("File handling finished.")

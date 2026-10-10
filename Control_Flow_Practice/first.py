##Write a program that asks the user to input a number and prints whether the number is positive.

num = int(input("Please enter the number"))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else :
    print("Zero")
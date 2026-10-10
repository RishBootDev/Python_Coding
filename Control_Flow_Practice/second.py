## Write a program that asks the user to input a number and prints whether the number is positive and even, positive and odd, or negative.

num = int(input("Please enter the number : "))

if num > 0:
    print("Positive")
    if num % 2 == 0:
        print("Even")
    else :
        print("Odd")

else :
    print("Negative")
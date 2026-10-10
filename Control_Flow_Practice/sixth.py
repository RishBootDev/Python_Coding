# Write a program that asks the user to input numbers until they input 0. The program should print the sum of all the input numbers.

sum = 0
while True:
    num = int(input("Please enter the number : "))
    if(num == 0):
        break
    else :
        sum += num

print("the sum of the numbers is ", sum)
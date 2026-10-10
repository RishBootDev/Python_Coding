# sum of digits of a number input

n = int(input("Enter a number: "))
sum = 0

while n > 0:
    digit = n % 10
    sum += digit
    n //= 10

print("Sum of digits:", sum)
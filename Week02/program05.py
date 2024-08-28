# Write a program to find the sum of digits of a supplied integer.

num = int(input("Enter any number :"))

temp = num
sum = 0
while temp > 0:
    sum += temp % 10
    temp //= 10

print(f"Sum of digit of {num} is : {sum}")

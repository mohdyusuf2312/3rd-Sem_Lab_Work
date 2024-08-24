# Write a program to check if the given number is a palindrome number or not. 
import math
num = int(input("Enter any number : "))
temp = num
rev = 0
last = 0

while(temp > 0):
    last = temp % 10
    rev = (rev * 10) + last
    temp //= 10

if(num == rev):
    print(f"{num} is palindrome.")
else:
    print(f"{num} is not a palindrome.")
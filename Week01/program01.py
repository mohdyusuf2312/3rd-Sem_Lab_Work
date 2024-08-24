# Write a program to find product of two usersupplied integers and if the product
# is equal to or lower than 5000 then return sum of the two numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def check(num1, num2) :
    if((num1*num2) >= 5000):
        return num1 + num2
    return num1 * num2

print(check(num1, num2))
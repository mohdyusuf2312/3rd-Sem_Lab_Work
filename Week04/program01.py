'''
Write a program to create function cal_sum_sub() such that it can accept two
variables and calculate addition and subtraction. Also, it must return both
addition and subtraction in a single return call
'''

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))


def cal_sum_sub(num1, num2):
    sum = num1 + num2
    sub = num1 - num2
    return sum,sub

sum, sub = cal_sum_sub(num1, num2)

print(f"The sum of {num1} and {num2} is : {sum}")
print(f"The difference of {num1} and {num2} is : {sub}")

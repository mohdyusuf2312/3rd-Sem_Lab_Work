# Write a program to use the loop to find the factorial of a given number.

def factorial(num):
    '''returns factorial of a number'''
    if num<0:
        return -1
    if num==0 or num==1:
        return 1
    
    fact=1
    for i in range(1,num+1):
        fact*=i
    
    return fact

num = int(input("Enter a number whose factorial you want : "))
print(f"Factorial of {num} is :{factorial(num)}")
# Write a program to display all prime numbers within a range.

def is_prime(n):
    '''return true if a number is prime'''
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def display_prime(start,end):
    '''Display all prime between a range provided'''
    for num in range(start,end+1):
        if is_prime(num):
            print(num)
        
        
num1=int(input("Enter the start of the prime check range:"))
num2=int(input("Enter the end of the prime check range:"))

display_prime(num1,num2)
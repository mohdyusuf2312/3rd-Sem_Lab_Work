# Write a program to print sum of first 10 numbers.

n = 1
sum = 0

while(n <= 10):
    num = int(input(f"Enter element {n} : "))
    sum += num
    n += 1
print(f"The sum of first 10 element is {sum}")
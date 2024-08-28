# Write a program to count the total number of digits in a number using a while loop.

num = input("Enter your number : ")
# print(len(num))
temp = int(num)
count = 0
while temp > 0:
    if temp :
        temp //= 10
        count+=1

print(f"Total number of digits in {num} are : {count}")
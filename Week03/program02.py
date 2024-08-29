'''
Write a program to print the following start pattern using the for loop:
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(4, 0, -1):
    for j in range(i, 0, -1):
        print("*", end=" ")
    print()

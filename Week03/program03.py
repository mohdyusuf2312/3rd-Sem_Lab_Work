# Write a program to print characters from a string which are present at an even index numbers.

str = str(input("Enter your string: "))

for i in range(len(str)):
    if i % 2 == 0:
        print(str[i])
# Write a program to Iterate the supplied list of 20 numbers by the user and print
# only those numbers which are divisible by 5.

list = []
print("Enter a list of 20 elements : ")
for i in range(20):
    num = int(input(f"Enter element {i+1}: "))
    list.append(num)

for i in list:
    if(i % 5 == 0):
        print(i)
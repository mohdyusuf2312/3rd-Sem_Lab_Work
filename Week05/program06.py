print("Write a program to create a NumPy array and sort it based on the following cases:\nCase 1: Sort the array by the second row.\nCase 2: Sort the array by the second column.\n")
import numpy as np

rows=int(input("Enter the number of rows : "))
cols=int(input("Enter the number of columns : "))

array=[]

print("Enter the elements row-wise (separated by spaces):")
for i in range(rows):
    elements=list(map(int, input().split()))
    array.append(elements)

np_array=np.array(array)

print("The numpy array looks like this : ")
print()
print(np_array)
print()

indices=np.argsort(np_array[1])

print()
print("The array sorted by second row : ")
sorted_by_row = np_array[:, indices]

print(sorted_by_row)

print()

indexCol=np.argsort(np_array[:,1])

sortedByCol=np_array[indexCol]

print("The array sorted by second column : ")
print(sortedByCol)
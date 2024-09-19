print("\nWrite a program to create a NumPy array and return an array of odd rows and even columns from the NumPy array\n")

import numpy as np


def get_even_and_odd_arr(array):
    result=array[1::2,::2]
    return result

def get_an_array():
    rows=int(input("Enter the numbers of rows: "))
    cols=int(input("Enter the numbers of cols: "))

    elements=[]

    print(f"Enter the element for  {rows}X{cols} array : ")
    for i in range(rows):
        row=[]
        for j in range(cols):
            element=int(input(f"Enter the element for position {i+1}{j+1}: "))
            row.append(element)
        elements.append(row)

    array=np.array(elements)
    return array

array=get_an_array()
print("original array: ")
print(array)

result=get_even_and_odd_arr(array)
print("Even Odd Array: ")
print(result)

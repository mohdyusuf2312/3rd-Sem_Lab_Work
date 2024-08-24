# Write a program to calculate the cube of all numbers from 1 to a given number

def cal_cube(num) -> None:
    '''returns list of cubes from 1 to till num'''
    
    list=[]
    for i in range(1,num+1):
        cube=pow(i,3)
        list.append(cube)
    return list

n=int(input("Enter number till cubes you want ? : "))
result=cal_cube(n)
print(f"Cubes of number from 1 till {n} are ",*result)
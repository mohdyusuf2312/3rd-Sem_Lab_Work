print("\nGiven two lists of numbers, write a program to create a new list that contains odd numbers from the first list and even numbers from the second list.\n")

def odd_even_list(l1,l2):
    result=[]
    for i in l1:
        if i%2!=0 :
            result.append(i)
    for j in l2:
        if j%2==0:
            result.append(j)
    return result


list1=input("Enter the first list (comma-sep values): ").split(',')
list2=input("Enter the first list (comma-sep values): ").split(',')

list1=[int(item.strip()) for item in list1]
list2=[int(item.strip()) for item in list2]


new_list=odd_even_list(list1,list2)
print(f"New list is ",new_list)
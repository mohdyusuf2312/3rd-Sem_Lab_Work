print("\nWrite a program to count the number of occurrences of the item 50 in the tuple tp1 = (50, 10, 60, 70, 50).\n")

def tuple_count(tuple,n):
    '''returns number count occurence in a tuple'''
    count=0
    for i in tuple:
        if n==i:
            count+=1
        
    return count

t=(50,10,60,50,70,50,50)
print(f"50 occurs {tuple_count(t,50)} times in tuple.")
print()
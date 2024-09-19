'''
Given a two Python list. Write a program to iterate both lists simultaneously
and display items from list 1 in original order and items from list 2 in reverse
order.
'''

list1 = [12, 55, 56, 145, 51, 8, 99]
list2 = [2, 45, 98, 63, 45, 15]
# for i in range(len(max(len(list1, list2)))):
list1 = list1[::-1]
print(list1)
print(list2)
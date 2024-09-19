print("\nWrite a program to pick a random character from a given string supplied by the user.\n")

import random
def pick_random_char(str,l):

    '''returns random char from the string'''
    index=random.randint(0,l)
    return str[index]


str=input("Enter the string: ")
l=len(str)
print(f"Random char from the string [{str}] is {pick_random_char(str,l)}")
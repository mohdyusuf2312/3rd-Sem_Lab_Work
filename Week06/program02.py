'''
Write a Python program to create a Python dictionary (the dictionary type). 
Add three names and their phone numbers in the dictionary. The names should 
act as a keys and phones as their values. Then ask the user a name and print its 
corresponding phone number. 
'''

dict = {
    "yusuf" : 9084662330,
    "faizan" : 9084662331,
    "shadab" : 9084662332,
    "farhan" : 9084662333,
    "shuja" : 9084662334,
}

name = input("Enter name : ")
print(f"Phone number of {name} is {dict[name]}")

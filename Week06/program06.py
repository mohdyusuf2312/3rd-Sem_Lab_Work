'''
Write a program to accept a string and display the following: 
a. Number of uppercase characters 
b. Numbers of lowercase characters 
c. Total number of alphabets 
d. Number of digits
'''

# Function to analyze the string
def analyze_string(input_string):
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    alphabet_count = 0
    
    # Loop through each character in the string
    for char in input_string:
        if char.isupper():
            uppercase_count += 1
            alphabet_count += 1
        elif char.islower():
            lowercase_count += 1
            alphabet_count += 1
        elif char.isdigit():
            digit_count += 1
    
    # Display the results
    print(f"Number of uppercase characters: {uppercase_count}")
    print(f"Number of lowercase characters: {lowercase_count}")
    print(f"Total number of alphabets: {alphabet_count}")
    print(f"Number of digits: {digit_count}")

# Input from the user
user_input = input("Enter a string: ")

# Call the function
analyze_string(user_input)

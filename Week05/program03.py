print("\nWrite a program to generate a random password that meets the following conditions:\nPassword length must be 10 characters long.\nIt must contain at least 2 uppercase letters, 1 digit, and 1 special symbol.\n")

import random
import string

def generate_password():
    '''Generate a random password with specific conditions'''
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_symbols = string.punctuation
    

    password_chars = [
        random.choice(uppercase_letters) for _ in range(2) 
    ] + [
        random.choice(digits) for _ in range(1) 
    ] + [
        random.choice(special_symbols) for _ in range(1)  
    ]
    

    remaining_chars = 10 - len(password_chars)
    all_chars = uppercase_letters + digits + special_symbols + string.ascii_lowercase
    password_chars += random.choices(all_chars, k=remaining_chars)
    
    random.shuffle(password_chars)
    

    password = ''.join(password_chars)
    return password

print("Generated password:", generate_password())

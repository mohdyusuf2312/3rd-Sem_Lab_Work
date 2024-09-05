'''
Write a program that inputs a main string and then creates an encrypted string 
by embedding a short symbol-based string after each character. The program 
should also be able to produce the decrypted string from encrypted string. 
'''

# Function to encrypt the string
def encrypt_string(main_string, symbol_string):
    encrypted_string = ""
    
    # Embed the symbol string after each character in the main string
    for char in main_string:
        encrypted_string += char + symbol_string
    
    return encrypted_string

# Function to decrypt the string
def decrypt_string(encrypted_string, symbol_string):
    decrypted_string = ""
    
    # Remove the symbol string after each character in the encrypted string
    for i in range(0, len(encrypted_string), len(symbol_string) + 1):
        decrypted_string += encrypted_string[i]
    
    return decrypted_string

# Input the main string and the symbol string for embedding
main_string = input("Enter the main string: ")
symbol_string = input("Enter the symbol-based string (e.g., #@!): ")

# Encrypt the string
encrypted = encrypt_string(main_string, symbol_string)
print(f"Encrypted string: {encrypted}")

# Decrypt the string
decrypted = decrypt_string(encrypted, symbol_string)
print(f"Decrypted string: {decrypted}")

# Input string
input_str = input("Enter a string containing both letters and numbers: ")

# Initialize lists
L1 = []  # List for numbers
L2 = []  # List for alphabets

# Iterate through each character in the string
for char in input_str:
    if char.isdigit():  # Check if the character is a digit
        L1.append(char)
    elif char.isalpha():  # Check if the character is an alphabet
        L2.append(char)

# Output the lists
print("List of numbers (L1):", L1)
print("List of alphabets (L2):", L2)

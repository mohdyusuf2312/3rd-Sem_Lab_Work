# Function to find the alphabet(s) with the maximum number of instances
def find_max_alphabets(filename):
    # Initialize a dictionary to count occurrences of each alphabet
    alphabet_count = {}

    # Open and read the file
    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                if char.isalpha():  # Check if the character is an alphabet
                    char = char.lower()  # Make it case-insensitive
                    if char in alphabet_count:
                        alphabet_count[char] += 1
                    else:
                        alphabet_count[char] = 1

    # Find the maximum count
    max_count = max(alphabet_count.values())

    # Find all alphabets that have the maximum count
    max_alphabets = [char for char, count in alphabet_count.items() if count == max_count]

    return max_alphabets, max_count

# File path
filename = '.\\3rd-Sem_Lab_Work\\Week09\\5data.txt'  # Replace with the path to your file

# Call the function
max_alphabets, max_count = find_max_alphabets(filename)

# Output the result
print(f"Alphabet(s) with the most occurrences: {', '.join(max_alphabets)} (appears {max_count} times)")

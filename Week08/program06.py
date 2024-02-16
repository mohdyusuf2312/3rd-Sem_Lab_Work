# Function to count vowels in the file
def find_max_vowel(filename):
    # Define vowels
    vowels = 'aeiouAEIOU'
    # Initialize a dictionary to store vowel counts
    vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    # Open and read the file
    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                if char.lower() in vowel_count:
                    vowel_count[char.lower()] += 1

    # Find the vowel with the maximum instances
    max_vowel = max(vowel_count, key=vowel_count.get)
    max_count = vowel_count[max_vowel]

    return max_vowel, max_count

# File path
filename = '.\data.txt'  # Replace 'data.txt' with the path to your file

# Call the function
max_vowel, max_count = find_max_vowel(filename)

# Output the result
print(f"The vowel '{max_vowel}' appears the most with {max_count} instances.")

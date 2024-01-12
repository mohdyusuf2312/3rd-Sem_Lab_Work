from collections import Counter

# Function to find and replace the word(s) with maximum instances
def replace_max_word(filename):
    # Read the file
    with open(filename, 'r') as file:
        text = file.read()
    
    # Split the text into words and count occurrences
    words = text.split()
    word_counts = Counter(words)
    
    # Find the word(s) with the maximum occurrences
    max_count = max(word_counts.values())
    max_words = [word for word, count in word_counts.items() if count == max_count]
    
    # Replace each max word with "Aligarh"
    for word in max_words:
        text = text.replace(word, "Aligarh")
    
    # Write the modified text back to the file
    with open(filename, 'w') as file:
        file.write(text)
    
    print(f"Replaced word(s) {max_words} with 'Aligarh' in the file.")

# Example usage
filename = '.\\3rd-Sem_Lab_Work\\Week10\\sample.txt'
replace_max_word(filename)

# Function to create two lists
def create_two_lists(original_list):
    # Sort the original list
    original_list.sort()

    # Split the list into two equal halves
    mid_index = len(original_list) // 2
    list1 = original_list[:mid_index]  # First half
    list2 = original_list[mid_index:]  # Second half

    return list1, list2

# Input list of distinct integers from the user
user_input = input("Enter distinct integers separated by spaces: ")

# Convert input string to a list of integers
original_list = list(map(int, user_input.split()))

# Check if the list has an even number of elements
if len(original_list) % 2 != 0:
    print("The list does not have an even number of elements.")
else:
    # Create two lists
    list1, list2 = create_two_lists(original_list)

    # Display the two lists
    print("List 1 (smaller elements):", list1)
    print("List 2 (larger elements):", list2)

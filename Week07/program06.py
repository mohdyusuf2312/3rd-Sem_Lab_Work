'''
Consider two files having some lines of statements. Write a Python program to swap 
content present at middle line of first file with the content of last line of the second 
file. (Note: First file contains odd numbers of lines of statement)
'''
def swap_middle_and_last(file1, file2):
    try:
        # Reading the content of the first file
        with open(file1, 'r') as f1:
            lines1 = f1.readlines()
        
        # Reading the content of the second file
        with open(file2, 'r') as f2:
            lines2 = f2.readlines()

        # Finding the middle index of the first file
        middle_index = len(lines1) // 2  # Assumes the number of lines in file1 is odd
        
        # The last line of the second file
        last_index = len(lines2) - 1
        
        # Swapping the middle line of file1 with the last line of file2
        lines1[middle_index], lines2[last_index] = lines2[last_index], lines1[middle_index]
        
        # Writing the modified content back to the first file
        with open(file1, 'w') as f1:
            f1.writelines(lines1)
        
        # Writing the modified content back to the second file
        with open(file2, 'w') as f2:
            f2.writelines(lines2)
        print("swaping is done.")

    except():
        print("Something went wrong.")

# Example usage
file1 = 'file1.txt'
file2 = 'file2.txt'
swap_middle_and_last(file1, file2)

'''
Write a Python program having a void function that receives a 4-digit number 
and calculates the sum of squares of first 2 digits’ number and last two digits’ 
number, e.g. if 1233 is passed as argument then function should calculate 144 
+ 1089. 
'''

def sum_of_squares(num):
    # Ensure the number is 4 digits
    if 1000 <= num <= 9999:
        # Split into the first two digits and the last two digits
        first_two_digits = num // 100  # First two digits
        last_two_digits = num % 100    # Last two digits
        
        # Calculate the squares and their sum
        result = (first_two_digits ** 2) + (last_two_digits ** 2)
        
        # Print the result
        print(f"Sum of squares of {first_two_digits} and {last_two_digits} is: {result}")
    else:
        print("Please enter a 4-digit number.")

# Example usage
number = int(input("Enter a 4-digit number: "))
sum_of_squares(number)

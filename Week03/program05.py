# Write a program to remove characters from a string starting from n to last and
# return a new string. Example: remove_chars("aligarh", 3) so output must be al.

str = str(input("Enter your string: "))
number = int(input("Enter index value : "))

# print(f"Your string is : {str[number:len(str)]}")
print(f"Your string is : {str[:number-1]}")
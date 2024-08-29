# Write a function to return True if the first and last number of a given list is
# same. If numbers are different then return False.

def check(list):
    if list[0] == list[len(list)-1]:
        return True
    return False

list = [10, 15, 20, 25, 36, 25, 15, 10]

print(check(list))
# Write a Program to extract each digit from an integer in the reverse order.

num = input("Enter a number that you want to reverse:")
for i in num:
    print(i)

def reverse(num):
    temp = int(num)
    reverse = 0
    while temp > 0:
        remainder = temp % 10
        reverse = (reverse * 10) + remainder
        temp //= 10
    return reverse

print(f"Your reverse number is : {reverse(num)}")
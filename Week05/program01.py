print("\n Write a program to generate a 6-digit random secure OTP.\n")

from random import randint

def random_otp():
    return randint(100000,999999)

print(f"Six digit otp is {random_otp()}")
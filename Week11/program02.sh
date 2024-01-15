#!/bin/bash
# This script calculates the factorial of a given number

echo "Enter a number:"
read number

# Initialize variables
factorial=1
counter=$number

# Calculate factorial using a while loop
while [ $counter -gt 0 ]; do
    factorial=$((factorial * counter))
    counter=$((counter - 1))
done

echo "The factorial of $number is: $factorial"

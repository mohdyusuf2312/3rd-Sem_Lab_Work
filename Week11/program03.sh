#!/bin/bash
# This script checks if a number is positive, negative, or zero

echo "Enter a number:"
read number

# Check if the number is positive, negative, or zero
if [ "$number" -gt 0 ]; then
    echo "The number $number is positive."
elif [ "$number" -lt 0 ]; then
    echo "The number $number is negative."
else
    echo "The number is zero."
fi

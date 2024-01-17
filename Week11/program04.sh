#!/bin/bash
# This script defines and uses a simple function to greet the user

# Define a function named greet
greet() {
    # Function takes one argument, the user's name
    echo "Hello, $1! Welcome to the script."
}

# Prompt the user for their name
echo "Please enter your name:"
read name

# Call the greet function with the user's name as an argument
greet "$name"

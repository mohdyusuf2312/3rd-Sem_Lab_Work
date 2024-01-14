Step 1: ```nano check_file.sh```
Step 2: Write code:=> 
#!/bin/bash
# This script checks if a specified file exists

# Prompt the user to enter a filename
echo "Enter the filename:"
read filename

# Check if the file exists
if [ -e "$filename" ]; then
    echo "The file '$filename' exists."
else
    echo "The file '$filename' does not exist."
fi

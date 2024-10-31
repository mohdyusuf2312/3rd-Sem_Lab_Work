# !/bin/bash
# This script searches for a specific pattern in a file and displays the results.

# Prompt for file name and pattern
echo "Enter the file name to search in:"
read fileName

# Check if the file exists
if [ ! -f "$fileName" ]; then
    echo "File '$fileName' not found."
    exit 1
fi

# Prompt for the search pattern
echo "Enter the pattern to search for:"
read pattern

# Use grep to search for the pattern in the file
echo "Searching for '$pattern' in '$fileName'..."
grep "$pattern" "$fileName"

# Check if any matches were found
if [ $? -ne 0 ]; then
    echo "No matches found for '$pattern' in '$fileName'."
else
    echo "Search complete."
fi

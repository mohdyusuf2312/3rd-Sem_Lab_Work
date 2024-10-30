#!/bin/bash
# This script automates the creation of user accounts

# Check if the script is run as root (required for creating users)
if [ "$(id -u)" -ne 0 ]; then
    echo "Please run this script as root or using sudo."
    exit 1
fi

# File containing usernames (one username per line)
USERLIST="username.txt"

# Check if the user list file exists
if [ ! -f "$USERLIST" ]; then
    echo "User list file '$USERLIST' not found. Please create it with usernames (one per line)."
    exit 1
fi

# Loop through each username in the file
while IFS= read -r USERNAME || [ -n "$USERNAME" ]; do
    # Skip empty lines
    [ -z "$USERNAME" ] && continue
    
    # Check if the user already exists
    if id "$USERNAME" &>/dev/null; then
        echo "User '$USERNAME' already exists. Skipping..."
    else
        # Create the user account with a home directory and default shell
        useradd -m -s /bin/bash "$USERNAME"
        
        # Set a default password (you may want to set unique passwords or prompt for manual password entry)
        echo "$USERNAME:password" | chpasswd
        
        # Force user to change password on first login
        passwd -e "$USERNAME"
        
        echo "User '$USERNAME' has been created and is required to change password on first login."
    fi
done < "$USERLIST"

echo "User account creation completed."
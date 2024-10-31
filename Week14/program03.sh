#!/bin/bash

# Define variables
USER=$1                   # Username for managing permissions
TARGET_DIR=$2             # Target directory for setting permissions
FILES_TO_BACKUP=("/etc/passwd" "/etc/hosts" "/etc/ssh/sshd_config")  # Critical files to backup
BACKUP_DIR="/backup"      # Backup directory
TIMESTAMP=$(date +%Y%m%d_%H%M%S)  # Timestamp for backup file

# Check if USER and TARGET_DIR are provided as arguments
if [ -z "$USER" ] || [ -z "$TARGET_DIR" ]; then
  echo "Usage: $0 <username> <target_directory>"
  exit 1
fi

# Check if the target directory exists
if [ ! -d "$TARGET_DIR" ]; then
  echo "Error: Target directory $TARGET_DIR does not exist."
  exit 1
fi

# Create backup directory if it doesn't exist
if [ ! -d "$BACKUP_DIR" ]; then
  echo "Creating backup directory at $BACKUP_DIR..."
  sudo mkdir -p $BACKUP_DIR
  sudo chmod 700 $BACKUP_DIR  # Restrict permissions for security
fi

# Manage user permissions on the target directory
echo "Setting permissions for $USER on $TARGET_DIR..."
sudo chown -R $USER:$USER $TARGET_DIR
sudo chmod -R 755 $TARGET_DIR  # Set read, write, and execute permissions

# Create a backup of the critical files
echo "Creating backup of critical files..."
BACKUP_FILE="$BACKUP_DIR/backup_$TIMESTAMP.tar.gz"
sudo tar -czf $BACKUP_FILE "${FILES_TO_BACKUP[@]}"
echo "Backup saved to $BACKUP_FILE."

# Verify and list the contents of the backup file
echo "Verifying backup contents:"
tar -tf $BACKUP_FILE

# Final message
echo "User permission management and backup completed successfully."

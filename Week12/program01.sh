#!/bin/bash
# This script backs up a specified directory to a target location

# Check if source and destination directories are provided as arguments
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 source_directory destination_directory"
    exit 1
fi

SOURCE_DIR=$1
DESTINATION_DIR=$2

# Check if the source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory '$SOURCE_DIR' does not exist."
    exit 1
fi

# Check if the destination directory exists; if not, create it
if [ ! -d "$DESTINATION_DIR" ]; then
    echo "Destination directory '$DESTINATION_DIR' does not exist. Creating it..."
    mkdir -p "$DESTINATION_DIR"
fi

# Create a timestamped backup directory in the destination directory
TIMESTAMP=$(date +"%Y%m%d%H%M%S")
BACKUP_DIR="$DESTINATION_DIR/backup_$TIMESTAMP"

# Copy the source directory contents to the backup directory
cp -r "$SOURCE_DIR" "$BACKUP_DIR"

echo "Backup of '$SOURCE_DIR' completed successfully at '$BACKUP_DIR'"

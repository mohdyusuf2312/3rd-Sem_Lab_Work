#!/bin/bash

# Configuration
LOG_DIR="/var/log"                  # Directory containing the logs
ARCHIVE_DIR="/var/log/archive"       # Directory to store archived logs
ROTATE_DAYS=7                        # Age in days after which logs will be archived
DELETE_DAYS=30                       # Age in days after which logs will be deleted

# Create archive directory if it doesn't exist
if [ ! -d "$ARCHIVE_DIR" ]; then
    echo "Creating archive directory at $ARCHIVE_DIR..."
    sudo mkdir -p "$ARCHIVE_DIR"
    sudo chmod 700 "$ARCHIVE_DIR"  # Restrict permissions for security
fi

# Step 1: Rotate (archive) logs older than ROTATE_DAYS
echo "Rotating logs older than $ROTATE_DAYS days..."
find "$LOG_DIR" -type f -name "*.log" -mtime +$ROTATE_DAYS -exec bash -c '
    for log; do
        log_name=$(basename "$log")
        archive_name="${log_name}_$(date +%Y%m%d_%H%M%S).gz"
        sudo gzip -c "$log" > "$ARCHIVE_DIR/$archive_name"
        echo "Archived $log to $ARCHIVE_DIR/$archive_name"
        : > "$log"  # Truncate the original log file
    done' bash {} +

# Step 2: Delete archives older than DELETE_DAYS
echo "Deleting archived logs older than $DELETE_DAYS days..."
find "$ARCHIVE_DIR" -type f -name "*.gz" -mtime +$DELETE_DAYS -exec rm -f {} \;
echo "Old archived logs deleted."

# Log rotation summary
echo "Log rotation completed. Logs older than $ROTATE_DAYS days have been archived."
echo "Archived logs older than $DELETE_DAYS days have been deleted."

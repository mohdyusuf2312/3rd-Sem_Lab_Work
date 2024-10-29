#!/bin/bash
# This script monitors disk usage and sends an alert if usage exceeds a specified threshold

# Define the threshold percentage (e.g., 80 for 80%)
THRESHOLD=80

# Define the partition to monitor (e.g., "/")
PARTITION="/"

# Check disk usage of the specified partition
USAGE=$(df -h "$PARTITION" | awk 'NR==2 {print $5}' | sed 's/%//')

# Convert USAGE to an integer
USAGE=$(($USAGE + 0))

# If usage exceeds threshold, display an alert
if [ "$USAGE" -ge "$THRESHOLD" ]; then
    echo "ALERT: Disk usage of $PARTITION has reached $USAGE%, which is above the threshold of $THRESHOLD%."
    
    # Optional: Uncomment the next lines to send an email (configure mail settings if needed)
    # echo "Disk usage alert for $PARTITION: $USAGE% used." | mail -s "Disk Usage Alert" your_email@example.com
else
    echo "Disk usage is at $USAGE%, which is within the safe limit."
fi
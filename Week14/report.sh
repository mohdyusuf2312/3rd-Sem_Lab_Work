#!/bin/bash

# Define the output report file
REPORT_FILE="system_health_report.txt"

# Clear previous report content if it exists
> $REPORT_FILE

# Add date and time to the report
echo "System Health Report - $(date)" >> $REPORT_FILE
echo "=========================================" >> $REPORT_FILE

# CPU Usage
echo "Checking CPU Usage..." >> $REPORT_FILE
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print 100 - $8 "%"}')
echo "CPU Usage: $CPU_USAGE" >> $REPORT_FILE
echo "-----------------------------------------" >> $REPORT_FILE

# Memory Usage
echo "Checking Memory Usage..." >> $REPORT_FILE
MEMORY_USAGE=$(free -m | awk 'NR==2{printf "Memory Usage: %s/%sMB (%.2f%%)\n", $3, $2, $3*100/$2 }')
echo "$MEMORY_USAGE" >> $REPORT_FILE
echo "-----------------------------------------" >> $REPORT_FILE

# Disk Space Usage
echo "Checking Disk Space Usage..." >> $REPORT_FILE
DISK_USAGE=$(df -h | awk '$NF=="/"{printf "Disk Usage: %s/%s (%s)\n", $3, $2, $5}')
echo "$DISK_USAGE" >> $REPORT_FILE
echo "-----------------------------------------" >> $REPORT_FILE

# Network Information
echo "Checking Network Information..." >> $REPORT_FILE
IP_ADDRESS=$(hostname -I | awk '{print $1}')
echo "IP Address: $IP_ADDRESS" >> $REPORT_FILE
echo "-----------------------------------------" >> $REPORT_FILE

# Uptime
echo "Checking System Uptime..." >> $REPORT_FILE
UPTIME=$(uptime -p)
echo "System Uptime: $UPTIME" >> $REPORT_FILE
echo "=========================================" >> $REPORT_FILE

# Print completion message
echo "System health check complete. Report saved to $REPORT_FILE."

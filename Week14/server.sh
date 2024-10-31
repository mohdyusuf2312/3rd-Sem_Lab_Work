#!/bin/bash

# Update system packages
echo "Updating system packages..."
sudo apt update -y
sudo apt upgrade -y

# Install Apache
echo "Installing Apache web server..."
sudo apt install apache2 -y

# Start and enable Apache to run on boot
echo "Starting Apache server and enabling it to start on boot..."
sudo systemctl start apache2
sudo systemctl enable apache2

# Configure firewall to allow traffic on HTTP and HTTPS
echo "Configuring firewall to allow HTTP and HTTPS traffic..."
sudo ufw allow in "Apache Full"

# Create a sample HTML page
echo "Creating a sample webpage..."
echo "<!DOCTYPE html>
<html>
<head>
  <title>Welcome to Your Web Server!</title>
</head>
<body>
  <h1>Apache Web Server is up and running!</h1>
  <p>This is a test page to verify the server configuration.</p>
</body>
</html>" | sudo tee /var/www/html/index.html > /dev/null

# Restart Apache to apply changes
echo "Restarting Apache server..."
sudo systemctl restart apache2

# Output status
echo "Web server setup complete! You can visit the test page to confirm."

# Print server IP address for easy access
SERVER_IP=$(hostname -I | awk '{print $1}')
echo "Visit http://$SERVER_IP to see the test page."


# To stop: sudo systemctl stop apache2
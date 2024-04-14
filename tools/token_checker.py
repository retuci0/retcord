from colorama import Fore

import os
import requests

"""
Checks Discord tokens stored in a file, by trying to log in with them
"""

def main():
    
    os.system("title Token checker")
    print("Valid tokens will be stored to outputs/valid_tokens.txt")
    
    
    tokens_file_path = input("Path of file where tokens are stored (separated by newlines): ")
    tokens_file_path = fr"{tokens_file_path}" #fr fr no cap
    if not os.path.exists(tokens_file_path):
        exit("Invalid file path")
    
    tokens = str()
    
    
    with open(tokens_file_path, "r") as tokens_file:
        tokens = tokens_file.read()
        
        try:
            tokens = list(tokens.split("\n"))
            
        except:
            exit("Make sure the tokens are separated by newlines")
        
        tokens_file.close()
    
    
    def check_token(token):
        
        request = requests.post(
                    url = "https://discord.com/api/v6/auth/login",
                    headers = {"Authorization": token}    
        )
        
        if request.status_code == 200 or request.status_code == 202:
            print(f"{token} is a {Fore.GREEN}valid token {Fore.RESET}")
            valid_tokens_file.write(token + "\n")
        
        elif request.status_code == 429:
            print(f"{Fore.YELLOW}Rate limited {Fore.RESET}")
            check_token(token)
        
        else:
            print(f"{token} is an {Fore.RED}invalid token {Fore.RESET}")
        
    
    with open(r"outputs\valid_tokens.txt", "a") as valid_tokens_file:
        
        try:
        
            for token in tokens:
                
                check_token(token)
        
        except KeyboardInterrupt:
            valid_tokens_file.close()
            exit("Exiting the token checker...")
        
        except requests.ConnectionError:
            exit("Connection error")

if __name__ == "__main__":
    main()
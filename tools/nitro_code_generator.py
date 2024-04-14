from colorama import Fore
import os
import random
import requests
import string
import time

"""
Generates random Nitro gift codes.
"""

def main():
    
    os.system("title [Retcord] Nitro code generator")
    
    try:
        print("Press CTRL + C or close the window to stop generating codes.")

        number_of_codes = input("Number of codes to generate (leave empty to keep generating indefinitely): ")
        
        try:
            
            if number_of_codes != "".strip():
                number_of_codes = int(number_of_codes)
                
            else:
                number_of_codes = 2 ** 30
                
        except:
            
            exit("Input a valid number, dumb ass.")

        type_of_nitro = input("Type of nitro (normal / boost): ")
        
        if type_of_nitro.lower().strip() != "normal" and type_of_nitro.lower().strip() != "boost":
            
            exit("You moron.")

        for i in range(number_of_codes):
            try:
                
                if type_of_nitro == "boost":
                    code = "".join([random.choice(string.ascii_letters + string.digits) for j in range(24)])
                    
                else:
                    code = "".join([random.choice(string.ascii_letters + string.digits) for j in range(16)])

                request = requests.get(
                    f"https://discordapp.com/api/entitlements/gift-codes/{code}", 
                    timeout=10
                )
                
                if request.status_code == 200:
                    print(f"discord.gift/{code} -->{Fore.GREEN} valid{Fore.RESET}")
                    open("outputs/nitro_codes.txt", "a").write(f"{code}\n")
                    
                if request.status_code == 404:
                    print(f"discord.gift/{code} -->{Fore.RED} invalid{Fore.RESET}")

                if request.status_code == 429:
                    print(f"discord.gift/{code} -->{Fore.YELLOW} rate limited{Fore.RESET}")

            except Exception as e:
                print(f"Exception: {e}")
                time.sleep(2)
                exit()

        print(f"Finished checking {number_of_codes} codes")
        exit("Valid codes saved to outputs/nitro_codes.txt")
        
    except KeyboardInterrupt:
        exit("Exiting the Nitro code generator...")

if __name__ == "__main__":
    main()
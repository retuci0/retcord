import json

import tkinter as tk
from tkinter import font

from misc.create_widgets import create_widgets

from configs.load_configs import load_configs
from configs.load_configs import load_user_info
from configs.load_configs import load_channel_id
from configs.load_configs import load_logo


class Retcord:
    def __init__(self, master=tk.Tk()):
        
        #Welcome the user in the terminal
        print("Welcum to Retcord! I'm Retucio, you're a moron, and this is just the terminal, which I'll use for debugging.")
        
        #Window
        self.master = master
        
        x = self.master.winfo_screenwidth() // 2 - 540
        y = self.master.winfo_screenheight() // 2 - 360
        
        self.master.title("Retcord v1.7")
        self.master.geometry(f"1080x720+{x}+{y}")
        self.master.iconbitmap("assets/icons/icon.ico")
        self.master.resizable(False, False)
        self.master.protocol("WM_DELETE_WINDOW", self.close)
        
        #Font
        self.font = font.nametofont("TkDefaultFont")
        self.font.config(
            family = "Ebrima",
            size = "10",
        )

        #Base for the attributes
        self.user_id = str()
        self.username = str()
        self.configs = {
            "token": "",
            "channel_id": "",
            "bot_id": "",
            "logo": "default",
            "x-super-properties": ""
        }

        #Booleans for sending different types of requests
        self.typing = False
        self.spamming = False
        self.custom_rpc_enabled = False
        self.opening_lootboxes = False

        #Load configs from configs.json into self.configs
        load_configs(self)
        
        #Create widgets
        create_widgets(self)
        
        #Load all configs from self.configs into their respective place
        load_user_info(self)
        load_channel_id(self)
        load_logo(self)
    
        #Headers for POST requests
        self.headers = {
            #For some reason, an "x-super-properties" header is required now (just for the lootboxes tho)
            "Authorization": self.configs["token"],
            "X-Super-Properties": self.configs["x-super-properties"]
        }
        
        
    def close(self):
        """Saves all configs before closing."""
        
        json.dump(self.configs, open("configs/configs.json", "w"), indent=4)
        print("Saved configs to configs.json, exiting Retcord")
        self.master.destroy()


#Run
app = Retcord()
app.master.mainloop()
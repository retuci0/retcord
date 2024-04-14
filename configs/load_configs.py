import base64
import json
import os
import requests

from tkinter import PhotoImage

from configs.update_configs import login


def load_configs(self):
    """Loads configs from the configs.json file, and if it doesn't exists it prompts the user to log in."""
    
    #Load configs from configs.json if it exists
    if os.path.exists("configs/configs.json"):
        
        with open("configs/configs.json", "r") as f:
            
            self.configs = json.loads(f.read())
            
            print("Loaded configs from configs.json:")
            print(f"    Token: {self.configs["token"]}")
            print(f"    Channel ID: {self.configs["channel_id"] if self.configs["channel_id"] else "None"}")
            print(f"    Bot ID: {self.configs["bot_id"] if self.configs["bot_id"] else "None"}")
            print(f"    Logo: {self.configs["logo"] if self.configs["logo"] else "Default"}")
            
    #If not, prompt the user to log in   
    else:  
        login(self)
        

def load_user_info(self):
    """Gets the user ID and username from the token, and displays it to the user."""
    
    #Get the user ID from the 1st part of the token
    user_id = self.configs["token"].split(".")[0]
    self.user_id = base64.b64decode(user_id + "==").decode("utf-8")
    
    print(f"Loaded user ID: {self.user_id}")
    
    #Try to get the username from the user ID
    try:
        request = requests.get(f"https://dashboard.botghost.com/api/public/tools/user_lookup/{self.user_id}")
        response = json.loads(request.text)
        
        self.username = response["username"]
        self.login_label.config(text=f"Logged in as {self.username} ({self.user_id})")
        
    except json.decoder.JSONDecodeError:
            self.login_label.config(text=f"Failed to get username ({self.user_id})")
            print("Error: Failed to load username (json.decoder.JSONDecodeError)")
            
    else:
        self.login_label.config(text=f"Logged in as {self.username} ({self.user_id})")
        print(f"Loaded username: {self.username}")
    
    
def load_channel_id(self):
    """Loads the saved channel ID into the channel ID entry"""
    
    self.channel_id_entry.insert(0, self.configs["channel_id"])
    print(f"Loaded channel ID ({self.configs["channel_id"]})")



def load_logo(self):
    """Gets the saved logo from the saved configs and loads it into the logo label."""
    
    #Dictionary for each logo and their path
    logos = {
        "default logo": PhotoImage(file="assets/logos/default.png"),
        "nerd logo": PhotoImage(file="assets/logos/nerd.png"),
        "uwu logo": PhotoImage(file="assets/logos/uwu.png"),
        "british logo": PhotoImage(file="assets/logos/british.png")
    }
    
    current_logo = self.configs["logo"]
    new_logo = logos[current_logo]
    
    #Load the logo
    self.logo_label.config(image=new_logo)
    self.logo_label.photo = new_logo
    
    print(f"Loaded {self.configs["logo"]}")
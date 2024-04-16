import subprocess
import webbrowser

from tkinter import PhotoImage
from tkinter import ttk

from configs.update_configs import login
from configs.update_configs import update_channel_id
from configs.update_configs import change_logo

from misc.tooltips import create_tooltip
from misc.credits import show_credits

from tools import colourize_text
from tools import custom_rpc
from tools import edit_message
from tools import edited_tag
from tools import fake_invite_link
from tools import lootbox_opener
from tools import spam
from tools import fake_typer


def create_widgets(self):
    """Creates all the widgets."""

    #Current user
    self.login_label = ttk.Label(self.master, text="Logged in as: ")
    self.login_label.place(relx=0.025, rely=0.05)
    
    self.login_button = ttk.Button(self.master, text="Change", command=lambda: login(self))
    self.login_button.place(relx=0.3, rely=0.05)
    create_tooltip(self.login_button, "Log in using your Discord token.")

    #Current channel ID
    self.channel_id_label = ttk.Label(self.master, text="Channel ID:")
    self.channel_id_label.place(relx=0.025, rely=0.1)
    
    self.channel_id_entry = ttk.Entry(self.master, width=22)
    self.channel_id_entry.place(relx=0.1, rely=0.1)
    create_tooltip(self.channel_id_entry, "Insert channel ID here. Don't forget to click the update button afterwards.")
    
    self.channel_id_button = ttk.Button(self.master, text="Update", command=update_channel_id)
    self.channel_id_button.place(relx=0.25, rely=0.1)
    create_tooltip(self.channel_id_button, "Click to update the channel ID.")

    #The super cool logo
    logo_image = PhotoImage(file="assets/logos/default.png")
    
    self.logo_label = ttk.Label(self.master, image=logo_image)
    self.logo_label.photo = logo_image
    self.logo_label.place(relx=0.5, rely=0.03)
    create_tooltip(self.logo_label, "super cool logo frfr")

    #Credits
    self.credits_button = ttk.Button(self.master, text="Credits", command=lambda: show_credits(self))
    self.credits_button.place(relx=0.05, rely=0.96, anchor="center")
    create_tooltip(self.credits_button, "Credits. Just in case you wanted to read them.")

    #Retcord's GitHub repo
    self.github_button = ttk.Button(self.master, text="GitHub", command=lambda: webbrowser.open("https://github.com/retuci0/retcord"))
    self.github_button.place(relx=0.15, rely=0.96, anchor="center")
    create_tooltip(self.github_button, "Retcord's GitHub repo.")

    #My Discord
    self.discord_button = ttk.Button(self.master, text="My Discord", command=lambda: webbrowser.open("https://discordapp.com/users/806597513943056464"))
    self.discord_button.place(relx=0.25, rely=0.96, anchor="center")
    create_tooltip(self.discord_button, "My Discord, in case you wanted to contact me (I'm not that important, ik).")

    #Custom logo
    self.customize_button = ttk.Button(self.master, text="Customize logo", command=lambda: change_logo(self))
    self.customize_button.place(relx=0.01, rely=0.88)
    create_tooltip(self.customize_button, "Select one of the preset logos. If you want an actual custom one, go to the source code, in line 135 and change the path to a custom one.")

    """Tools"""
    #Type infinitely
    self.type_button = ttk.Button(self.master, text="Fake typer", command=lambda: fake_typer.main(self))
    self.type_button.place(relx=0.13, rely=0.25, anchor="center", width=200, height=50)
    create_tooltip(self.type_button, "Continously sends typing requests to the Discord API, making it look like you're always typing.")

    #Spam
    self.spam_button = ttk.Button(self.master, text="Spam", command=lambda: spam.main(self))
    self.spam_button.place(relx=0.13, rely=0.35, anchor="center", width=200, height=50)
    create_tooltip(self.spam_button, "Spams the desired message in the desired channel at the desired interval (desired).")

    #Edit a message without the (edited) tag showing up
    self.edit_button = ttk.Button(self.master, text="Discreet edit", command=lambda: edit_message.main(self))
    self.edit_button.place(relx=0.13, rely=0.45, anchor="center", width=200, height=50)
    create_tooltip(self.edit_button, "Edits a message by sending a message request with an already existing message ID, replacing the text and preventing the (edited) tag from appearing.")

    #Add color to discord text
    self.colourize_button = ttk.Button(self.master, text="Colourize text", command=lambda: colourize_text.main(self))
    self.colourize_button.place(relx=0.13, rely=0.55, anchor="center", width=200, height=50)
    create_tooltip(self.colourize_button, "Adds colour to your Discord message using ANSI colour codes.")

    #Create a fake invite link by using spoiler spam
    self.fake_link_button = ttk.Button(self.master, text="Fake invite link", command=lambda: fake_invite_link.main(self))
    self.fake_link_button.place(relx=0.13, rely=0.65, anchor="center", width=200, height=50)
    create_tooltip(self.fake_link_button, "Creates a fake invite link by using spoiler spam.")

    #Custom RPC
    self.rpc_button = ttk.Button(self.master, text="Custom RPC", command=lambda: custom_rpc.main(self))
    self.rpc_button.place(relx=0.36, rely=0.25, anchor="center", width=200, height=50)
    create_tooltip(self.rpc_button, "Sets a custom Rich Presence in Discord. Don't forget to create your own bot for this.")

    #Token bruteforcer
    self.token_bruteforce_button = ttk.Button(self.master, text="Token bruteforcer", command=lambda: subprocess.Popen(["start", "cmd", "/k", "python", "tools/token_bruteforcer.py"], shell=True))
    self.token_bruteforce_button.place(relx=0.36, rely=0.35, anchor="center", width=200, height=50)
    create_tooltip(self.token_bruteforce_button, "Tries to bruteforce a Discord token. Use at your own risk.")

    #Nitro code generator
    self.nitro_button = ttk.Button(self.master, text="Nitro code generator", command=lambda: subprocess.Popen(["start", "cmd", "/k", "python", "tools/nitro_code_generator.py"], shell=True))
    self.nitro_button.place(relx=0.36, rely=0.45, anchor="center", width=200, height=50)
    create_tooltip(self.nitro_button, "It most likely won't work. Basically joins random characters after the Discord gift link, to try and get one right.")

    #Customize where the (edited) tag will appear using the RLO (U202B+) character
    self.edited_tag_button = ttk.Button(self.master, text="Custom (edited) tag", command=lambda: edited_tag.main(self))
    self.edited_tag_button.place(relx=0.36, rely=0.55, anchor="center", width=200, height=50)
    create_tooltip(self.edited_tag_button, "Makes the (edited) tag appear anywhere you want in the message, by using the right-to-left embedding character.")

    #Basic DOS tool
    self.dos_button = ttk.Button(self.master, text="DoS attack", command=lambda: subprocess.Popen(["start", "cmd", "/k", "python", "tools/dos.py"], shell=True))
    self.dos_button.place(relx=0.36, rely=0.65, anchor="center", width=200, height=50)
    create_tooltip(self.dos_button, "Sends multiple HTTP requests per second, which might overwhelm the target's servers. This is called Denial of Service (DoS). Use at your own risk.")
    
    #Open lootboxes automatically
    self.lootbox_button = ttk.Button(self.master, text="Open lootboxes", command=lambda: lootbox_opener.main(self))
    self.lootbox_button.place(relx=0.13, rely=0.75, anchor="center", width=200, height=50)
    create_tooltip(self.lootbox_button, "Opens lootboxes for your lazy ass, so you can get that clown avatar decoration that suits you so well.")
    
    #Check tokens by trying to log in with them
    self.token_checker_button = ttk.Button(self.master, text="Token checker", command=lambda: subprocess.Popen(["start", "cmd", "\k", "python", r"tools\token_checker.py"], shell=True))
    self.token_checker_button.place(relx=0.36, rely=0.75, anchor="center", width=200, height=50)
    create_tooltip(self.token_checker_button, "Checks Discord tokens by trying to log in with them.")
    
    print("Widgets created")
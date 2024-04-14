import tkinter as tk
from tkinter import ttk, messagebox as msgbox

import pypresence

from misc.tooltips import create_tooltip

"""
Sets a custom RPC status, using a Discord bot.
"""


instructions = "INSTRUCTIONS:\n\n\
You'll need a Discord bot in order to make a custom RPC.\n\
Go to https://discord.com/developers/applications and create a new one, if you haven't already.\n\
Name it whatever you want, note that it'll appear as \"<User> is playing <bot name>\". \n\
Once you've created it, copy the client ID and paste it into the client ID field. To use large and \n\
small images, you'll have to the Rich Presence tab, and import an image (at least 512x), and name it\n\
whatever you want, but I'd recommend naming it either largeimage or smallimage, depending on which one\n\
it'll be. To display it, enter the image name into either the large image name field or the small image\n\
name field. Click the start updating button for the custom RPC to show up. Note that it'll update every 5\n\
seconds, in order to keep it working. Using URLs as images won't work."

def main(self):
    
    from misc.icons import iconify #I have to import it after a root window is created (in this case, self.master)
    
    #Create a toplevel window
    toplevel = tk.Toplevel()
    toplevel.title("Custom RPC")
    toplevel.geometry("1080x720")
    toplevel.wm_iconphoto(True, iconify("custom_rpc"))
    toplevel.resizable(False, False)
    toplevel.focus()

    #Instructions
    instructions_label = ttk.Label(toplevel, text=instructions)
    instructions_label.place(relx=0.025, rely=0.025)

    #All the fields for the custom RPC
    client_id_label = ttk.Label(toplevel, text="Client ID")
    client_id_label.place(relx=0.8, rely=0.025, anchor="center")
    
    client_id_entry = ttk.Entry(toplevel)
    client_id_entry.place(relx=0.8, rely=0.05, anchor="center", width=200)
    client_id_entry.insert(0, self.configs["bot_id"])
    create_tooltip(client_id_entry, "Client or bot ID.")

    details_label = ttk.Label(toplevel, text="Details (line 1 and 2)")
    details_label.place(relx=0.8, rely=0.1, anchor="center")
    
    state_entry = ttk.Entry(toplevel)
    state_entry.place(relx=0.8, rely=0.125, anchor="center", width=200)
    create_tooltip(state_entry, "Line 2 of description. For stuff like \"Playing solo mode\".")
    
    details_entry = ttk.Entry(toplevel)
    details_entry.place(relx=0.8, rely=0.16, anchor="center", width=200)
    create_tooltip(details_entry, "Line 1 of description. For stuff like \"Competitive\".")

    timestamps_label = ttk.Label(toplevel, text="Timestamps (start / end), in Unix format.")
    timestamps_label.place(relx=0.8, rely=0.2, anchor="center")
    
    start_entry = ttk.Entry(toplevel)
    start_entry.place(relx=0.8, rely=0.225, anchor="center", width=200)
    create_tooltip(start_entry, "Start timestamp, in Unix format.")
    
    end_entry = ttk.Entry(toplevel)
    end_entry.place(relx=0.8, rely=0.26, anchor="center", width=200)
    create_tooltip(end_entry, "End timestamp, in Unix format.")

    large_image_label = ttk.Label(toplevel, text="Large image (name and text)")
    large_image_label.place(relx=0.8, rely=0.3, anchor="center")
    
    large_image_entry = ttk.Entry(toplevel)
    large_image_entry.place(relx=0.8, rely=0.325, anchor="center", width=200)
    create_tooltip(large_image_entry, "Key or name of the image you imported. URLs won't work.")
    
    large_text_entry = ttk.Entry(toplevel)
    large_text_entry.place(relx=0.8, rely=0.36, anchor="center", width=200)
    create_tooltip(large_text_entry, "Text that appears when hovering the image. Pretty much like the text that is appearing right now.")

    small_image_label = ttk.Label(toplevel, text="Small image (name and text)")
    small_image_label.place(relx=0.8, rely=0.4, anchor="center")
    
    small_image_entry = ttk.Entry(toplevel)
    small_image_entry.place(relx=0.8, rely=0.425, anchor="center", width=200)
    create_tooltip(small_image_entry, "Key or name of the image you imported. URLs won't work.")
    
    small_text_entry = ttk.Entry(toplevel)
    small_text_entry.place(relx=0.8, rely=0.46, anchor="center", width=200)
    create_tooltip(small_text_entry, "Text that appears when hovering the image. Pretty much like the text that is appearing right now.")

    button1_label = ttk.Label(toplevel, text="Button 1 (label and url)")
    button1_label.place(relx=0.8, rely=0.5, anchor="center")
    button1_label_entry = ttk.Entry(toplevel)
    button1_label_entry.place(relx=0.8, rely=0.525, anchor="center", width=200)
    button1_url_entry = ttk.Entry(toplevel)
    button1_url_entry.place(relx=0.8, rely=0.56, anchor="center", width=200)
    create_tooltip(button1_label_entry, "Text that appears on the 1st button.")
    create_tooltip(button1_url_entry, "URL of the 1st button.")

    button2_label = ttk.Label(toplevel, text="Button 2 (label and url)")
    button2_label.place(relx=0.8, rely=0.6, anchor="center")
    button2_label_entry = ttk.Entry(toplevel)
    button2_label_entry.place(relx=0.8, rely=0.625, anchor="center", width=200)
    button2_url_entry = ttk.Entry(toplevel)
    button2_url_entry.place(relx=0.8, rely=0.66, anchor="center", width=200)
    create_tooltip(button2_label_entry, "Text that appears on the 2nd button.")
    create_tooltip(button2_url_entry, "URL of the 2nd button.")


    def update():
        """Update the custom RPC every 5 seconds"""
        
        #Try to get the client ID, if there's none, warn the user
        if client_id_entry.get():
            self.configs["bot_id"] = client_id_entry.get()
        else:
            msgbox.showwarning("Client ID missing.", "You need a client ID, you dumb ass.")
            toplevel.focus()
        
        #Gather all the information from the entries
        state = state_entry.get()
        details = details_entry.get()
        large_image = large_image_entry.get()
        large_text = large_text_entry.get()
        small_image = small_image_entry.get()
        small_text = small_text_entry.get()
        button1_label = button1_label_entry.get()
        button1_url = button1_url_entry.get()
        button2_label = button2_label_entry.get()
        button2_url = button2_url_entry.get()

        #Try to convert the timestamps into integers
        try:
            start = int(start_entry.get()) if start_entry.get() else None
            end = int(end_entry.get()) if end_entry.get() else None
            
        except:
            print("The fucking asshole in front of the computer didn't input valid numbers for the timestamps, setting them both to None")
            start = None
            end = None

        #Update the custom RPC, with all the stuff from the entries
        RPC = pypresence.Presence(self.configs["bot_id"])
        RPC.connect()
        
        RPC.update(
            state = state if state else None,
            details = details if details else None,
            start = start,
            end = end,
            large_image = large_image if large_image else None,
            large_text = large_text if large_text and large_image else None,
            small_image = small_image if small_image else None,
            small_text = small_text if small_text and small_image else None,
            buttons = [
                {
                    "label": button1_label,
                    "url": button1_url
                } if button1_label and button1_url else {},
                {
                    "label": button2_label,
                    "url": button2_url
                } if button2_label and button2_url else {}
            ] if button1_label and button1_url or button2_label and button2_url else None
        )
        
        
        #Do it every 5 seconds
        if self.custom_rpc_enabled:
            self.master.after(5000, update)
            
            print(f"""
    Updated the custom RPC:
    State: {state}
    Details: {details}
    Start timestamp: {start}
    End timestamp: {end}
    Large image: {large_image}
    Large image text: {large_text}
    Small image: {small_image}
    Small image text: {small_text}
    Button 1 label: {button1_label}
    Button 1 URL: {button1_url}
    Button 2 label: {button2_label}
    Button 2 URL: {button2_url}
    """)


    def start():
        #Starts updating the custom RPC
        
        self.custom_rpc_enabled = True
        update()


    def stop():
        #Stops updating the custom RPC
        
        self.custom_rpc_enabled = False
        print("Stopped updating the custom RPC")


    #Update button
    update_button = ttk.Button(toplevel, text="Start updating", command=start)
    update_button.place(relx=0.2, rely=0.4, anchor="center", width=200, height=50)

    #Stop button
    stop_button = ttk.Button(toplevel, text="Stop updating", command=stop)
    stop_button.place(relx=0.4, rely=0.4, anchor="center", width=200, height=50)
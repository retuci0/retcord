import requests

import tkinter as tk
from tkinter import messagebox as msgbox
from tkinter import ttk


def main(self):
    
    from misc.icons import iconify #I have to import it after a root window is created (in this case, self.master)
    
    if self.configs["channel_id"]:
        #Create a toplevel window
        toplevel = tk.Toplevel(self.master)
        toplevel.title("Spam")
        toplevel.resizable(False, False)
        toplevel.wm_iconphoto(True, iconify("spam"))
        toplevel.geometry("1200x800")
        toplevel.focus()
        
        def close():
            self.spamming = False
            toplevel.destroy()
            
        toplevel.protocol("WM_DESTOY_WINDOW", close)

        #Message
        message_text = tk.Text(toplevel)
        message_text.place(relx=0.5, rely=0.3, width=1000, height=100, anchor="center")
        message_text.insert(1.0, "Message goes here")

        #Interval spinbox
        interval_label = ttk.Label(toplevel, text="Interval:                                                     ms")
        interval_label.place(relx=0.082, rely=0.15)
        interval_spinbox = ttk.Spinbox(toplevel, from_=20, to=3600000)
        interval_spinbox.place(relx=0.125, rely=0.15)
        
        #Create a listbox for the responses' status codes
        response_listbox = ttk.Treeview(toplevel, show="tree")
        response_listbox.place(relx=0.5, rely=0.65, anchor="center", width=1000, height=400)

        def start_spamming():
            #Spam the desired message at the desired interval in the desired channel (desired)
            if message_text.get(1.0, tk.END):
                message = message_text.get(1.0, tk.END)
            else:
                msgbox.showwarning("Message missing!", "You have to send a message with content, you dumbfuck.")
            
            if interval_spinbox.get() and int(interval_spinbox.get()) >= 20 and int(interval_spinbox.get()) <= 3600000:
                interval = int(interval_spinbox.get())
            else:
                msgbox.showwarning("Interval missing!", "Add an interval in milliseconds (20-3600000), if you know how to count.")

            request = requests.post(
                url = f"https://discord.com/api/v9/channels/{self.configs["channel_id"]}/messages",
                headers = self.headers,
                json = {
                    "mobile_network_type": "unknown",
                    "content": message,
                    "nonce": "",
                    "tts": False,
                    "flags": 0
                }
            )

            if self.spamming:
                #Get the status codes and put them into the listbox
                response_listbox.insert("", "end", text=f"Status code: {request.status_code}; Message: {message}")
                print(f"Spammed message: {message}")
                print(f"Status code: {request.status_code}")
                self.master.after(interval, start_spamming)
        
        def start():
            #Start spamming
            self.spamming = True
            print("Started spamming")
            start_spamming()
        
        def stop():
            #Stop spamming
            self.spamming = False
            print("Stopped spamming")

        #Start button
        start_button = ttk.Button(toplevel, text="Start", command=start)
        start_button.place(relx=0.35, rely=0.05, anchor="center", width=200, height=50)

        #Stop button
        stop_button = ttk.Button(toplevel, text="Stop", command=stop)
        stop_button.place(relx=0.65, rely=0.05, anchor="center", width=200, height=50)
        
    else:
        msgbox.showwarning("Channel ID missing!", "Enter a channel ID, you dumbass.")
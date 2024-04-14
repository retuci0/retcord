import requests
import tkinter as tk
from tkinter import messagebox as msgbox
from tkinter import ttk

"""
Edits a message without the (edited) tag showing up, this is done by sending a message request, and setting the \"nonce\" (message ID) to an already existing one, 
replacing the original message's content with the new one. Keep in mind that the message's timestamp does change.
"""

def main(self):
    
    from misc.icons import iconify #I have to import it after a root window is created (in this case, self.master)
    
    if self.configs["channel_id"]:
        
        #Create a toplevel window
        toplevel = tk.Toplevel(self.master)
        toplevel.title("Edit message secretly")
        toplevel.geometry("600x500")
        toplevel.wm_iconphoto(True, iconify("edit_message"))
        toplevel.resizable(False, False)
        toplevel.focus()

        #Message
        message_text = tk.Text(toplevel, relief="solid", highlightcolor="#828790")
        message_text.place(relx=0.5, rely=0.55, width=500, height=200, anchor="center")
        message_text.insert(1.0, "New message content")

        #Message ID entry
        nonce_label = ttk.Label(toplevel, text="Message ID: ")
        nonce_label.place(relx=0.05, rely=0.15)
        nonce_entry = ttk.Entry(toplevel)
        nonce_entry.place(relx=0.25, rely=0.15)


        def edit():
            
            #Edits the message
            nonce = nonce_entry.get()
            content = message_text.get(1.0, tk.END)

            request = requests.post(
                url = f"https://discord.com/api/v9/channels/{self.configs["channel_id"]}/messages",
                headers = self.headers,
                json = {
                    "mobile_network_type": "unknown",
                    "content": content,
                    "nonce": nonce,
                    "tts": False,
                    "flags": 0,
                }
            )
            
            print(f"Message (edit) request status code: {request.status_code}")
            print(f"    Message ID: {nonce}")
            print(f"    Content: {content}")
            print(f"    Response text: {request.text}")
            msgbox.showinfo("Successfully edited message", f"Status code: {str(request.status_code)}")

        #Edit button
        edit_button = ttk.Button(toplevel, text="Edit", command=edit)
        edit_button.place(relx=0.7, rely=0.17, anchor="center", width=100, height=30)
    
    else:
        msgbox.showwarning("Channel ID missing!", "You need to input a channel ID, you dumbshit.")
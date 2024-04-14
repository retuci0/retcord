import pyperclip

import tkinter as tk
from tkinter import messagebox as msgbox
from tkinter import ttk

"""
Uses the right to left embedding character (U+202B) where you want the (edited) tag to be.
"""

def main(self):

    from misc.icons import iconify #I have to import it after a root window is created (in this case, self.master)
    
    #Toplevel window
    toplevel = tk.Toplevel(self.master)
    toplevel.title("Custom (edited) tag location")
    toplevel.geometry("800x600")
    toplevel.wm_iconphoto(True, iconify("edited_tag"))
    toplevel.resizable(False, False)
    toplevel.focus()

    #Info label
    info_label = ttk.Label(toplevel, text="Write some normal text, and write (edited) where you want the edited tag to be.")
    info_label_2 = ttk.Label(toplevel, text="Then, send a message, edit it and replace the content with the copied text.")
    info_label.place(relx=0.5, rely=0.1, anchor="center")
    info_label_2.place(relx=0.5, rely=0.15, anchor="center")

    #Message entry
    message_text = tk.Text(toplevel)
    message_text.place(relx=0.5, rely=0.5, anchor="center")

    def convert_and_copy():
        
        #Get the message, format it and copy it into the user's clipboard
        message = message_text.get("1.0", tk.END)
        
        if "(edited)" in message:
            try:
                message = message.replace("(edited)", "\u202b", 1)
                pyperclip.copy(message)
                print("Copied message to clipboard")
                msgbox.showinfo("Success", "Message copied successfully.")
                
            except Exception as e:
                msgbox.showerror("How did you fuck this up too", e)
                
        else:
            msgbox.showerror("Dumb ass", "Instructions were very clear, but your autistic ass managed to mess that up too.")
            toplevel.focus()
    
    copy_button = ttk.Button(toplevel, text="Convert and copy", command=convert_and_copy)
    copy_button.place(relx=0.5, rely=0.9, anchor="center", width=200, height=50)
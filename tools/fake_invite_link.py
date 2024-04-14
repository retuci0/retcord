import pyperclip

import tkinter as tk
from tkinter import messagebox as msgbox
from tkinter import ttk

"""
Uses spoiler spam to glitch out the message, making the original link embed appear, but only the fake link appears on the message.
"""

spoiler_spam = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _ "

def main(self):
    
    from misc.icons import iconify #I have to import it after a root window is created (in this case, self.master)

    #Create a toplevel window
    toplevel = tk.Toplevel(self.master)
    toplevel.title("Fake invite link")
    toplevel.geometry("700x500")
    toplevel.wm_iconphoto(True, iconify("fake_invite_link"))
    toplevel.resizable(False, False)
    toplevel.focus()

    #Widgets
    real_link_label = ttk.Label(toplevel, text="Original link: ")
    real_link_label.place(relx=0.5, rely=0.25, anchor="center")
    real_link_entry = ttk.Entry(toplevel)
    real_link_entry.place(relx=0.5, rely=0.3, anchor="center")

    fake_link_label = ttk.Label(toplevel, text="New / fake link: ")
    fake_link_label.place(relx=0.5, rely=0.4, anchor="center")
    fake_link_entry = ttk.Entry(toplevel)
    fake_link_entry.place(relx=0.5, rely=0.45, anchor="center")

    protip_label = ttk.Label(toplevel, text="Pro tip: use the spoiler spam and simply add a mention at the end for an invisible mention.")
    protip_label.place(relx=0.5, rely=0.7, anchor="center")

    def copy():
        
        #Copy the formatted text into the clipboard
        if real_link_entry.get():
            real_link = real_link_entry.get()
        else:
            msgbox.showwarning("Fill all entries, you dumbshit.")
            return
        
        if fake_link_entry.get():
            fake_link = fake_link_entry.get()
        else:
            msgbox.showwarning("Fill all entries, you dumbshit.")
            return

        pyperclip.copy(fake_link + spoiler_spam + real_link)
        print("Copied fake invite link to clipboard")
    
    copy_button = ttk.Button(toplevel, text="Copy to clipboard", command=copy)
    copy_button.place(relx=0.5, rely=0.6, anchor="center", width=200, height=50)
import tkinter as tk

from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import ttk


def login(self):
    
    from misc.icons import iconify
    
    """Logs in using a Discord token."""
    
    toplevel = tk.Toplevel(self.master)
    toplevel.title("Log in with a Discord token.")
    toplevel.geometry("1080x720")
    #toplevel.wm_iconphoto(True, iconify("login"))
    toplevel.resizable(False, False)
    toplevel.focus()
    
    token_label = tk.Label(toplevel, text="Enter your Discord token to log in:")
    token_label.pack()
    
    token_entry = ttk.Entry(toplevel, width=100)
    token_entry.pack()
    
    def login():
        #Get the token
        
        global token
        token = token_entry.get().strip()
        
        if token:
            #Save token to configs
            self.configs["token"] = token
            toplevel.destroy()
        
        else:
            messagebox.showerror("Error", "Token cannot be empty, moron.")
    
    login_button = ttk.Button(toplevel, text="Log in", command=login)
    login_button.pack()

        
def update_channel_id(self):
    """Updates the channel ID attribute."""
    
    if not self.channel_id_entry.get():
        messagebox.showerror("Channel ID missing", "Next time input a channel ID, smart ass.")
        return
    
    self.configs["channel_id"] = self.channel_id_entry.get()
    
    self.channel_id_entry.insert(0, str(self.configs["channel_id"]))
    print(f"Updated channel ID: {self.configs["channel_id"]}")
    
    
def change_logo(self):
    """Let the user choose between the coolest logo in history."""
    
    from misc.icons import iconify
    
    #Create a toplevel window
    toplevel = tk.Toplevel()
    toplevel.title("Select custom logo")
    toplevel.geometry("1080x720")
    toplevel.wm_iconphoto(True, iconify("change_logo"))
    toplevel.resizable(False, False)
    toplevel.focus()
    
    #Logo images declaration
    default_image = PhotoImage(file="assets/logos/default.png")
    nerd_image = PhotoImage(file="assets/logos/nerd.png")
    uwu_image = PhotoImage(file="assets/logos/uwu.png")
    british_image = PhotoImage(file="assets/logos/british.png")

    logo_names = {
        default_image: "default logo",
        nerd_image: "nerd logo",
        uwu_image: "uwu logo",
        british_image: "british logo"
    }
    
    #Instructions label
    logo_label = ttk.Label(toplevel, text="Select logo from below, or change path in line 135 to a custom one.")
    logo_label.place(relx=0.2, rely=0.07, anchor="center")
    
    #Sets the logo to the selected one
    def set_logo(logo):
        self.logo_label.config(image=logo)
        self.logo_label.photo = logo
        
        self.configs["logo"] = logo_names[logo]
        print(f"Logo set to: {logo_names[logo]}")
        

    #Default logo button
    default_button_image = PhotoImage(file="assets/buttons/default.png")
    default_logo_button = ttk.Button(toplevel, image=default_button_image, command=lambda: set_logo(default_image))
    default_logo_button.photo = default_button_image
    default_logo_button.place(relx=0.2, rely=0.5, anchor="center", width=160, height=210)
    
    #Nerdy logo button
    nerd_button_image = PhotoImage(file="assets/buttons/nerd.png")
    nerd_logo_button = ttk.Button(toplevel, image=nerd_button_image, command=lambda: set_logo(nerd_image))
    nerd_logo_button.photo = nerd_button_image
    nerd_logo_button.place(relx=0.4, rely=0.5, anchor="center", width=160, height=210)
    
    #UwU logo button
    uwu_button_image = PhotoImage(file="assets/buttons/uwu.png")
    uwu_logo_button = ttk.Button(toplevel, image=uwu_button_image, command=lambda: set_logo(uwu_image))
    uwu_logo_button.photo = uwu_button_image
    uwu_logo_button.place(relx=0.6, rely=0.5, anchor="center", width=160, height=210)
    
    #Bri'ish logo button
    british_button_image = PhotoImage(file="assets/buttons/british.png")
    british_logo_button = ttk.Button(toplevel, image=british_button_image, command=lambda: set_logo(british_image))
    british_logo_button.photo = british_button_image
    british_logo_button.place(relx=0.8, rely=0.5, anchor="center", width=160, height=210)
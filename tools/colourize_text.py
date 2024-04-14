import pyperclip
import re

import tkinter as tk
from tkinter import ttk


"""
Adds colour to your text by using ANSI colour codes. Shoutout to kkrypt0nn for this guide on ANSI colour codes: https://gist.github.com/kkrypt0nn/a02506f3712ff2d1c8ca7c9e0aed7c06
"""

patterns = {
    "gray": r"<gray>(.*?)</gray>",
    "red": r"<red>(.*?)</red>",
    "green": r"<green>(.*?)</green>",
    "yellow": r"<yellow>(.*?)</yellow>",
    "blue": r"<blue>(.*?)</blue>",
    "pink": r"<pink>(.*?)</pink>",
    "cyan": r"<cyan>(.*?)</cyan>",
    "white": r"<white>(.*?)</white>"
}

colour_codes = {
    "gray": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "pink": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "reset": "\033[0m"
}

def main(self):
    
    from misc.icons import iconify #I have to import it after a root window is created (in this case, self.master)
    
    #Creates a toplevel window
    toplevel = tk.Toplevel(self.master)
    toplevel.title("Colourize text")
    toplevel.geometry("1000x800")
    toplevel.iconphoto(True, iconify("colourize_text"))
    toplevel.resizable(False, False)
    toplevel.focus()

    #Instructions
    title_label = ttk.Label(toplevel, text="INSTRUCTIONS", font=("Helvetica", 20))
    title_label.place(relx=0.5, rely=0.05, anchor="center")
        
    #I haven't really found another way of centering a multiline label, I tried with newlines and with multiline strings, I may just be stupid though
    message_label_1 = ttk.Label(toplevel, text="Use colour tags to add colour to your text, then click the copy to clipboard button to copy it.")
    message_label_2 = ttk.Label(toplevel, text="Format: <colorname>coloured text goes here</colourname> normal text goes here <colourname>more coloured text here</colourname>")
    message_label_3 = ttk.Label(toplevel, text="Supported colours: gray, red, green, yellow, blue, pink, cyan and white.")
    message_label_4 = ttk.Label(toplevel, text="e. g.: <blue>blue text</blue> normal text <red>red text</red>")
    message_label_1.place(relx=0.5, rely=0.1, anchor="center")
    message_label_2.place(relx=0.5, rely=0.15, anchor="center")
    message_label_3.place(relx=0.5, rely=0.2, anchor="center")
    message_label_4.place(relx=0.5, rely=0.25, anchor="center") 

    #User inputs text here
    message_text = tk.Text(toplevel)
    message_text.place(relx=0.5, rely=0.6, anchor="center")

    def convert_and_copy():
        
        #Formats the text into ANSI to colour it and copies it to the user's clipboard
        text = message_text.get("1.0", tk.END)
        
        for colour, pattern in patterns.items():
            matches = re.findall(pattern, text)
            
            for match in matches:
                colorized_text = colour_codes[colour] + match + colour_codes["reset"]
                text = re.sub(pattern, colorized_text, text, count=1)
        
        pyperclip.copy("```ansi\n" + text + "\n```")
        print("Copied text to clipboard")

    #Copy button
    copy_button = ttk.Button(toplevel, text="Copy to clipboard", command=convert_and_copy)
    copy_button.place(relx=0.5, rely=0.9, anchor="center", width=150, height=50)
import tkinter as tk
"""Credits."""

credits_text = """
Retcord v1.7 [14/IV/2024]
Made by Retucio. Do not claim this as yours, you fucking loser.


Stolen code:
- DOS tool: Zero-attacker tool
- Token bruteforcer: Byete's token bruteforcer
- Nitro code generator: lnxcz's Nitro gen
- Lootbox opener: Tenclea's lootbox opener (I just needed to know X-super-properties was needed in the headers)
"""

def show_credits(self):
    from misc.icons import iconify #I have to import it after a root window is created (in this case, self.master)
    
    toplevel = tk.Toplevel(self.master)
    toplevel.title("Credits")
    toplevel.geometry("1080x720")
    toplevel.wm_iconphoto(True, iconify("credits"))
    toplevel.resizable(False, False)
    toplevel.focus()

    credits_label = tk.Label(toplevel, text=credits_text)
    credits_label.pack()
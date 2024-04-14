import requests
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox

"""
Types infinitely by sending typing requests to the Discord API every 5 seconds (each one last 10 but just in case yk).
"""
    
def main(self):
    
    from misc.icons import iconify #I have to import it after a root window is created (in this case, self.master)
    
    if self.configs["channel_id"]:
        #Create a toplevel window
        toplevel = tk.Toplevel(self.master)
        toplevel.title("Type infinitely")
        toplevel.geometry("1200x800")
        toplevel.wm_iconphoto(True, iconify("type_infinitely"))
        toplevel.resizable(False, False)
        toplevel.focus()
        
        def close():
            self.typing = False
            toplevel.destroy()
            
        toplevel.protocol("WM_DELETE_WINDOW", close)
        
        #Create a listbox for the responses' status codes
        response_listbox = ttk.Treeview(toplevel, show="tree")
        response_listbox.place(relx=0.5, rely=0.5, anchor="center", width=1000, height=600)

        def start_typing():
                #Send a typing request every 5 seconds (each one lasts 10, but just in case)
                try:
                    request = requests.post(
                        url = f"https://discord.com/api/v9/channels/{self.configs["channel_id"]}/typing",
                        headers = self.headers
                    )

                    #Get the status codes and put them into the listbox
                    print(f"Typing request status code: {request.status_code}")
                    response_listbox.insert("", "end", text=f"Status code: {request.status_code}")
                except Exception as e:
                    print(e, request.status_code, request.text)
                    print(f"Exception: {e}")
                    print(f"Status code: {request.status_code}")
                    print(f"Response text: {request.text}")

                if self.typing == True:
                    self.master.after(5000, start_typing)
        
        def start():
            #Starts typing
            self.typing = True
            print("Started typing")
            start_typing()

        def stop():
            #Stops typing
            self.typing = False
            print("Stopped typing")

        #Start button
        start_button = ttk.Button(toplevel, text="Start", command=start)
        start_button.place(relx=0.35, rely=0.05, anchor="center", width=200, height=50)

        #Stop button
        stop_button = ttk.Button(toplevel, text="Stop", command=stop)
        stop_button.place(relx=0.65, rely=0.05, anchor="center", width=200, height=50)
        
    else:
        msgbox.showwarning("Channel ID missing!", "Enter a channel ID, you dumbass.")
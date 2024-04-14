from PIL import Image, ImageTk

#I came across some problems when using .ico files as icons, so I used PhotoImage objects with wm_iconphoto instead

def iconify(image_name):
    """Converts a png into a PhotoImage object."""
    
    image = Image.open("assets/icons/" + image_name + ".png")
    icon = ImageTk.PhotoImage(image=image)
    return icon
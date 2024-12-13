# Import the Tkinter font module
import tkinter.font as tkfont


# Function to configure the fonts of the Tkinter application
def configure():
    # Choose the desired font family (e.g., "Helvetica")
    family = "Helvetica"

    # Retrieve and configure the default font
    default_font = tkfont.nametofont("TkDefaultFont")
    default_font.configure(size=15, family=family)

    # Retrieve and configure the font for Tkinter text widgets
    text_font = tkfont.nametofont("TkTextFont")
    text_font.configure(size=12, family=family)

    # Retrieve and configure the fixed font for Tkinter
    fixed_font = tkfont.nametofont("TkFixedFont")
    fixed_font.configure(size=12, family=family)

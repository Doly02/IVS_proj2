
#######################################################
 # Název projektu: Kalkulačka
 # Soubor: aboutGUI.py
 # Datum: 22.3.2023
 # Poslední změna: 23.3.2023
 # Autor: Jakub Jerabek
 # Tým: Tomojavo
 # Popis: GUI okna ABout
#######################################################



from pathlib import Path
from datetime import date

import tkinter as tk
from tkinter import *


# Explicit imports to satisfy Flake8
#from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)




class About(tk.Toplevel):
    def __init__(self, parent, color_bg, color_toppanel):
        tk.Toplevel.__init__(self)
        self.geometry("535x535")
        self.configure(bg=color_bg)
        
        canvas = tk.Canvas(
            self,
            bg = color_bg,
            height = 701,
            width = 535,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            0.0,
            535.0,
            43.0,
            fill=color_toppanel,
            outline="")

        # Aktualni datum
        canvas.create_text(
            390.0,
            9.0,
            anchor="nw",
            text=date.today(),
            fill="#FFFFFF",
            font=("Inter", 20 * -1)
        )

        canvas.create_text(
            110.0,
            54.0,
            anchor="nw",
            text="O nás (a o programu)",
            fill="#FFFFFF",
            font=("Inter", 30 * -1)
        )

        canvas.create_text(
            110.0,
            100.0,
            anchor="nw",
            text="Version 1.0\nAuthors:\nJakub Jerabek\nMonika Zahradnikova\nVojtech Teichmann\nTomas Dolak\n\nTento program byl vytvoren\npro predmet IVS na FIT VUT Brno\n\nLicence GNU GPL v. 3.0",
            fill="#FFFFFF",
            font=("Inter", 20 * -1)
        )




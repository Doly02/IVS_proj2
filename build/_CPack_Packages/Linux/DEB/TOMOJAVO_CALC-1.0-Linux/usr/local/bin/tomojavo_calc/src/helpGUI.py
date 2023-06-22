
#######################################################
 # Název projektu: Kalkulačka
 # Soubor: helpGUI.py
 # Datum: 22.3.2023
 # Poslední změna: 23.3.2023
 # Autor: Jakub Jerabek a Tomas Dolak
 # Tým: Tomojavo
 # Popis: GUI okna Help
#######################################################


from pathlib import Path
from datetime import date

import tkinter as tk
from tkinter import *


# Explicit imports to satisfy Flake8
#from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


#window = Tk()

#window.geometry("535x701")
#window.configure(bg = "#420069")

class Help(tk.Toplevel):
    def __init__(self, parent, color_bg, color_toppanel):
        tk.Toplevel.__init__(self, parent)

        self.geometry("735x735")
        #self.title(u"About calculator")
        self.focus_set()
        self.configure(bg = "#420069")
        

        canvas = tk.Canvas(
            self,
            bg = color_bg,
            height = 701,
            width = 735,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            0.0,
            735.0,
            43.0,
            fill=color_toppanel,
            outline="")

        # Aktualni datum
        canvas.create_text(
            590.0,
            9.0,
            anchor="nw",
            text=date.today(),
            fill="#FFFFFF",
            font=("Inter", 20 * -1)
        )
        canvas.create_text(
            250.0,
            54.0,
            anchor="nw",
            text="MÁTE POTÍŽE? ",
            fill="#FFFFFF",
            font=("Inter", 30 * -1)
        )

        canvas.create_text(
            10.0,
            95.0,
            anchor="nw",
            text="Tým Tomojavo vyvinul kalkulačku, kterou je jednoduché používat, zde jsou\nzákladní tipy, které vám usnadní práci s naší kalkulačkou:\n\nI. Pro napsání čísla, zmáčkněte symbol vybraného čísla nebo zmáčkněte\nklávesu symbolizující danou číslici na klávesnici\nII. Zde můžete najít některé významy užitečných operátorů:\n\t- tlačítko AC, vyčistí obsah okna\n\t- tlačítko X znamená násobení (ale né to v rohu obrazovky!)\n\t\t- PŘÍKLAD POUŽITÍ: 4 * 5 = 20\n\t- tlačítko s čírkou a dvěmi tečkami znamená dělení\n\t\t- PŘÍKLAD POUŽITÍ: 20 / 5 = 4\n\t- tlačítko n s vykřičníkem znamená faktoriál\n\t\t- PŘÍKLAD POUŽITÍ: 4! = 4 * 3 * 2 * 1 = 24\n\t- červené tlačítko vymaže poslední číslo v okně\n\t- zelené tlačítko s dvěmi čarami je rovná se a zobrazí\n\t   výsledek operace \n\t- tlačítko x s malou dvojkou je symbol druhé mocniny x\n\t\t- PŘÍKLAD POUŽITÍ: 4^2 = 16\n\t- tlačítko x s malým n-kem symbolizuje obecnou mocninu x\n\t\t- PŘÍKLAD POUŽITÍ: 4^5 = 1024\n\t- tlačítko druhé odmocniny spočítá druhou odmocninu\n\t\t- PŘÍKLAD POUŽITÍ: sqrt(16) = 4\n\t- tlačítko mod vypočítá celočíselný zbytek po dělení\n\t\t- PŘÍKLAD POUŽITÍ: 5 % 2 = 1",
            fill="#FFFFFF",
            font=("Inter", 17 * -1)
        )

        canvas.create_text(
            10.0,
            630.0,
            anchor="nw",
            text="V případě problému zkuste restartovat kalkulačku,v případě neúspěchu zkuste\nznova nainstalovat kalkulačku jestli ani to nepomůže prosím kontaktujte podporu.",
            fill="#FFFFFF",
            font=("Inter", 17 * -1)
        )

        canvas.create_text(
            226.0,
            680.0,
            anchor="nw",
            text="Licence GNU GPL v. 3.0\n",
            fill="#FFFFFF",
            font=("Inter", 20 * -1)
        )

        canvas.create_text(
            590.0,
            680.0,
            anchor="nw",
            text="FIT VUT Brno",
            fill="#FFFFFF",
            font=("Inter", 20 * -1)
        )

        canvas.create_text(
            5.0,
            680.0,
            anchor="nw",
            text="2023",
            fill="#FFFFFF",
            font=("Inter", 20 * -1)
        )

    
#!/usr/bin/env python3
import tkinter as tk

from pathlib import Path
from datetime import date

from aboutGUI import About
from helpGUI import Help

from link_lib_w_gui import *

#

# Deklarace cesty k assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frame0/purple")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



# Pocatecni barvicky
color_scheme="blue"
background="#420069"
toppanel="#7B2CBF"
color_fg="#3a0057"


class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Kalkulacka TOMOJAVO")
        # Barvicky
        global color_toppanel, color_bg
        self.configure(bg=background)
        color_toppanel=toppanel
        color_bg=background
        foreground=color_fg
        # creating a frame and assigning it to container
        container = tk.Frame(self, height=400, width=200)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        #container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # Ikonka
        icon = PhotoImage(
        file=Path(r"/usr/local/bin/tomojavo_calc/assets/Tomojavo_icon.png"))
        self.iconphoto(True, icon)


        # We will now create a dictionary of frames
        self.frames = {}
        frame = Calculator(container, self, color_bg, color_toppanel)
        frame.entry.focus_set()
        self.frames[Calculator] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.frames[Calculator] = Calculator(container, self, color_bg, color_toppanel)


def change_colors():
    """ Changes color scheme of the app
    @return: creates a window with new color scheme
    """
    global color_scheme, ASSETS_PATH, background, toppanel, color_fg
    if color_scheme == "purple":
        ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frame0/purple")
        background="#420069"
        toppanel="#7B2CBF"
        color_fg="#3a0057"
        color_scheme="blue"
    else:
        ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frame0/blue")
        background="#2C2C2C"
        toppanel="#0066FF"
        color_fg="#000716"
        color_scheme="purple"
    global app
    app.destroy()
    app = windows()
    app.mainloop()


class Calculator(tk.Frame):
    def __init__(self, parent, controller, color_bg, color_toppanel):
        tk.Frame.__init__(self, parent)
        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        self.configure(bg=color_bg)
        self.create_buttons()

    def create_buttons(self):
        butcntr=buttons()
        button_top = {
            "borderwidth": 0,
            "highlightthickness": 3,
            "highlightbackground": toppanel,
            "background": toppanel
        }

        button_style = {
            "borderwidth": 0,
            "highlightthickness": 3,
            "highlightbackground": color_bg,
            "background": color_bg
        }

        # Define buttons
        topFrame= tk.Frame(self, width=550, height=43, bg=toppanel, highlightbackground="red", highlightthickness=0, borderwidth=0)
        topBG= tk.Label(topFrame)

        entryFrame= tk.Frame(self, width=500, height=120, borderwidth=0, bg=color_fg)
        #global e
        self.entry = tk.Entry(entryFrame, 
                  justify="right", 
                  width=10,
                  font=("Inter", 48), 
                  fg="white", 
                  bg=color_fg, 
                  highlightthickness=0, 
                  borderwidth=0,
                  bd=0)
        
        self.entry.bind("<Return>", lambda event: butcntr.button_equal(self.entry))
        self.entry.bind("<Escape>", lambda event: butcntr.button_clear(self.entry))
        #self.entry.bind("<KP_Decimal>", lambda event: butcntr.button_dot(self.entry))

        self.entry.bind("<KeyRelease-KP_Add>", lambda event: (
            self.entry.delete(len(event.widget.get())-1),
            butcntr.button_add(self.entry)
            ))
        
        self.entry.bind("<KeyRelease-KP_Subtract>", lambda event: (
            self.entry.delete(len(event.widget.get())-1),
            butcntr.button_subtract(self.entry),
            ))
        self.entry.bind("<KeyRelease-KP_Multiply>", lambda event: (
            self.entry.delete(len(event.widget.get())-1),
            butcntr.button_multiply(self.entry)
            ))
        self.entry.bind("<KeyRelease-KP_Divide>", lambda event: (
            self.entry.delete(len(event.widget.get())-1),
            butcntr.button_divide(self.entry)
            ))
        ####################################
        #                                  #
        #         IMAGE BUTTONS            #
        #                                  #
        ####################################
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png")
        )
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png")
        )
        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png")
        )
        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png")
        )
        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png")
        )
        self.button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png")
        )
        self.button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png")
        )
        self.button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png")
        )
        self.button_image_9 = PhotoImage(
            file=relative_to_assets("button_9.png")
        )
        self.button_image_0 = PhotoImage(
            file=relative_to_assets("button_0.png")
        )
        self.button_image_eq = PhotoImage(
            file=relative_to_assets("button_eq.png")
        )
        self.button_image_clear = PhotoImage(
            file=relative_to_assets("button_clear.png")
        )
        self.button_image_add = PhotoImage(
            file=relative_to_assets("button_add.png")
        )
        self.button_image_sub = PhotoImage(
            file=relative_to_assets("button_sub.png")
        )
        self.button_image_mult = PhotoImage(
            file=relative_to_assets("button_mult.png")
        )
        self.button_image_div = PhotoImage(
            file=relative_to_assets("button_div.png")
        )
        self.button_image_fact = PhotoImage(
            file=relative_to_assets("button_fact.png")
        )
        self.button_image_pow2 = PhotoImage(
            file=relative_to_assets("button_pow2.png")
        )
        self.button_image_pown = PhotoImage(
            file=relative_to_assets("button_pown.png")
        )
        self.button_image_sqr2 = PhotoImage(
            file=relative_to_assets("button_sqr2.png")
        )
        self.button_image_sqrn = PhotoImage(
            file=relative_to_assets("button_sqrn.png")
        )
        self.button_image_mod = PhotoImage(
            file=relative_to_assets("button_modulo.png")
        )
        self.button_image_dot = PhotoImage(
            file=relative_to_assets("button_dot.png")
        )
        self.button_image_about = PhotoImage(
            file=relative_to_assets("button_about.png"))
        self.button_image_help = PhotoImage(
            file=relative_to_assets("button_help.png"))
        self.button_image_color = PhotoImage(
            file=relative_to_assets("button_color.png"))
        self.button_image_del = PhotoImage(
            file=relative_to_assets("button_del.png"))
        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))


        ####################################
        #                                  #
        #         DEFINE BUTTONS           #
        #                                  #
        ####################################

        button_about = Button(topFrame, image=self.button_image_about, **button_top, command=self.open_about)
        button_help = Button(topFrame, image=self.button_image_help, **button_top, command=self.open_help)
        button_color = Button(topFrame, image=self.button_image_color, **button_top, command=change_colors)
        date_label = Label(topFrame, text=date.today(), bg=color_toppanel, fg="white", font=("Inter", 20 * -1))

        entry_bg_1 = Label(self, image=entry_image_1)
        self.button_1 = Button(self, image=self.button_image_1, **button_style, command=lambda: butcntr.button_click(self.entry, 1))
        self.button_2 = Button(self, image=self.button_image_2, **button_style, command=lambda: butcntr.button_click(self.entry, 2))
        button_3 = Button(self, image=self.button_image_3, **button_style, command=lambda: butcntr.button_click(self.entry, 3))
        button_4 = Button(self, image=self.button_image_4, **button_style, command=lambda: butcntr.button_click(self.entry, 4))
        button_5 = Button(self, image=self.button_image_5, **button_style, command=lambda: butcntr.button_click(self.entry, 5))
        button_6 = Button(self, image=self.button_image_6, **button_style, command=lambda: butcntr.button_click(self.entry, 6))
        button_7 = Button(self, image=self.button_image_7, **button_style, command=lambda: butcntr.button_click(self.entry, 7))
        button_8 = Button(self, image=self.button_image_8, **button_style, command=lambda: butcntr.button_click(self.entry, 8))
        button_9 = Button(self, image=self.button_image_9, **button_style, command=lambda: butcntr.button_click(self.entry, 9))

        button_0 = Button(self, image=self.button_image_0, **button_style, command=lambda: butcntr.button_click(self.entry, 0))
        global math
        global f_num
        global counter
        counter = 0
        f_num = 0
        button_dot = Button(self, image=self.button_image_dot, **button_style, command=lambda: butcntr.button_dot(self.entry))
        button_eq = Button(self, image=self.button_image_eq, **button_style, command=lambda: butcntr.button_equal(self.entry))
        button_clear = Button(self, image=self.button_image_clear, **button_style, command=lambda: butcntr.button_clear(self.entry))
        button_add = Button(self, image=self.button_image_add, **button_style, command=lambda: butcntr.button_add(self.entry))
        button_subtract = Button(self, image=self.button_image_sub, **button_style, command=lambda: butcntr.button_subtract(self.entry))
        button_multiply = Button(self, image=self.button_image_mult, **button_style, command=lambda: butcntr.button_multiply(self.entry))
        button_divide = Button(self, image=self.button_image_div, **button_style, command=lambda: butcntr.button_divide(self.entry))
        button_fact = Button(self, image=self.button_image_fact, **button_style, command=lambda: butcntr.button_fact(self.entry))
        button_pow2 = Button(self, image=self.button_image_pow2, **button_style, command=lambda: butcntr.button_pow2(self.entry))
        button_pown = Button(self, image=self.button_image_pown, **button_style, command=lambda: butcntr.button_pow(self.entry))
        button_sqr2 = Button(self, image=self.button_image_sqr2, **button_style, command=lambda: butcntr.button_sqr2(self.entry))
        button_sqrn = Button(self, image=self.button_image_sqrn, **button_style, command=lambda: butcntr.button_sqr(self.entry))
        button_mod = Button(self, image=self.button_image_mod, **button_style, command=lambda: butcntr.button_mod(self.entry))
        button_del = Button(self, image=self.button_image_del, **button_style, command=lambda: butcntr.button_del(self.entry))


        
        ####################################
        #                                  #
        # Put the buttons on the screen    #
        #                                  #
        ####################################

        topFrame.grid(row=0, column=0, columnspan=5, sticky="ew")
        topFrame.columnconfigure(0, weight=10)
        topFrame.grid_propagate(False)
        #topBG.grid(row=0, column=0, columnspan=5)

        #button_about.config(width=102)
        button_about.pack(fill=X, side="left")
        #button_help.config(width=130)
        button_help.pack(fill=X, side="left")
        button_color.pack(fill=X, side="left")
        date_label.pack(side="right", padx=20)

        #entry_bg_1.grid(row=1, column=0, rowspan=2, columnspan=5)
        entryFrame.grid(row=1, column=0, columnspan=5)
        entryFrame.columnconfigure(0, weight=10)
        entryFrame.grid_propagate(False)
        self.entry.grid(sticky="se")

        button_clear.grid(row=3, column=0)
        button_multiply.grid(row=3, column=1)
        button_divide.grid(row=3, column=2)
        button_del.grid(row=3, column=3)
        button_fact.grid(row=3, column=4)

        button_7.grid(row=4, column=0)
        button_8.grid(row=4, column=1)
        button_9.grid(row=4, column=2)
        button_add.grid(row=4, column=3)
        button_pow2.grid(row=4, column=4)

        button_4.grid(row=5, column=0)
        button_5.grid(row=5, column=1)
        button_6.grid(row=5, column=2)
        button_subtract.grid(row=5, column=3)
        button_pown.grid(row=5, column=4)

        self.button_1.grid(row=6, column=0)
        self.button_2.grid(row=6, column=1)
        button_3.grid(row=6, column=2)
        button_sqr2.grid(row=6, column=4)

        button_0.grid(row=7, column=0)
        button_dot.grid(row=7, column=1)
        button_mod.grid(row=7, column=2)
        button_sqrn.grid(row=7, column=4)

        button_eq.grid(row=6, column=3, rowspan=2)

        
    def open_about(self):
        window = About(self, color_bg, color_toppanel)
        window.grab_set()
    def open_help(self):
        window = Help(self, color_bg, color_toppanel)
        window.grab_set()
# Spusteni aplikace
if __name__ == "__main__":
    app = windows()
    app.resizable(False, False)
    app.mainloop()



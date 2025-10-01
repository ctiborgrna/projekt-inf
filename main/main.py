# TODO - toto by si nikdy nemal wildcardovat Marek :)
from tkinter import *

window = Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.geometry("{}x{}+0+0".format(screen_width, screen_height))
window.title("Logic Gates Simulator")
window.configure(bg="white")

import webbrowser

button_frame = Frame(window, bg="lightgray", height=100)
button_frame.pack(fill=X, side=TOP)
button_frame.pack_propagate(False)

buttons = [
    "INPUT",
    "OUTPUT",
    "NOT",
    "AND",
    "NAND",
    "OR",
    "NOR",
    "XOR",
    "XNOR",
    "TABULKA",
    "NASTAVENIA",
]

i = 0
buttons_obj = []
for text in buttons:
    btn = Button(button_frame, text=text, font=("Arial", 30))
    btn.grid(row=0, column=i, sticky="nsew", padx=2, pady=10)
    button_frame.grid_columnconfigure(i, weight=1)
    buttons_obj.append(btn)
    i += 1


canvas = Canvas(window, bg="white")
canvas.pack(fill=BOTH, expand=True)


def open_link(event):
    webbrowser.open_new("https://www.101computing.net/logic-gates-studio/")


link_text = canvas.create_text(
    screen_width / 2,
    screen_height / 2,
    text="SIMULATOR",
    font=("Arial", 64),
    fill="blue",
    anchor="center",
)
canvas.tag_bind(link_text, "<Button-1>", open_link)


bin_btn = Button(window, text="Kôš", font=("Arial", 16))
import_btn = Button(window, text="Import", font=("Arial", 16))
export_btn = Button(window, text="Export", font=("Arial", 16))


def center(event=None):
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    canvas.coords(link_text, canvas_width / 2, canvas_height / 2)
    w = window.winfo_width()
    h = window.winfo_height()
    bin_btn.place(x=w - 125, y=h - 65, width=120, height=60)
    import_btn.place(x=5, y=h - 65, width=120, height=60)
    export_btn.place(x=130, y=h - 65, width=120, height=60)


canvas.bind("<Configure>", center)

window.mainloop()

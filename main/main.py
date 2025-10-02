# TODO - toto by si nikdy nemal wildcardovat Marek :)
from tkinter import *

window = Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.geometry("{}x{}+0+0".format(screen_width, screen_height))
window.title("Logic Gates Simulator")
window.configure(bg="white")

#minimalna velkost okna aby sa tie ikony neglitchovali
#mozme potom zmenit/vymysliet ine riesenie
window.minsize(800, 600)

import webbrowser
from PIL import Image, ImageTk

button_frame = Frame(window, bg="lightgray", height=100)
button_frame.pack(fill=X, side=TOP)
button_frame.pack_propagate(False)

#loadujeme ikony
img_input=ImageTk.PhotoImage(Image.open("resources/IO/INPUT.png").resize((60, 40)))
img_output=ImageTk.PhotoImage(Image.open("resources/IO/OUTPUT.png").resize((60, 40)))
img_not = ImageTk.PhotoImage(Image.open("resources/switches/NOTswitch.png").resize((60, 40)))
img_and = ImageTk.PhotoImage(Image.open("resources/switches/ANDswitch.png").resize((60, 40)))
img_nand = ImageTk.PhotoImage(Image.open("resources/switches/NANDswitch.png").resize((60, 40)))
img_or = ImageTk.PhotoImage(Image.open("resources/switches/ORswitch.png").resize((60, 40)))
img_nor = ImageTk.PhotoImage(Image.open("resources/switches/NORswitch.png").resize((60, 40)))
img_xor = ImageTk.PhotoImage(Image.open("resources/switches/XORswitch.png").resize((60, 40)))
img_xnor = ImageTk.PhotoImage(Image.open("resources/switches/XNORswitch.png").resize((60, 40)))
img_table = ImageTk.PhotoImage(Image.open("resources/misc/table.png").resize((60, 40)))
img_settings = ImageTk.PhotoImage(Image.open("resources/misc/settings.png").resize((60, 40)))
img_import = ImageTk.PhotoImage(Image.open("resources/misc/import.png").resize((40, 40)))
img_export = ImageTk.PhotoImage(Image.open("resources/misc/export.png").resize((40, 40)))
img_bin1 = ImageTk.PhotoImage(Image.open("resources/misc/closedbin.png").resize((40, 40)))
img_bin2 = ImageTk.PhotoImage(Image.open("resources/misc/openbin.png").resize((40, 40)))

#robime buttony
buttons = [
    ("INPUT", img_input),
    ("OUTPUT", img_output),
    ("NOT", img_not),
    ("AND", img_and),
    ("NAND", img_nand),
    ("OR", img_or),
    ("NOR", img_nor),
    ("XOR", img_xor),
    ("XNOR", img_xnor),
    ("TABULKA", img_table),
    ("NASTAVENIA", img_settings),
]

i = 0
buttons_obj = []
for text, img in buttons:
    if img:
        btn = Button(button_frame, image=img, text=text, compound="top", font=("Arial", 12))
    else:
        btn = Button(button_frame, text=text, font=("Arial", 16))
    btn.grid(row=0, column=i, sticky="nsew", padx=2, pady=10)
    button_frame.grid_columnconfigure(i, weight=1)
    buttons_obj.append(btn)
    i += 1

#cavas
canvas = Canvas(window, bg="white")
canvas.pack(fill=BOTH, expand=True)

#text v strede
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

#spodne buttony
bin_btn1 = Button(window, image=img_bin1, font=("Arial", 16))
import_btn = Button(window, image=img_import, font=("Arial", 16))
export_btn = Button(window, image=img_export, font=("Arial", 16))

#aby sa to pekne centrovalo
def center(event=None):
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    canvas.coords(link_text, canvas_width / 2, canvas_height / 2)
    w = window.winfo_width()
    h = window.winfo_height()
    bin_btn1.place(x=w - 125, y=h - 65, width=120, height=60)
    import_btn.place(x=5, y=h - 65, width=120, height=60)
    export_btn.place(x=130, y=h - 65, width=120, height=60)
canvas.bind("<Configure>", center)

window.mainloop()

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
images_data = [
    ("resources/IO/INPUT.png", (60, 40)),
    ("resources/IO/OUTPUT.png", (60, 40)),
    ("resources/switches/NOTswitch.png", (60, 40)),
    ("resources/switches/ANDswitch.png", (60, 40)),
    ("resources/switches/NANDswitch.png", (60, 40)),
    ("resources/switches/ORswitch.png", (60, 40)),
    ("resources/switches/NORswitch.png", (60, 40)),
    ("resources/switches/XORswitch.png", (60, 40)),
    ("resources/switches/XNORswitch.png", (60, 40)),
    ("resources/misc/table.png", (60, 40)),
    ("resources/misc/settings.png", (60, 40)),
    ("resources/misc/import.png", (40, 40)),
    ("resources/misc/export.png", (40, 40)),
    ("resources/misc/closedbin.png", (40, 40)),
    ("resources/misc/openbin.png", (40, 40)),
]


icons = []
for path, size in images_data:
    if path:
        icon = ImageTk.PhotoImage(Image.open(path).resize(size))
    else:
        icon = None
    icons.append(icon)


#robime buttony
buttons = [
    ("INPUT", icons[0]),
    ("OUTPUT", icons[1]),
    ("NOT", icons[2]),
    ("AND", icons[3]),
    ("NAND", icons[4]),
    ("OR", icons[5]),
    ("NOR", icons[6]),
    ("XOR", icons[7]),
    ("XNOR", icons[8]),
    ("TABULKA", icons[9]),
    ("NASTAVENIA", icons[10]),
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
bin_btn1 = Button(window, image=icons[11], font=("Arial", 16))
import_btn = Button(window, image=icons[12], font=("Arial", 16))
export_btn = Button(window, image=icons[13], font=("Arial", 16))

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

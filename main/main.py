from tkinter import *
window=Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.geometry('{}x{}+0+0'.format(screen_width, screen_height))
window.title("Logic Gates Simulator")
window.configure(bg='white')

import webbrowser

button_frame = Frame(window, bg='lightgray', height=100)
button_frame.pack(fill=X, side=TOP)
button_frame.pack_propagate(False)

input=Button(button_frame, text="INPUT", font=('Arial', 30)).pack(side=LEFT, fill=BOTH, expand=True, padx=2, pady=10)
output=Button(button_frame, text="OUTPUT", font=('Arial', 30)).pack(side=LEFT, fill=BOTH, expand=True, padx=2, pady=10)
negacia=Button(button_frame, text="NOT", font=('Arial', 30)).pack(side=LEFT, fill=BOTH, expand=True, padx=2, pady=10)
konjunkcia=Button(button_frame, text="AND", font=('Arial', 30)).pack(side=LEFT, fill=BOTH, expand=True, padx=2, pady=10)
neg_konjunkcia=Button(button_frame, text="NAND", font=('Arial', 30)).pack(side=LEFT, fill=BOTH, expand=True, padx=2, pady=10)
disjunkcia=Button(button_frame, text="OR", font=('Arial', 30)).pack(side=LEFT, fill=BOTH, expand=True, padx=2, pady=10)
neg_disjunkcia=Button(button_frame, text="NOR", font=('Arial', 30)).pack(side=LEFT, fill=BOTH, expand=True, padx=2, pady=10)
exclusive_or=Button(button_frame, text="XOR", font=('Arial', 30)).pack(side=LEFT, fill=BOTH, expand=True, padx=2, pady=10)
neg_exclusive_or=Button(button_frame, text="XNOR", font=('Arial', 30)).pack(side=LEFT, fill=BOTH, expand=True, padx=2, pady=10)
table=Button(button_frame, text="TABULKA", font=('Arial', 30)).pack(side=LEFT, fill=BOTH, expand=True, padx=2, pady=10)
settings=Button(button_frame, text="NASTAVENIA", font=('Arial', 30)).pack(side=LEFT, fill=BOTH, expand=True, padx=2, pady=10)


canvas = Canvas(window, bg='white')
canvas.pack(fill=BOTH, expand=True)

def open_link(event):
    webbrowser.open_new("https://www.101computing.net/logic-gates-studio/")

link_text = canvas.create_text(screen_width/2, screen_height/2, text='SIMULATOR', font=('Arial', 64), fill='blue', anchor='center')
canvas.tag_bind(link_text, "<Button-1>", open_link)


bin_btn = Button(window, text="Kôš", font=('Arial', 16))
import_btn = Button(window, text="Import", font=('Arial', 16))
export_btn = Button(window, text="Export", font=('Arial', 16))

def center(event=None):
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    canvas.coords(link_text, canvas_width/2, canvas_height/2)
    w = window.winfo_width()
    h = window.winfo_height()
    bin_btn.place(x=w-125, y=h-65, width=120, height=60)
    import_btn.place(x=5, y=h-65, width=120, height=60)
    export_btn.place(x=130, y=h-65, width=120, height=60)

canvas.bind('<Configure>', center)

window.mainloop()
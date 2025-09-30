from tkinter import *
window=Tk()
window.geometry('{}x{}+0+0'.format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.title("Logic Gates Simulator")
window.configure(bg='white')

import webbrowser
canvas = Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight(), bg='white')
canvas.pack()

def open_link(event):
    webbrowser.open_new("https://www.101computing.net/logic-gates-studio/")

link_text = canvas.create_text(window.winfo_screenwidth()/2, window.winfo_screenheight()/2, text='SIMULATOR', font=('Arial', 64), fill='blue')
canvas.tag_bind(link_text, "<Button-1>", open_link)

canvas.create_oval(50, 150, 350, 250, outline='red', width=5)

window.mainloop()
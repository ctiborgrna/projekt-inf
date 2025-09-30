import tkinter
import webbrowser

def open_link(event):
    webbrowser.open_new("https://www.101computing.net/logic-gates-studio/")

canvas = tkinter.Canvas(width=400, height=400, bg='white')
canvas.pack()

link_text = canvas.create_text(200, 200, text='https://www.101computing.net/logic-gates-studio/', font=('Arial', 12), fill='blue')
canvas.tag_bind(link_text, "<Button-1>", open_link)

canvas.create_oval(50, 150, 350, 250, outline='red', width=5)
tkinter.mainloop()
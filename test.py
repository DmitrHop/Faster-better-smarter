from tkinter import *

win = Tk()
win.geometry("300x400")
win.title("color test")

color = "green"

box1 = Frame(win, bg = "blue", width = 200)
box1.pack()

text = Button(box1, text = "Hi!")
text.pack()



win.mainloop()
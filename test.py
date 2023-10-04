from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry("300x400")
win.title("color test")


const = 1

color = "green"

box1 = [0, 0]
for i in range(2):
	box1[i] = Frame(win, bg = "blue", width = 200, padx = 20)
	box1[i].pack()

text = Button(box1[0], text = "Hi!")
text.pack()

text2 = Label(grid = box1[1], text = "Hello")
text2.pack()

a = 2

win.mainloop()
from tkinter import *
from tkinter import ttk
from game import *

win = Tk()
win.geometry("800x400")
win.configure(bg = BGColor, padx = 10, pady = 10)
win.title("Game name")

# Functions

def AnswerToQues(ButNumber):
	QuNum = NextQuestion()
	AnswerVer(ButNumber, QuNum)
	SwitchText(QuNum)

def SwitchText(QuNum):
	if QuNum < QuestionAmount:
		for ButNum in range(AnswersAmount):
			ButtonArr[ButNum]["text"] = f"{Answers[QuNum][ButNum]}"
		QuestionText["text"] = f"{Questions[QuNum]}" 
	else:
		CorrectAnswers, IncorrectAnswers = AnswerVer()
		QuestionText["text"] = f"Amount of true answers = {CorrectAnswers}\nAmount of false answers = {IncorrectAnswers}"
		QuestionText["padx"] = 8
		QuitButton = Button(text = "Quit", height = 2, width = 10, 
							activeforeground = "white", borderwidth = "0",
							bg = Colors[0], activebackground = AcColors[0], font = "Arial 10 bold",
							command = quit)
		for ButtonNum in range(AnswersAmount):
			ButtonArr[ButtonNum].pack_forget()
		for AnsBoxNum in range(BoxesAmount):
			AnswerBox[AnsBoxNum].pack_forget()
		QuitButton.pack(anchor = "nw")

# FrontEnd

QuesBox = Frame(win, bg = BGColor)
QuesBox.pack(anchor = "nw")

AnswerBox = [0]*BoxesAmount

for BoxNum in range(BoxesAmount):
	AnswerBox[BoxNum] = Frame(bg = BGColor)
	AnswerBox[BoxNum].pack(anchor = "nw")

QuestionText = Label(QuesBox, justify = "left", bg = BGColor, text = f"{Questions[QuestionNum]}", font = "Arial 14 bold", padx = 8)
QuestionText.pack(anchor = "nw")

# Buttons

ButtonArr = [0] * AnswersAmount

for ButtonNum in range(AnswersAmount):
	ButtonArr[ButtonNum] = Button(AnswerBox[ButtonNum % BoxesAmount], text = f"{Answers[QuestionNum][ButtonNum]}",
								  height = 2, width = 10, 
								  activeforeground = "white", borderwidth = "0",
								  bg = Colors[ButtonNum], activebackground = AcColors[ButtonNum], font = "Arial 10 bold",
								  command = lambda ButNumber = ButtonNum: AnswerToQues(ButNumber))
	ButtonArr[ButtonNum].pack(side = LEFT, pady = 8, padx = 16)



win.mainloop()
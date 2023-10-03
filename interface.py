from tkinter import *
from tkinter import ttk
from game import *

win = Tk()
win.geometry("800x400")
win.resizable(width = False, height = False)
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
		QuestionText["text"] = f"Amount of true answers = {CorrectAnswers}\n Amount of false answers = {IncorrectAnswers}"
		QuestionText["padx"] = 8
		for ButtonNum in range(AnswersAmount):
			ButtonArr[ButtonNum].pack_forget()

# FrontEnd

AnswerBox = Frame(bg = BGColor)
AnswerBox.pack(anchor = "nw")



QuestionText = Label(AnswerBox, bg = BGColor, text = f"{Questions[QuestionNum]}", font = "Arial, 15", padx = 8)
QuestionText.pack(anchor = "nw")

# Buttons

ButtonArr = ["0"] * AnswersAmount

for ButtonNum in range(AnswersAmount):
	ButtonArr[ButtonNum] = Button(AnswerBox, text = f"{Answers[QuestionNum][ButtonNum]}",
								  height = 2,
								  width = 10, activeforeground = "white", borderwidth = "0", highlightbackground = "red",
								  bg = Colors[ButtonNum], activebackground = AcColors[ButtonNum], font = "Arialblack, 10",
								  command = lambda ButNumber = ButtonNum: AnswerToQues(ButNumber))
	ButtonArr[ButtonNum].pack(side = LEFT, pady = 4, padx = 8)



win.mainloop()
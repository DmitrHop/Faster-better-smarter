from tkinter import *
from tkinter import ttk
from game import *

win = Tk()
win.geometry("400x400")
win.resizable(width = False, height = False)
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
		for ButtonNum in range(AnswersAmount):
			ButtonArr[ButtonNum].pack_forget()

# FrontEnd

AnswerBox = Frame(height = 100)
AnswerBox.pack()

ButtonArr = ["0"] * AnswersAmount

QuestionText = ttk.Label(AnswerBox, text = f"{Questions[QuestionNum]}")
QuestionText.pack(anchor = "nw")

for ButtonNum in range(AnswersAmount):
	ButtonArr[ButtonNum] = ttk.Button(text = f"{Answers[QuestionNum][ButtonNum]}",
									  width = 10,
									  command = lambda ButNumber = ButtonNum: AnswerToQues(ButNumber))
	ButtonArr[ButtonNum].pack(anchor = "c", pady = 4)



win.mainloop()
from tkinter import *
from tkinter import ttk
from game import *

win = Tk()
win.geometry("200x100")
win.configure(bg = BGColor, padx = 10, pady = 10)
win.title("Game name")

# Functions

def AnswerToQues(BNum):
	QuNum = NextQuestion()
	AnswerVer(BNum, QuNum)
	SwitchText(QuNum)

def SwitchText(QuNum):
	if QuNum < QuestionAmount:
		for ButNum in range(AnswersAmount):
			ButtonArr[ButNum]["text"] = f"{Answers[QuNum][ButNum]}"
		QuestionTextLabel[0]["text"] = f"{Questions[QuNum]}"
	else:
		CorrectAnswers, IncorrectAnswers = AnswerVer()
		QuestionTextLabel[0]["text"] = f"Amount of true answers = {CorrectAnswers}\nAmount of false answers = {IncorrectAnswers}"
		QuestionTextLabel[0]["padx"] = 8
		QuitButton = Button(text = "Quit", height = 2, width = 10, 
							activeforeground = "white", borderwidth = "0",
							bg = Colors[0], activebackground = AcColors[0], font = "Arial 10 bold",
							command = quit)
		for ButtonNum in range(AnswersAmount):
			ButtonArr[ButtonNum].pack_forget()
		for AnsBoxNum in range(2):
			AnswerBox[AnsBoxNum].pack_forget()
		QuitButton.pack(anchor = "nw")

# FrontEnd

def MainQues(category):
	variables(category)
	Answers = CreateFun()

	QuesBox = Frame(win, bg = BGColor)
	QuesBox.pack(anchor = "nw")
	
	for BoxNum in range(2):
		AnswerBox[BoxNum] = Frame(bg = BGColor)
		AnswerBox[BoxNum].pack(anchor = "nw")
	QuestionTextLabel[0] = Label(QuesBox, justify = "left", bg = BGColor, text = f"{questions[QuestionNum]['question']['text']}", font = "Arial 14 bold", padx = 8)
	QuestionTextLabel[0].pack(anchor = "nw")
	for ButtonNum in range(4):
		ButtonArr[ButtonNum] = Button(AnswerBox[ButtonNum % 2], text = f"{Answers[QuestionNum][ButtonNum]}",
									  height = 4, width = 40,
									  activeforeground = "white", borderwidth = "0",
									  bg = Colors[ButtonNum], activebackground = AcColors[ButtonNum], font = "Arial 14 bold",
									  command = lambda i = ButtonNum: AnswerToQues(i))
		
		ButtonArr[ButtonNum].pack(side = LEFT, pady = 8, padx = 16)

# MainQues()

def category():
	categories = "science,film_and_tv,music,history,geography,art_and_literature,sport_and_leisure,general_knowledge,food_and_drink".split(",")
	print(len(categories))
	ButtonArr = [0] * len(categories)
	Box = [0] * 3
	for i in range(3):
		Box[i] = Frame(bg = BGColor)
		Box[i].pack(anchor = "nw")
	for i in range(len(categories)):
		ButtonArr[i] = Button(Box[i%3], text = categories[i],
							  height = 2, width = 20,
							  activeforeground = "white", borderwidth = "0",
							  bg = Colors[i], activebackground = AcColors[i], font = "Arial 14 bold",
							  command = lambda category = categories[i]: MainQues(category))
		ButtonArr[i].pack(side = LEFT, pady = 8, padx = 16)
	return categories

print(category())
win.mainloop()
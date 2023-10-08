from tkinter import *
from tkinter import ttk
from json import loads
from requests import get
from random import shuffle

#			red      blue        yellow     green      orange    purple     lime       dark blue
Colors = ["#FD7B7B", "#7F6AC2", "#FDE77B", "#69D869", "#FDC57B", "#A450A4", "#DFF477", "#5581A3"]
AcColors = ["#D14141", "#4A3490", "#D1B841", "#34A734", "#D19341", "#882A88", "#B2CA3F", "#306186"]

BGColor = "#F6FFB4"

questions = loads(get("https://the-trivia-api.com/v2/questions?category=science").text)

# задание переменных
Questions, Answers, TrueAnswers = [],[],[]
QuestionNum = 0
BoxesAmount = 1
QuestionAmount = len(questions)
AnswersAmount = len(questions[0]["incorrectAnswers"])+1

# создание листов ответов и вопросов
for question in questions:
	Questions.append(question["question"]["text"])
	TrueAnswers.append(question["correctAnswer"])
	answers = question["incorrectAnswers"]
	answers.append(question["correctAnswer"])
	shuffle(answers)
	Answers.append(answers)
print(Answers)
print(TrueAnswers)

Falses = 0
Trues = 0


# хрен знает зачем
if AnswersAmount % 4 == 0 and AnswersAmount > 8:
	BoxesAmount = 4
elif AnswersAmount % 3 == 0 and AnswersAmount > 6:
	BoxesAmount = 3
elif AnswersAmount % 2 == 0:
	BoxesAmount = 2

# увеличение номера вопроса, пока они не скажут ауминь
def NextQuestion():
	global QuestionNum
	global QuestionAmount
	if QuestionNum < QuestionAmount:
		QuestionNum += 1
	return QuestionNum

# проверка ответов пользователя
def AnswerVer(Num = None, Answer = None):
	global Trues
	global Falses
	if Num != None and Answer != None:
		if  TrueAnswers[Num] == Answer:
			Trues += 1
		else:
			Falses += 1
	return Trues, Falses
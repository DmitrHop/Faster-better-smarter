from tkinter import *
from tkinter import ttk
from json import loads
from requests import get
from random import shuffle

#			red      blue        yellow     green      orange    purple     lime       dark blue  pink        sand
Colors = ["#FD7B7B", "#7F6AC2", "#FDE77B", "#69D869", "#FDC57B", "#A450A4", "#DFF477", "#5581A3", "#C6659C", "#F7C57D"]
AcColors = ["#D14141", "#4A3490", "#D1B841", "#34A734", "#D19341", "#882A88", "#B2CA3F", "#306186", "#E3A5C8", "#FBD59E"]

BGColor = "#F6FFB4"

URL = "https://the-trivia-api.com/v2/questions"

questions = loads(get(f"{URL}?categories={category}").text)
print(questions[0]['category'])
Questions, Answers, TrueAnswers = [],[],[]
ButtonArr = [0] * 4
QuestionTextLabel = [0]
AnswerBox = [0]*2
QuestionNum = 0
BoxesAmount = 1
QuestionAmount = len(questions)
AnswersAmount = len(questions[0]["incorrectAnswers"])+1

# создание листов ответов и вопросов
def CreateFun():
	for question in questions:
		Questions.append(question["question"]["text"])
		TrueAnswers.append(question["correctAnswer"])
		answers = question["incorrectAnswers"]
		answers.append(question["correctAnswer"])
		shuffle(answers)
		Answers.append(answers)
	return Answers

Falses = 0
Trues = 0


# хрен знает зачем
# if AnswersAmount % 4 == 0 and AnswersAmount > 8:
# 	BoxesAmount = 4
# elif AnswersAmount % 3 == 0 and AnswersAmount > 6:
# 	BoxesAmount = 3
# elif AnswersAmount % 2 == 0:
# 	BoxesAmount = 2

# увеличение номера вопроса, пока они не скажут ауминь
def NextQuestion():
	global QuestionNum
	global QuestionAmount
	if QuestionNum < QuestionAmount:
		QuestionNum += 1
	return QuestionNum

# проверка ответов пользователя
def AnswerVer(BText = None, QuNum = None):
	global QuestionNum
	global Trues
	global Falses
	# print(BText)
	# if BText != None:
		# print(f"correct answer = {questions[QuestionNum-1]['correctAnswer']}")
		# print(f"text = {ButtonArr[BText]['text']}")
	try:
		if ButtonArr[BText]['text'] == questions[QuestionNum-1]['correctAnswer']:
			Trues += 1
		else:
			Falses += 1
	except TypeError:
		return Trues, Falses
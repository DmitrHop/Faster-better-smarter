from tkinter import *
from tkinter import ttk

QuestionAmount = 0
AnswersAmount = 0
Questions = 0
Answers = 0
TrueAnswers = 0
QuestionNum = 0

Falses = 0
Trues = 0

FileName = "questions/first"
FileSRC = FileName + ".qz"

# File reading

File = open(FileSRC, encoding = "UTF-8")

QuestionAmount, AnswersAmount = map(int, File.readline().split(", "))

Questions = [0]*QuestionAmount
TrueAnswers = [0]*QuestionAmount
Answers = [[0] * AnswersAmount for _ in range(QuestionAmount)]

for QuestionsAmountNum in range(QuestionAmount):

	Questions[QuestionsAmountNum] = File.readline().removesuffix("\n")

	TrueAnswers[QuestionsAmountNum] = File.readline().removesuffix("\n")

	for AnswersAmountNum in range(AnswersAmount):

		Answers[QuestionsAmountNum][AnswersAmountNum] = File.readline().removesuffix("\n")

File.close()

def NextQuestion():
	global QuestionNum
	global QuestionAmount
	if QuestionNum < QuestionAmount:
		QuestionNum += 1
	return QuestionNum

def AnswerVer(Num = None, AnswerNum = None):
	global Trues
	global Falses
	if Num != None and AnswerNum != None:
		if int(Num) == int(TrueAnswers[AnswerNum-1]):
			Trues += 1
		else:
			Falses += 1
	return Trues, Falses

print(f"True answers = {Trues}")
print(f"False answers = {Falses}")
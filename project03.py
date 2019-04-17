#生成随机测验的试卷
#35 students 
#需求:
''' 1.创建30个卷子
	2.每份50个选择
	3.一个正确三个错误答案
	4.写入35个文本
	5.答案写入35个文本

'''
#!python3
#randomQuizGenerator.py --Creates quizzes with questions and answers in 
#random order ,along with the answer key

import random

#The quiz data .Keys are states and value are their capital
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#Generator 35 quiz files:
for quiznum in range(35):
	#TO DO :create the quiz and answer key files
	quizFile=open('.\\Pr3Data\\Capitalsquiz%s.txt' % (quiznum+1),'w')
	answerFile=open('.\\Pr3Data\\Capitalsquiz_answer%s.txt' % (quiznum+1),'w')

	#TO DO :write out the header for the quiz
	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')#Period 周期
	quizFile.write((' '*20)+'State Capitals Quiz (Form %s)' %(quiznum+1))
	quizFile.write('\n\n')

	#TO DO :shuffle the order of the states
	states=list(capitals.keys())
	random.shuffle(states)

	#TO DO :Loop through all 50 states ,making a quesion for each
	for questionNum in range(50):

		#Get right and wrong answers.
		#print('questionNum is '+ str(questionNum))
		correctAnswer=capitals[states[questionNum]]
		wrongAnswers=list(capitals.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		wrongAnswers=random.sample(wrongAnswers,3)
		answerOptions=wrongAnswers+[correctAnswer]
		random.shuffle(answerOptions)

		#TO DO :Write the questions and answer options to the quiz file
		quizFile.write('%s . What is the capital of %s ?\n' %(questionNum+1,states[questionNum]))
		for i in range (4):
			quizFile.write('%s. %s\n' %('ABCD'[i],answerOptions[i]))
		quizFile.write('\n')

		#TO DO :Write the answer key to a file
		answerFile.write('%s. %s\n' %(questionNum+1,'ABCD'[answerOptions.index(correctAnswer)]))
	quizFile.close()
	answerFile.close()

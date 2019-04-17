''' 需求：
	1.创建30个卷子
	2.每份50个选择
	3.一个正确答案三个错误答案
	4.写入
'''

import random

#The quiz data
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

#Generator 35 quiz question files:
for quizNum in range(35):
		#TO DO :Create the quiz and answer key files
		quizFile=open('.\\r-Pr4Data\\Capitalsquiz%s.txt' %(quizNum+1),'w')
		answerFile=open('.\\r-Pr4Data\\Capitalsquiz_answer%s.txt' %(quizNum+1),'w')

		#TO DO:write out the header for the quiz
		quizFile.write('Name:\n\nDate:\n\nPeroid\n\n')
		quizFile.write('State Capitals Quiz (Form %s)'.center(50,'=') %(quizNum+1))
		quizFile.write('\n\n')

		#TO DO :shuffle the order of the states
		states=list(capitals.keys())
		random.shuffle(states)# 混乱states

		for questionNum in range(50):
			#Get right and wrong answer 
			correctAnswer=capitals[states[questionNum]]
			wrongAnswer=list(capitals.values())
			del wrongAnswer[wrongAnswer.index(correctAnswer)]
			wrongAnswer=random.sample(wrongAnswer,3)
			answerOptions=wrongAnswer+[correctAnswer]
			random.shuffle(answerOptions)

			#TO DO :write the question and answer options to the quiz file
			quizFile.write('%s.what is the capital of %s?\n' %(questionNum+1,states[questionNum]))
			for i in range(4):
				quizFile.write('%s. %s \n' %('ABCD'[i],answerOptions[i]))
			quizFile.write('\n')

			#write the answer key to a file
			answerFile.write('%s. %s' %(questionNum+1,'ABCD'[answerOptions.index(correctAnswer)]))
			answerFile.write('\n')
		quizFile.close()
		answerFile.close()
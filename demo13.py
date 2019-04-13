# 反复验证用户输入

while True:
	print('Enter you age:')
	age=input()
	if age.isdecimal():
		break
	else:
		print('Enter a number for your age')

while  True:
	print('Selct  a new password (letters and number only:)')
	password=input()
	if password.isalnum():
		break
	else:
		print('Please Enter a password')

def show():
	print('Your age is '+age)
	print('Your password is '+password)

show()

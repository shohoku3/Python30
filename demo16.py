# 口令保存箱

#!python 3
#pw.py -an insercure password locked program.

PASSWORD={'email':'F7ZMINSANSF',
			'blog':'sdasdasasd',
			'luggage':'1234587'}

import sys,pyperclip
if len(sys.argv)<2:#运行python 时使用的命令行参数
	print('Usage:python pw.py [account] -copy account password')
	sys.exit()

account=sys.argv[1]#first command line arg is the account name

if account in PASSWORD:
	pyperclip.copy(PASSWORD[account])
	print('Password for '+account+'copied to clipboard')
else:
	print('There is no account named '+ account)
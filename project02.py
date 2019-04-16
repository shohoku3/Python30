#电话号码和email地址提取程序
#!python3
#phoneAndEmail.py -Finds phone number and email address on the clipboard

import re,pyperclip

phoneRegex=re.compile(r'''(
	(\d{3}|\(\d{3}\))?  #area code 可以是3个数字也可以是（3）个数字
	(\s|-|\.)? #spearator
	(\d{3}) #first code
	(\s|-|\.)? #spearator
	(\d{4}) #last code
	(\s*(ext|x|ext\.)\s*(\d{2,5}))? #extension
	)''',re.VERBOSE)

#TODO:Create email regex
emailRegex=re.compile(r'''(
	[a-zA-Z0-9._%+-]+ #username
	@                 #@ sybmbol
	[a-zA-Z0-9._%+-]+ #domain name
	(\.[a-zA-Z]{2,4})
	)''',re.VERBOSE)
#TODO:Find matches in clipboard text.

#test type of clipboard
text=str(pyperclip.paste())
matches=[]#creat a new list
for groups in phoneRegex.findall(text):#groups 变量
	phoneNum='-'.join([groups[1],groups[3],groups[5]])
	if groups[8]!=' ':
		phoneNum+=' x '+groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])

#TODO:Copy results to the clipboard

if len(matches)>0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard')
	print('\n'.join(matches))
else:
	print('No phone number or email address found')
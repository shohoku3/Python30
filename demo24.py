#project
# 电话号码与E-mail 地址提取程序
# 需求:在长的文章中找出所有电话号码和邮件地址

#TODOLIST：
''' 1.剪切板获取文本
	2.找出文本中的phone && email
	3.结果粘贴到剪切板
'''
# 框架
''' 
	1.pyperclip module 
	2.re module 
	3.两个正则表达式 phoneRegex emailRegex
	4.findall()
	5.存放在字符串中str()
	6.else print(not found)
'''

#!python3
#phoneEmail.py -finds phone numbers and email addresses on the clipboard

import re,pyperclip

phoneRegex=re.compile(r'''(
	(\d{3}|\(\d{3}))?  #area code
	(\s|-|\.)?  #sperator
	(\d{3})  #first code
	(\s|-|\.)? #sperator
	(\d{3})  #last code
	(\s*(ext))))

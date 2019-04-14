#自动化任务篇
#模式匹配与正则表达式


# 不使用正则表达式查找文本模式
def isPhoneNumber(text):
	if len(text)!=12:
		return False
	for i in range(0,3):
		if not text[i].isdecimal():
			return False
	if text[3]!='-':
		return False
	for i in range(4,7):
		if not text[i].isdecimal():
			return False
	if text[7]!='-':
		return False
	for i in range(8,12):
		if not text[i].isdecimal():
			return False
	return True

print('415-123-2232 is a phone number ：')
print(isPhoneNumber('415-123-2232'))
msg='call me at 565-244-2332 tomorrow.423-231-1121 is my office'
for i in range(len(msg)):
	chunk=msg[i:i+12]
	if isPhoneNumber(chunk):
		print('Phone number found: '+chunk)
print('Done')



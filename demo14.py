#startwith() and endswith()

spam ='hello world'
print(spam.startswith('hello'))
print(spam.endswith('world'))

#join() 和 split()
#join() 链接字符串列表
print('.'.join(['cat','mom','dog']))
print(' '.join(['my','name','is','syf']))
#split 返回一个字符串列表
print('my name is syf'.split())
print('mymnamemismsyf'.split('m'))

spam2=''' Dear syf
How are you today.
I am fine .
thank you.
'''
print(spam2.split('\n'))

#rjust() ljust() center()
#用于对齐以及填充字符 参数为输入几个空格

# 打印野餐数目
def printPicnic(itemDict,leftWidth,rightWidth):
	print('PICNIC ITEMS'.center(leftWidth+rightWidth,'-'))
	for k,v in itemDict.items():
		print(k.ljust(leftWidth,'.')+str(v).rjust(rightWidth))

pinicItem={'apple':4,'ham':12,'cup':2,'banana':12}

printPicnic(pinicItem,12,5)




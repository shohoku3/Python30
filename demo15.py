#使用rjust() ljust() 等方法打印 数据

def printPicnic(itemDict,leftwidth,rightwidth):
	print('PICNIC ITEM'.center(leftwidth+rightwidth,'-'))
	for k,v in itemDict.items():
		print(k.ljust(leftwidth,'.')+str(v).rjust(rightwidth))

pinicitem={'apple':12,'cups':5,'ham':12}
pinicitem.setdefault('banana',0)

printPicnic(pinicitem,12,5)

allGuest={'alice':{'apple':5,'ham':12},'bacon':{'apple':12,
'banana':21},'clic':{'cup':12,'ham':12}}

def totalGuestBrought(guests,item):
	broughtNum=0
	for k,v in guests.items():
		broughtNum=broughtNum+v.get(item,0)
		return broughtNum

print('TOTALBROUGHT'.center(20,'-'))
print('Apple'.ljust(5,'-')+str(totalGuestBrought(allGuest,'apple')).rjust(10,'.'))

#strip() rstrip() lstrip()
#strip 剥去 条纹 纸带
spam=' Hello World '
print(spam.strip())






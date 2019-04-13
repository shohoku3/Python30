# 记录野餐数据

allGuest={'Alice':{'apple':5,'pretzel':12},
'Bob':{'ham':6,'apple':4},
'Crole':{'apple':10,'cups':3,'Cake':2}}

def totalBrought(guests,item):
	numBrought=0
	for k,v in guests.items():
		numBrought=numBrought+v.get(item,0)
	return numBrought

print('Number of thing being brought:')
print(' - Apples '+ str(totalBrought(allGuest,'apple')))
print(' - Pretzel '+ str(totalBrought(allGuest,'pretzel')))
print(' - Cakes '+str(totalBrought(allGuest,'Cakes')))
print(' - Mike '+str(totalBrought(allGuest,'mike')))


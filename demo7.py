#输入列表catName
catNames=[]
while True:
    print('Enter the name of cat '+str(len(catNames)+1)+' or enter nothing to end')
    name=input()
    if name=='':
        break
    catNames=catNames+[name] #list concatenation
print('the cat name are:')
for name in catNames:
    print(''+name)
if 'syf' in catNames:
    print('syf is in list')
else:
    print('none')

supplies=['pens','staplers','flame-throwes','biner']
for i in range(len(supplies)):#i为变量
    print('Index ' + str(i)+ ' in supplies is ' + supplies[i])
    

#list concation 
catNames=[] # 初始化列表

while True:
    print('Enter the name of cat' + str(len(catNames)+1))
    name=input()
    if name == '':
        break
    catNames=catNames+[name] #list concatentaion
print('the cat names are:')
for name in catNames:
    print(' '+name)

    
   	
    


#读写文件
import os
pa=os.path.join('user','bin','spam')
print(type(pa))

myFiles=['account.txt','detail.csv','invite.docx']
for filename in myFiles:
	print(os.path.join('e:\\git',filename))

pa2=os.getcwd()
print(pa2)

pa3=os.chdir('c:\\windows\\system32')
pa3=os.getcwd()#current working directory
print(pa3)

#absolute relative path
#absolute path: root begin
#relative path: 相对程序的工作路径
# ..父文件夹的缩写 .当前文件夹
pa4=os.getcwd()
print(pa4)
pa5=os.chdir('e:\\git\\python30')
pa5=os.getcwd()
print(pa5)
#pa6=os.mkdir('test')
pa6=os.path.abspath('.')
print(pa6)
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))
print(os.path.relpath('e:\\git','e:\\'))
path='c:\\windows\\system32\\calc.exe'
print(os.path.dirname(path))
print(os.path.basename(path))

calFilepath='c:\\windows\\system32\\calc.exe'
print(type(os.path.split(calFilepath)))#tuple
print(os.path.split(calFilepath))

print((os.path.basename(calFilepath),os.path.dirname(calFilepath)))
#使用split() 返回一个字符串列表
print(calFilepath.split(os.path.sep))
print(type(calFilepath.split(os.path.sep)))

#file size file content
print(os.path.getsize('e:\\git\\python30'))
print(os.listdir('e:\\git\\python30'))#type:list 

#total file size
totalfielsize=0
for filename in os.listdir('e:\\git\\python30'):
	totalfielsize=totalfielsize+os.path.getsize(os.path.join('e:\\git\\python30',filename))
print(totalfielsize)

totalfielsize2=0
for filename in os.listdir('e:\\git\\python30'):
	totalfielsize2=totalfielsize2+os.path.getsize(filename)
print(totalfielsize2)

#checkout path valid
print(os.path.exists('c:\\syf\\cc'))
print(os.path.isfile('e:\\git\\python30\\demo11.py'))
print(os.path.isdir('e:\\git\\python30'))

#chechout flashcard is access
print(os.path.isdir('d:'))


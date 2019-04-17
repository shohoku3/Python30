#read write
#open file
import os

#write():写入文件
baconFile=open('e:\\git\\python30\\test.py','w')
baconFile.write('hello world!\n')
baconFile.close()
baconFile=open('e:\\git\\python30\\test.py','a')
baconFile.write('how are you')
baconFile.close()
baconFile=open('e:\\git\\python30\\test.py')
content=baconFile.read()
baconFile.close()
print(content)



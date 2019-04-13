#Wiki中加入无序列表
#!python 3
#bulletPointAdder.py -Adds wikipedia bullet points to the start

import pyperclip
print('Please copy text in your clipboard')
text=pyperclip.paste()

#separate line and add start
lines=text.split('\n')
for i in range(len(lines)):
	#loop through all indexs in the "lines" list
	lines[i] =' * '+lines[i]
	text='\n'.join(lines)

pyperclip.copy(text)
print(pyperclip.paste())



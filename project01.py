#需求:将剪切板中的内容加星号
import pyperclip

text=pyperclip.paste()

lines=text.split('\n')
for i in range(len(lines)):
	lines[i]='*'+lines[i]
text='\n'.join(lines)
pyperclip.copy(text)

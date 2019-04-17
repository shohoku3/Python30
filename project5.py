#多重剪切板
''' 需求：
1.填充网页中的软件中的许多表格
2.不显示终端
3.mcb 程序
'''

#!pyhotn3
#mcb(multiclipboard) --save and load pices of text to the clipboard

#Usage :py.exe mcd.pyw save <KeyWord> -save clipboard to the keyword
#      :py.exe mcd.pyw <Keyword> -Loads keywords to clipboard 
#      :py.exe mcd.pyw list -Loads all keywords to clipboard

import shelve ,pyperclip ,sys
mcbShelf=shelve.open('.\\Pr5Data\\mcb')

#TODO: save clipboard content
print('Multiclipboard'.center(80,'='))
print('''
	Usage :py.exe mcd.pyw save <KeyWord> --save clipboard to the keyword
          :py.exe mcd.pyw <Keyword> --Loads keywords to clipboard 
		  :py.exe mcd.pyw list --Loads all keywords to clipboard
	''')
if len(sys.argv)==3 and sys.argv[1].lower()=='save':
	mcbShelf[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv)==2:
	#TODO:List keywords and load content
	if sys.argv[1].lower()=='list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

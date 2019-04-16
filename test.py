import re

finRegex=re.compile(r'\d')
finRegex2=re.compile(r'(\d\d\d)(\d\d\d)')
moss1=finRegex.findall('123 add 123 equal 246')
moss2=finRegex2.findall('123123 213123 123123')
print(type(moss1))
print(type(moss2))































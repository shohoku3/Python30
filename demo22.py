#demo22.py
#贪心匹配和非贪心匹配
#python 的正则表达式默认是贪心的模式

#eg.

import re
greedyHaReg=re.compile(r'(Ha){3,5}')
mo1=greedyHaReg.search('HaHaHaHaHa')
print(mo1.group())

nogreedyHaReg=re.compile(r'(Ha){3,5}?')
mo2=nogreedyHaReg.search('HaHaHaHaHa')
print(mo2.group())

#findall()
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo3=phoneNumRegex.findall('cell is 412-233-4355 work is 324-223-4343')
print(mo3)

#字符分类
xmasReg=re.compile(r'\d+\s\w+') #+表示匹配一次或多次
mo4=xmasReg.findall('12 dums, 11 pices ,4 cups ,23 lords, 8 mails')
print(mo4)

#建立字符分类
vowelRegex=re.compile(r'[aeiouAEIOU]') #[自定义字符分类]
moss=vowelRegex.findall('Robocp eats baby food.BABY FOOD')
print(moss)

#开始与结束匹配
beginWithHello=re.compile(r'^hello')
moss1=beginWithHello.search('hello world')
print(moss1.group())

endWithNum=re.compile(r'\d$')
moss2=endWithNum.search('number is 42')
print(moss2.group())

wholeStringNum=re.compile(r'^\d+$')
moss3=wholeStringNum.search('12312312312')
print(moss3.group())


#unicode 统配符
atRegex=re.compile(r'.at')
moss4=atRegex.findall('The cat in the hat sat on the flat mat')
print(moss4)

#.* 重复匹配任意字符
nameRegex=re.compile(r'First Name:(.*) Last Name:(.*)')
moss5=nameRegex.search('First Name:AI Last Name:SYF')
print(moss5.groups())

#DOTALL 参数

#re.I 不区分大小写




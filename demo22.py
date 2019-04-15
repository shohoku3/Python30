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
print(mo2)
print(mo2.group())

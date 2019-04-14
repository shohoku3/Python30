#模式匹配进阶
#利用括号进行模式匹配分组
import re

phoneNumRegx2=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')#regex 对象
mo=phoneNumRegx2.search('my number is 415-412-2323.')#search() 对象
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())

print(mo.groups())
areacode,maincode=mo.groups()
print(areacode)
print(maincode)
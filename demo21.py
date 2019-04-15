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

#匹配多个分组
heroRegex=re.compile(r'Batman|Tina Fey')
mo1=heroRegex.search('Batman and Tina Fey')
print(mo1.group())#group() 不加参数则是返回全部

mo2=heroRegex.search('Tina Fey and Batman')
print(mo2.group())

batRexgex=re.compile(r'Bat(man|moblie|copter|bat)')
mo=batRexgex.search('Batmoblie lost a wheel')
print(mo.group())
print(mo.group(1))
#?号可选匹配
bat2Rexgex=re.compile(r'Bat(wo)?man')
mo3=bat2Rexgex.search('the adventures of Batman')
print(mo3.group())

phoneNumRex=re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo4=phoneNumRex.search('my number is 425-234-2332')
print(mo4.group())

mo5=phoneNumRex.search('my number is 453-3434')
print(mo5.group())

#* 通用匹配
batRex=re.compile(r'Bat(wo)*man')#匹配0次或多次
mo6=batRex.search('my name is Batman')
mo7=batRex.search('my name is Batwowowoman')
mo8=batRex.search('my name is Batwoman')
print(mo6.group())
print(mo7.group())
print(mo8.group())

#+匹配
batRex3=re.compile(r'Bat(wo)+man')#匹配一次或多次
mo9=batRex3.search('my name is Batwoman')
print(mo9.group())

#{}多次匹配
haxReg=re.compile(r'(Ha){3}')
mo10=haxReg.search('HaHaHa')
print(mo10.group())

mo11=haxReg.search('HaHa')
if mo11== None:
	print('None')

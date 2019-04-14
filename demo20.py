#使用正则表达式查找文本模式
#正则表达式

#regex 文本描述模式
import re
phoneNumRegx=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')#变量引用了正则表达式 创造regex对象 字符串中使用r参数进行转义 
mo=phoneNumRegx.search('My number is 415-555-4242')#search()方法返回一个Match对象 并保存在mo当中
print('Phone number found:' +mo.group())



#demo10.py

# get() 和 setdefault()

#get() 用来检查元素是否在其中 if 不存在返回0
picinicItems={'apple':5,'cups':2,'bananas':40}
print('I am bringing '+str(picinicItems.get('apple',0))+' apple')
print('I am bringing '+str(picinicItems.get('chicken',0))+' chicken')

# setdefault() 判断元素是否存在  if 不存在则设置默认值
spam ={'name':'pooka','age':'5'}
spam.setdefault('color','red')
spam.setdefault('name','pooka')
print(spam)

#漂亮打印 message 中的数据
import pprint
message = 'It was a bright cold in April,and the clocks were striking'
count={}

for char in message:# char 是随机的变量
	count.setdefault(char,0)
	count[char]=count[char]+1

pprint.pprint(count)



	

# 结构化数据 字典

# 比较字典与列表
spam =['cats','dogs','mosses']
bacon=['dogs','cats','mosses']
if spam == bacon:
	print('两个 list相同')
else:
	print('两个list 不同')

eggs={'name':'zomap','age':'8'}
ham={'age':'8','name':'zomap'}
if eggs==ham:
	print('两个字典相同')
else:
	print('两个字典不同')

# values() keys() items()
for v in eggs.values():
	print(v)
for i in eggs.items():
	print(i)
for k in eggs.keys():
	print(k)

#保存朋友的生日
birthday={'Alice':'Apir 1','Syf':'Oct 02'}

while True:
	print('Enter a name: (blank to quit)')
	name=input()
	if name == '':
		break
	if name in birthday:
		print(birthday[name]+'is the birthday of '+name)
	else:
		print('I do not have birthday info for' + name)
		print('Please input')
		bday=input()
		birthday[name]=bday
		print('birthday info is update')

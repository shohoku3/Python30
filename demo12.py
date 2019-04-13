#String

print("hello world ' ")
print('hello world \' ')
print(r'hello world \' ')
print(''' hello world
	 what is your name,gues
	 ''')

""" this is the test python program
Written by alice sweight

thsi program was designed for python 3,not python 2
"""

def spam():
	"""thsi is a mulyiline comment to help
	explain what the spam() function does.
	print('hello ')
	""" 

# Strign split
spam ="hello world"
print(spam[0])
print(spam[4])
print(spam[-1])
print(spam[0:5])

if 'hello' in spam:
	print('hello in spam')
else:
	print('hello not in spam')

#字符串方法
print(spam.upper())
print(spam.lower())

print('How are you today')
feeling =  input()
if feeling.lower() == 'great':
	print('I feeling great today')
else:
	print('I hope the rest of your day is good')

# islower()
# isupper()

if 'Hello'.islower():
	print('yes')
else:
	print('no')	
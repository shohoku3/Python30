#sub()匹配方
#subsititue
import re
nameRegex=re.compile(r'^Agent\w+')
moss=nameRegex.sub('Cenert','Agent Alice gave the secert document to Agent BOb')
print(moss)

phoneRegex=re.compile(r'''(
	(\d{3}|\(\d{3})\)? #area code
	(\s|-|\.)? #sperator 
	\d{3} #first 3 digits
	(\s|-|\.)  #sperator
	\d{4}  #last 4 digits
	(\s*(ext|x|ext.)\s*\d(2,5))?
	)''',re.VERBOSE)
#使用管道运算符进行替换

someRegexValue=re.compile('foo',re.IGNORECASE|re.VERBOSE|re.DOTALL)


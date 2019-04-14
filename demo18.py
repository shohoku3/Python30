# printTable() 函数 组织良好的列表 每列右对齐
#每列右对齐

tableData=[['apples', 'oranges', 'cherries', 'banana'],
           ['Alice', 'Bob', 'Carol', 'David'],
           ['dogs', 'cats', 'moose', 'goose']]

#print(str(len(tableData))) #打印子列表数
#初始化一个列表用以记录每列的最长长度
def printTable(tableData):
	colWidths=[0]*len(tableData)
	col=[]
	for i in range(len(colWidths)):
		for j in range(len(tableData[i])):
			col.append(len(tableData[i][j]))
			max_len=max(col)
	for i in range(len(colWidths)):		
		for j in range(len(tableData[i])):
			print(tableData[i][j].rjust(max_len),end='')
		print()

printTable(tableData)		
#print(colWidths)


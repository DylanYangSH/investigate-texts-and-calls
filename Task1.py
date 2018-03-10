"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""

'''
#方法1，用2次循环遍历，类似其他语言
numbers = []
for i in range(len(texts)):
	for j in range(2):
		if texts[i][j] not in numbers:
			numbers.append(texts[i][j])
for i in range(len(calls)):
	for j in range(2):
		if calls[i][j] not in numbers:
			numbers.append(calls[i][j])
count = len(numbers)
print("There are {} different telephone numbers in the records.".format(count))
'''

#方法二，用2次循环遍历，利用集合省去判断环节
numbers = set()
for i in range(len(texts)):
	for j in range(2):
		numbers.add(texts[i][j])
for i in range(len(calls)):
	for j in range(2):
		numbers.add(calls[i][j])
count = len(numbers)
print("There are {} different telephone numbers in the records.".format(count))


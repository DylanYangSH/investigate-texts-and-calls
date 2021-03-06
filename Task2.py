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
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""

#通话总时长字典
total_time = {}

#定义计算总通话时长的函数，生成字典
def cal_time(phone_number,during_time):
	if phone_number not in total_time:
		total_time[phone_number] = int(during_time)	#转化为整型很有必要！
	else:
		total_time[phone_number] += int(during_time)

#主叫和被叫号码都通过调用函数来加入字典
for call in calls:
	cal_time(call[0],call[3])
	cal_time(call[1],call[3])

#测试一下
#print(total_time)
#存最长通话时长的号码
max_total_time_number = []
#存最长时长
max_time = 0
#遍历字典找出最长时长
for ph_number in total_time:
	if total_time[ph_number] > max_time:
		max_total_time_number = []
		max_total_time_number.append(ph_number)
		max_time = total_time[ph_number]
	elif total_time[ph_number] == max_time and not (ph_number in max_total_time_number):
		max_total_time_number.append(ph_number)

#打印最长通话时长号码和最长时长
if len(max_total_time_number) == 1:
	print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_total_time_number[0],max_time))
	

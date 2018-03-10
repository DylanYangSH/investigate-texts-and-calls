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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

calls_calling = set()
calls_called = set()
texts_send = set()
texts_receive = set()
normal_numbers = set()
#分别提取全部号码到集合中
for call in calls:
	calls_calling.add(call[0])
	calls_called.add(call[1])
for text in texts:
	texts_send.add(call[0])
	texts_receive.add(call[1])
#正常号码集合合并
normal_numbers = set(list(calls_called) + list(texts_send) + list(texts_receive))

#代码测试
#print(normal_numbers)


abnormal_numbers = []	#异常（可疑）号码列表
#方法1,flag标记法
'''
for calling_number in calls_calling:
	flag = 0
	for normal_number in normal_numbers:
		if calling_number == normal_number:
			flag = 1	#存在被叫记录
			break
	if flag == 0:	#确认异常则加入可疑列表
		abnormal_numbers.append(calling_number) 
'''

#方法2，善用in方法！！！
for calling_number in calls_calling:
	if calling_number not in normal_numbers:	#对每一个主叫电话号码判断是否在normal_numbers列表里
		abnormal_numbers.append(calling_number)

#代码测试
#print(abnormal_numbers)
abnormal_numbers.sort()	#列表按字典顺序排序
print("These numbers could be telemarketers:")
for abnormal_number in abnormal_numbers:	#分行输出
	print(abnormal_number)

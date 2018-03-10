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
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""

#Part1
prefixer = set()
bangalore_calling = 0	#part2, 打出电话次数总数
bangalore_called = 0	#part2, 其中被叫次数总数
for call in calls:
	if "(080)" == call[0][0:5]:
		bangalore_calling +=1	#计算bangalore打出电话次数总数
		if "(0" == call[1][0:2]:	#校验左括号很有必要！
			index = call[1].find(")")
			#print(index) 这里忽略了index可能为-1的情形！所以需要校验左括号（ 。
			prefixer.add(call[1][0:index+1])
			#print(call[1][0:index+1])	#测试代码
		elif " " in call[1] and (call[1][0]=='7' or call[1][0]=='8' or call[1][0]=='9'):
			prefixer.add(call[1][0:4])
		elif "140" == call[1][0:3]:
			prefixer.add(call[1][0:4])

		if "(080)" == call[1][0:5]:
			bangalore_called +=1	#计算bangalore拨出电话中bangolore被叫次数总数

#测试
#print(prefixer)	#发现输出第一个元素是''，不解，需询问！！！
prefixer = sorted(prefixer)
print("The numbers called by people in Bangalore have codes:")
for pre in prefixer:
	print(pre)
#测试
#print(prefixer)	#发现输出第一个元素是''，不解，需询问！！！


#Part2
#理解1，求通话次数比例
percentage = round(bangalore_called/bangalore_calling*100,2)
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))

#Part2
#理解2，求电话号码比例,应该不是这么理解

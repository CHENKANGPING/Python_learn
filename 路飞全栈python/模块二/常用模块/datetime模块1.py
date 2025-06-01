import datetime

# datetime.time
# datetime.date
# datetime.datetime
# datetime.timedelta

# datetime.datetime:

# (1)创建日期对象
# 获取当前日期对象
# now = datetime.datetime.now()
# print(now,type(now))
# today = datetime.datetime.today()
# print(today,type(today))

# 创建任意日期对象
# my = datetime.datetime(2020,12,23,0,0)
# print(my)

# (2) datetime对象的属性 对象.变量名

# now = datetime.datetime.now()
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

# （3） datetime对象和格式化字符串转换
# now = datetime.datetime.now()
# s = now.strftime("%Y/%m/%d %H:%M:%S")
# print(s)

# 将字符串转对象
# timer = "2020 12 20 10:0:0"
# s = datetime.datetime.strptime(timer, "%Y %m %d %H:%M:%S")
# print(s)












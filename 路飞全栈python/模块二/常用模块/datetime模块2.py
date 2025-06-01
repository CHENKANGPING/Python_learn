# 创建日期对象
import datetime
# today = datetime.date.today()
# print(today)

# mydate = datetime.date(2020, 12,20)
# # print(# mydate)

# 对象的属性
# print(today.year)
# print(today.month)
# print(today.day)

# 将日期对象转为格式化字符串

# ret = mydate.strftime("%d/%m/%Y")
# print(ret)


# datetime.timedelta:时间间隔
# my_date1 = datetime.date(2020, 12, 31)
# my_date2 = datetime.date(2019, 12, 31)
#
# delta = my_date1 - my_date2
# print(delta.days)
# print(delta.total_seconds())

now = datetime.datetime.now()
f =  now + datetime.timedelta(weeks=1)
print(f)

f2 =  now - datetime.timedelta(weeks=4)
print(f2)


































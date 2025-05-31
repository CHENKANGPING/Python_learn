"""
time() 返回从1970年1月1日午夜开始进过的秒数

sleep(secs) 暂停指定的秒数

localtime（secs） 将秒数转换为当前时区的stuct_time对象。

mktime（t） 将struct_time对象转换为秒数

gmtime(secs) 将秒数转换为UTC时间的struct_time对象

strftime（format, t) 将时间元组对象t按指定的格式format进行格式化输出

"""
import time

# print(time.time()/3600/24/365)


# print("start")
# time.sleep(10)
# print("end")


# print(time.localtime())

# c = time.mktime(time.localtime())
# print(c)
#
# g =time.gmtime(c)
# print(g)


c =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(c)
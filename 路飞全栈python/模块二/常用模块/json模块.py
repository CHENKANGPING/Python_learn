"""
序列化是将胡数据数据结构 或 对象转换为字节流（二进制数据）
以便储存或传输

返序列化 是将字节流还原为原始数据结构 或 对象的过程
Python        -         json
dict          -         object
list, tuple   -         array
str           -         string
int,float     -         number
True          -         true
False         -         false
None          -         null

"""

import json

# 序列化 ： 将本语言支持的高级数据对象转换为json格式字符串的过程

# num = 3,14
# name = "ckp"
# l = [1,2,3,4,5]
# t = (4,5,6)
# d = {"name":"ckp","age":18,"is_married" : False,"gf":None}
#
# print(repr(json.dumps(num)))# '3.14'
# print(repr(json.dumps(name))) # '"ckp"'
# print(repr(json.dumps(l))) # '[1,2,3,4,5]'
# print(repr(json.dumps(t))) # '[4,5,6]'
# print(repr(json.dumps(d))) # '{"name" : "ckp","age" : 18, "is_married" : false, "gf":null}'

# 存储和传输

# 反序列化 ： 将json格式的字符串转为本语言支持的数据对象格式


# d = {"name":"ckp","age":18,"is_married" : False,"gf":None}
#
# json_d = json.dumps(d)
# print(json_d,type(json_d))
#
# date = json.loads(json_d)
#
# print(date,type(date))
#
# name = date.get("name")
# print(name,type(name))



# d = {"name":"ckp","age":18,"is_married" : False,"gf":None}
#
# data = json.loads(json.dumps(d))
#
# print(data,type(data))
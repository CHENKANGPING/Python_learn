# 字符串进行编码， 得到新的数据类型：字节
# s = "yuan"
# ret = s.encode("utf8")
# print(ret)
# print(type(ret))

# s = "陈"
# ret = s.encode("gbk")
# print(ret)
# print(type(ret))


# 将字符串解码成字符串

data = b' \xb3\xc2'
print(type(data))

ret = data.decode()
print(ret)


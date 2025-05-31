# 返回的是一个文件的操作句柄
f = open("hello.txt", mode="r", encoding="gbk")
# 读所有字符
data = f.read()
print(data)
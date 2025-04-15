# 整型（int）
print(0b001)  #二进制整数 
print(0o100)  # 八进制整数
print(100)    # 十进制整数
print(0x100)  # 十六进制整数

#浮点数（float）
print(123.456)  # 数学写法
print(1.23456e2)  # 科学计数法

# 字符串型（str）：是以单引号或双引号包括起来的任意文本 'hello' "hello"
# 布尔型（bool）：只有True和False

print('------------------------')

# 变量命名
a = 45
b = 12
print(a, b)
print(a + b)
print(a - b)
print(a * b)
print(a / b)

print('------------------------')

#type函数检查变量的类型
a = 100
b = 123.45
c = 'hello, wold'
d = True
print(type(a)) # <class'int'>
print(type(b)) # <class'float'>
print(type(c)) # <class'str'>
print(type(d)) # <class'bool'> 

print('------------------------')

# 变量的类型转化
a = 100
b = 123.45
c = '123'
d = '100'
e = '123.45'
f = 'hello, world'
g = True
print(float(a)) # int -> flot = 100.0
print(int(b)) # flot -> int = 123
print(int(c)) # str -> int = 123
print(int(c, base=16)) # str -> int(base = 16) = 291
print(int(d, base=2)) # str -> int(base = 2) = 4
print(float(e)) # str -> flot = 123.45
print(bool(f)) # str -> bool = True
print(int(g)) # bool -> int = 1
print(chr(a)) # int -> str = 'd'
print(ord('d'))# str -> int = 100


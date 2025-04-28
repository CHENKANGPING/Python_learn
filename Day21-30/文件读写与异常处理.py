""" 
    打开和关闭文件
    open函数
    'r' 读取
    'w' 写入
    'x' 写入 如文件已经存在会产生异常
    'a' 追加 将内容写入到已有文件
    'b' 二进制模式
    't' 文本模式
    '+' 更新(既可以读又可以写)
    
"""
# 读写文本文件致橡树.txt
file = open('Day21-30\致橡树.txt', 'r', encoding = 'utf-8')
print(file.read())
file.close()


print('--------------------------------------------------')


file = open('Day21-30\致橡树.txt', 'r', encoding = 'utf-8')
for line in file:
    print(line, end='')
file.close()






file = open('Day21-30\致橡树.txt', 'r', encoding = 'utf-8')
lines = file.readlines()
for line in lines:
    print(line, end='')
file.close()





file = open('Day21-30\致橡树.txt', 'a', encoding = 'utf-8')
file.write('\n标题: 《致橡树》')
file.write('\n作者: 舒婷')
file.write('\n时间: 1977年3月')
file.close()


"""
    异常处理机制
    使用python的异常机制对可能在运行时发生状况的代码进行适当的处理
    python中和异常相关的关键字有五个
    try except else finally raise
    
"""
file = None
try:
    file = open('Day21-30\致橡树.txt', 'r', encoding = 'utf-8')
    print(file.read())
except FileNotFoundError:
    print('无法打开指定的文件！')
except LookupError:
    print('指定了未知的编码！')
except UnicodeDecodeError:
    print('读取文件时解码错误！')
finally:
    if file:
        file.close()
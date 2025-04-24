# 装饰器
# 用一个函数装饰另一个函数并为其提供额外能力的语法现象
# 装饰器本身是一个函数
# 它的参数是被装饰的函数
# 它的返回值是一个带有装饰功能的函数
# 下面举个例子
import time
import random
def download(filname):
    """下载文件"""
    print(f'开始下载{filname}.')
    time.sleep(random.random() * 6)
    print(f'{filname} 下载完成')

def upload(filname):
    """上传文件"""
    print(f'开始上传{filname}')
    time.sleep(random.random() * 8)
    print(f'{filname} 上传成功')
    
download('mysql从删库到跑路.avi')
upload('python从入门到住院.pdf')


print('--------------------------------------------------')


# 知道到底下载和上传用来多少时间
start = time.time()
download('mysql从删库到跑路.avi')
end = time.time()
print(f'花费时间:{end - start:.2f}s')

start = time.time()
upload('python从入门到住院.pdf')
end = time.time()
print(f'花费时间:{end - start:.2f}s')


print('--------------------------------------------------')


# 通过装饰器将原来的上传和下载和计时功能代码封装在一个函数中
# 装饰器整体结构
def record_time(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper


import time

def record_time(func):
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间: {end - start : 2f} 秒')
        return result
    
    return wrapper

download = record_time(download)
upload = record_time(upload)
download('mysql从删库到跑路.avi')
upload('python从入门到住院.pdf')


print('--------------------------------------------------')


# 语法糖
import time
import random

def record_time(func):
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间: {end - start :.2f} 秒')
        return result
    
    return wrapper

@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename} 下载完成')
    
@record_time
def download(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename} 上传完成')
    
download('xxx')
upload('yyy')


print('--------------------------------------------------')


# 递归调用
# python中允许函数嵌套定义
# 也允许函数之间相互调用
# 而且一个函数还可以直接或佳节的调用自身
# 函数自己调用自己称为递归调用
def fac(num):
    if num in (0, 1):
        return 1
    return num * fac(num - 1)

print(fac(5))

"""
    递归函数入栈
    5 * fac(4)
    5 * (4 * fac(3))
    5 * (4 * (3 * fac(2)))
    5 * (4 * (3 * (2 * fac(1))))
    停止递归函数出栈
    5 * (4 * (3 * (2 *1)))
    5 * (4 * (3 * 2))
    5 * (4 * 6)
    5 * 24
    120
"""


print('--------------------------------------------------')


#生成斐波那契数列

def fib1(n):
    if n in (1, 2):
        return 1
    return fib1(n - 1) + fib1(n - 2)
for i in range(1, 20):
    print(fib1(i))
    
    
print('--------------------------------------------------')


def fib2(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a 

for i in range(1,20):
    print(fib2(i))
    
    
    
print('--------------------------------------------------')


# 使用functools 的 lru_cache函数优化递归代码
from functools import lru_cache

@lru_cache
def fib1(n):
    if n in (1, 2):
        return 1
    return fib1( n - 1) + fib1(n - 2)

for i in range(1, 51):
    print(i, fib1(i))
    
    
 



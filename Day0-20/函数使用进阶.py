# 函数使用进阶
# python 中的函数是一等函数
# 函数可以赋值给函数 函数可以作为函数的参数 函数可以作为函数的返回值
# 把一个函数作为其他函数的参数或返回值的用法
# 叫高阶函数

# 低阶函数
def calc(*args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = 0
    for item in items:
        if type(items) in (int, float):
            result += item
    return result

# 改写高阶函数
def calc(init_value, op_func, *args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result

# init_value 代表运算的初始值
# op_func 代表二元运算函数

def add(x, y):
    return x + y

def mul(x, y):
    return x * y

print(calc(0, add, 1, 2, 3, 4, 5))
print(calc(1, mul, 1, 2, 3, 4, 5))



print('--------------------------------------------------')


# 如没有提前定义好add 和 mul 函数
# 可以调用python标准库中的operator模块中的 add 和 mul 函数
import operator
print(calc(0, operator.add, 1, 2, 3, 4, 5))
print(calc(1, operator.mul, 1, 2, 3, 4, 5))


print('--------------------------------------------------')


"""
    python中内置函数中有不少高阶函数
    filter 实现对序列元素的过滤
    map 可以实现对序列中元素的映射
    
"""
# 去掉一个整数列表中的奇数 对所有偶数求平方得到新的列表

def is_even(num):
    return num % 2 == 0

def square(num):
    return num ** 2

old_num = [35, 12, 8, 99, 60, 52]
new_nums = list(map(square, filter(is_even, old_num)))
print(new_nums)


print('--------------------------------------------------')



# sorted函数 实现对容器型数据类型的元素排序
old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
new_strings = sorted(old_strings)
print(new_strings)


print('--------------------------------------------------')



old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
new_strings = sorted(old_strings, key = len)
print(new_strings)


print('--------------------------------------------------')


# lambda 函数
old_num = [35, 12, 8, 99, 60, 52]
new_nums = list(map(lambda x : x ** 2, filter(lambda x : x % 2 == 0, old_num)))
print(new_nums)


print('--------------------------------------------------')


import functools
import operator

fac = lambda n : functools.reduce(operator.mul, range(2, n + 1), 1)
is_prime = lambda x : all(map(lambda f : x % f, range(2, int(x ** 0.5) + 1)))

print(fac(6))
print(is_prime(37))


print('--------------------------------------------------')



# 偏函数
# 是指固定函数额某些参数 生成一个新的函数 这样就无需再每次调用函数时都传递相同的函数
# 使用 functools 的 partial函数来构造偏函数
import functools

int2 = functools.partial(int, base = 2)
int8 = functools.partial(int, base = 8)
int16 = functools.partial(int, base = 16)

print(int('1001'))
print(int2('1001'))
print(int8('1001'))
print(int16('1001'))

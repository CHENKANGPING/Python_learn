
# # 输入m和n的值 计算组合数c(m,n)的值
# m = int(input('m = '))
# n = int(input('n = '))

# # 计算m的阶乘
# fm = 1
# for num in range(1, m + 1):
#     fm *= num

# # 计算n的阶乘
# fn = 1
# for num in range(1, n + 1):
#     fn *= num

# # 计算 m - n 的阶乘
# fk =1
# for num in range(1,m - n + 1):
#     fk *= num
    
# print(fm//fn//fk)


# print('--------------------------------------------------')


# """
#     定义函数
#     python中可以使用def关键字来定义函数
#     在函数名后面的圆括号中可以设置函数的参数
#     函数执行完后
#     会通过return关键字来返回函数的执行结果
#     如: def function(arg1, arg2)
#             return 'something'
# """
# # 重构上面的代码
# # 通过关键字def定义求阶乘的函数
# # 自变量(参数) num是一个非负整数
# # 因变量(返回值) 时num的阶乘
# def fac(num):
#     result = 1
#     for n in range(2, num + 1 ):
#         result *= n
#     return result

# m = int(input('m = '))
# n = int(input('n = '))

# print(fac(m) // fac(n) // fac(m - n))

# """
#     使用函数可以帮我们将功能上相对独立且会被重复使用的代码分装起来
#     通过调用函数实现对既有代码的复用
# """


# print('--------------------------------------------------')



# # 从math导入factorial函数使用
# from math import factorial

# m = int(input('m = '))
# n = int(input('n = '))
# print(factorial(m) // factorial(n) // factorial(m - n))


print('--------------------------------------------------')


# 函数的参数
# 位置参数和关键字参数
def make_jubdgement(a, b, c):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and a + c > b and c + b > a
# 上面的三个参数叫做位置参数 在调用函数时通常按照从左到右的顺序依次传入
# 且数量必须相同
print(make_jubdgement(1, 2, 3))
print(make_jubdgement(4, 5, 6))

# 如不想按顺序传入参数，可以使用关键字参数
# 通过参数名 = 参数值的形式为函数传参
print(make_jubdgement(b = 2, c = 3, a = 1))
print(make_jubdgement(c = 6, b = 4, a = 5))

# 在定义函数时 可以在参数列表中用 / 设置强制位置参数
# 用 * 设置命名关键字参数

# /前面的参数是强制位置参数
def make_judgement(a, b, c, /):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and a + c > b and c + b > a

# * 后面的参数是命名关键字参数
def make_judgement(*, a, b, c):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and a + c > b and c + b > a


print('--------------------------------------------------')




# 参数的默认值
def add (a = 0, b = 0, c = 0):
    """三个数求和"""
    return a + b + c
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3,))


print('--------------------------------------------------')




# 可变参数
"""
    python中
    可以通过星号表达式语法让函数支持可变参数
    在函数调用时
    可以向函数传入0个或任意多个参数
"""
# 使用可变位置参数实现对任意多个数求和的add函数
def add(*args):
    total = 0
    for val in args:
        if type(val) in (int, float):
            total += val
    return total

print(add())
print(add(1))
print(add(1, 2, 3))
print(add(1, 2, 'hello', 3.45, 6))


print('--------------------------------------------------')




# 希望通过参数名 = 参数值的形式传入若干个参数
# 可以给函数添加关键字可变参数 
# 把传入的关键数参数组装到一个字典中
def foo(*args, **kwargs):
    print(args)
    print(kwargs)
    
foo(3, 2, 1, True, name = 'HiiAen', age = 13, gpa = 5)


print('--------------------------------------------------')


# 用模块管理函数
def foo():
    print('hello, world!')
    
def foo():
    print('goodbye, world!')
    
foo()




    
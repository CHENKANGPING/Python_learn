# 随机验证码
# 设计一个生成随机验证码的函数 验证码由数字和英文大小写字母组成
# 长度可以通过参数设置
import random
import string
ALL_CHARS = string.digits + string.ascii_letters
# digeits 代表0 - 9的数字构成的字符串
# ascii_letters 代表 abcd - YXZ 大小写构成的字符串

def generate_code(*, code_len = 4):
    """生成指定长度的验证码"""
    return ''.join(random.choices(ALL_CHARS, k= code_len))
# choices函数可以做到由放回抽样


for _ in range(5):
    print(generate_code())
    
    
print('--------------------------------------------------')



for _ in range(5):
    print(generate_code(code_len=7))


print('--------------------------------------------------')


# 判断素数
# 设计一个判断给定的大于1的正整数是不是素数的函数
# 质数只能被1和自身整除的正整数
def is_prime(num: int) -> bool:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


print('--------------------------------------------------')


# 最大公约数和最小公倍数
def lcm(x : int, y : int) -> int:
    """求最小公倍数"""
    return x * y // gcd(x, y)

def gcd(x : int, y: int) -> int:
    """求最大公约数"""
    while y % x != 0:
        x, y = y % x, x 
    return x    


print('--------------------------------------------------')


# 数据统计
def ptp(data):
    """极差"""
    return max(data) - min(data)

def mean(data):
    """算数平均"""
    return sum(data) / len(data)

def median(data):
    """中位数"""
    temp, size = sorted(data), len(data)
    if size % 2 != 0:
        return temp[size // 2]
    else:
        return mean(temp[size // 2 - 1 : size // 2 + 1])

def var(data, ddof = 1):
    """方差"""
    x_bar = mean(data)
    temp = [(num - x_bar) ** 2 for num in data]
    return sum(temp) / (len(temp) - ddof)

def std(data, ddof = 1):
    """标准差"""
    return var(data, ddof) ** 0.5

def cv(data, ddof = 1):
    """变异系数"""
    return std(data, ddof) / mean(data)

def desceibe(data):
    print(f'均值：{mean(data)}')
    print(f'中位数：{median(data)}')
    print(f'极差：{ptp(data)}')
    print(f'方差：{var(data)}')
    print(f'标准差：{std(data)}')
    print(f'变异系数：{cv(data)}')
    

print('--------------------------------------------------')


# 双色球随机选号
"""
双色球随机选号程序

Author: 骆昊
Version: 1.3
"""
import random

RED_BALLS = [i for i in range(1, 34)]
BLUE_BALLS = [i for i in range(1, 17)]


def choose():
    """
    生成一组随机号码
    :return: 保存随机号码的列表
    """
    selected_balls = random.sample(RED_BALLS, 6)
    selected_balls.sort()
    selected_balls.append(random.choice(BLUE_BALLS))
    return selected_balls


def display(balls):
    """
    格式输出一组号码
    :param balls: 保存随机号码的列表
    """
    for ball in balls[:-1]:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    print(f'\033[034m{balls[-1]:0>2d}\033[0m')


n = int(input('生成几注号码: '))
for _ in range(n):
    display(choose())




    
    









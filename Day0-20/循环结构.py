# 循环结构
# for - in 循环
# 每隔一秒输出一次'hello, word'

# import time
# for i in range(3600):
#     print(' hello, word ')
#     time.sleep(1)
    
"""
    range函数说明 
    range(101) 用来产生0 - 100 范围的整数 取不到101
    range(1, 101) 用来产生1 - 100 范围的整数 [1, 100)
    range(1, 101, 2) 用来产生1 - 100 的奇数 其中2是步长(跨步) 即每次递增的值, 101取不到
    range(100, 0, -2) 用来产生100 - 1 的偶数 其中 -2 是步长 及每次递减的值， 0取不到

"""

print('--------------------------------------------------')

# 用for - in 循环实现1到100的整数求和
total = 0
for _ in range(1, 101):
    total += _
print(total)

# total += _ 相当于 total = total + _  实现累加的效果


print('--------------------------------------------------')


# 用for - in 循环实现1到100的偶数求和

total = 0 
for _ in range(1, 101):
    if _ % 2 == 0:
        total += _
print(total)


print('--------------------------------------------------')


# 用range(2, 101, 2)求偶数总和
total = 0
for _ in range(2, 101, 2):
    total += _ 
print(total)


print('--------------------------------------------------')


# while循环
"""
    如果要构造循环结构但是又不能确定循环重复的次数,我们推荐使用while循环
    while循环通过布尔值或能产生布尔值的表达式来控制循环
    当布尔值或表达式的值为True时,循环体(while语句下方保持相同缩进的代码块)中的语句就会被重复执行
    当表达式的值为False时 结束循环
"""
# while循环实现1到100整数求和代码
total = 0
_ = 1 
while _ <= 100:
    total += _
    _  += 1
print(total)

print('--------------------------------------------------')


# break 和 continue
# 从1到100的偶数求和
total = 0 
_ = 2 
while True:
    total += _
    _ += 2
    if _ > 100:
        break
print(total)


print('--------------------------------------------------')


total = 0
for _ in range(1, 101):
    if _ % 2 != 0:
        continue
    total += _
print(total)


print('--------------------------------------------------')


# 嵌套的循环结构
# 循环输出九九乘法表
for _ in range(1, 10):
    for j in range(1, _ + 1):
        print(f'{_}x{j}={_ * j}', end='\t')
    print()


print('--------------------------------------------------')

# 循环判断应用
# 1.判断素数
# 要求：输入一个大于1的正整数，判断它是不是素数
num = int(input('请输入一个正整数：'))
end = int(num ** 0.5)
is_prime = True
for _ in range(2, end + 1):
    if num % _ == 0:
        is_prime = False
        break
if is_prime:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')

"""
- 计算输入数的平方根作为最大可能因数
- 检查2到该平方根之间是否有能整除的数
- 如果没有则是素数，否则不是
"""


print('--------------------------------------------------')


# 2.最大公约数
x = int(input('x = '))
y = int(input('y = '))
while y % x != 0:
    x, y = y % x, x
    # 关键步骤
print(f'最大公约数：{x}')

"""
算法原理：

1. 欧几里得算法基于原理:gcd(a,b) = gcd(b, a mod b)
2. 持续用较小数除较大数的余数,直到余数为0
3. 最后的非零余数就是最大公约数
示例执行过程(假设输入x=30, y=18):

1. 第一次循环:30 % 18 = 12 → x=12, y=18
2. 第二次循环:18 % 12 = 6 → x=6, y=12
3. 第三次循环:12 % 6 = 0 → 循环结束
4. 输出:6
"""


print('--------------------------------------------------')


# 猜数字游戏
import random
answer = random.randrange(1, 101)
counter = 0
while True:
    counter += 1
    num = int(input('请输入： '))
    if num < answer:
        print('大一点')
    elif num > answer:
        print('小一点')
    else:
        print('猜对了！')
        break
print(f'你一共猜了{counter}次')
    





        
    



# 将一颗骰子投掷6000次，统计每种点数出现的次数
import random
f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0
f6 = 0
for _ in range(6000):
    point = random.randrange(1, 7)
    if point == 1:
        f1 += 1
    elif point == 2:
        f2 += 2
    elif point == 3:
        f3 += 3
    elif point == 4:
        f4 += 4
    elif point == 5:
        f5 += 5
    else:
        f6 += 6
print(f' 一共出现了{f1}次一点')
print(f' 一共出现了{f2}次二点')
print(f' 一共出现了{f3}次三点')
print(f' 一共出现了{f4}次四点')
print(f' 一共出现了{f5}次五点')
print(f' 一共出现了{f6}次六点')
# 上述代码就两个字：丑陋，恶心。


print('--------------------------------------------------')


# 创建列表
"""
    在python中 列表是由一系列元素按特定顺序所构成的数据序列 
    它可以用来保存多个数据 用[]来定义列表 多个元素用逗号隔开
"""
items1 = [35, 12, 99, 68, 55, 35, 86]
items2 = ['python', 'java', 'go', 'cpp']
items3 = [100, 23.3, 'python', True]
print(items1)
print(items2)
print(items3)
# 列表中可以有重复元素，也可以有不同类型的元素，但不建议将不同类型的元素放在同一个列表中


print('--------------------------------------------------')


# list函数 创造列表对象的构造器
items4 = list(range(1, 10))
# range(1, 10)会产生1到9的整数序列，给到list容器中 会创建出1到9的整数构成的列表
items5 = list('hello')
print(items4)
print(items5)


print('--------------------------------------------------')


# 列表的运算
items6 = [43, 24, 234, 453, 353]
items7 = [45, 24, 75]
items8 = ['python', 'java', 'js']
print(items6 + items7)
print(items7 + items8)
items6 += items7
print(items6)
print(items6 * 2)
print(items8 * 3)
print(1 in items6)
print(43 in items6)
print('cpp' not in items8)
print('python' not in items8)


print('--------------------------------------------------')


# []运算符
"""
    当我们想要对列表中的某个元素进行操作时 可以运用[]运算符
    又被称为索引运算 []的元素位置可以是0 到 N-1 的整数
    也可以是 -1 到 -N 的整数 分别为正向索引和反向索引
    其中 N 代表列表元素的个数 对于正向索引 [0] 可以访问
    列表中的第一个元素 [N - 1] 可以访问最后一个元素
    对于反向索引 [-1] 可以访问列表中的最后一个元素
    [-N] 可以访问第一个元素 
"""
items9 = ['apple', 'peach', 'watermelon', 'waxberry', 'pitaya']
print(items9[0])
# 输出为apple [0]为第一个元素
print(items9[2])
# 输出为watermelon [2]为第三个元素
print(items9[4])
# 输出为pitaya [4]为第五个元素
items9[2] = 'durian'
# 将第三个元素换为durian
print(items9)
print(items9[-5])
# 输出为apple 这里是反向索引 为反向数第5个元素为apple
print(items9[-4])
# 输出为peach 反向数第4个元素为peach
print(items9[-1])
# 输出为pitaya 反向数第1个元素为pitaya
items9[-4] = 'strawberry'
print(items9)


print('--------------------------------------------------')


# 切片运算
"""
    如果希望一次性访问列表中多个元素 可以使用切片运算
    切片运算为[start : end : stride]
    start 代表访问列表元素的起始位置
    end 代表访问列表元素的终止位置
    终止位置的元素无法访问
    stride代表了跨度(位置的增量)
    比如我要访问的第一个元素在start位置
    第二个元素就在start + stride 位置
    注:start + stride 要小于 end
"""
# items9 = ['apple', 'strawberry', 'durian', 'waxberry', 'pitaya']
print(items9[1:3:1])
# start元素为strawberry stride为1 end元素waxberry 不取
print(items9[0:3:1])
# start元素为apple stride为1 end元素为waxberrt 不取
print(items9[0:5:2])
# start元素为apple stride为2 end元素没有 不取
print(items9[-4:-2:1])
# start元素为strawberry stride为1 end元素为waxberry 不取
print(items9[-2:-6:-1])
# start元素为waxberry stride为-1 end元素为没有 不取


print('--------------------------------------------------')

# 切片修该列表元素
items9[1:3] = ['x', 'o']
print(items9)


print('--------------------------------------------------')


# 两列表可以进行关系运算
nums1 = [1, 2, 3, 4]
nums2 = list(range(1, 5))
nums3 = [3, 2, 1]
print(nums1 == nums2)
print(nums1 != nums2)
print(nums1 <= nums3)
print(nums2 >= nums3)


print('--------------------------------------------------')


# 元素遍历
# 方法一 在循环中通过索引运算 遍历列表元素
language = ['python', 'java', 'cpp', 'js']
for index in range(len(language)):
    print(language[index])

# len函数可以获取列表元素的个数N，而range(N) 则构成了从0到N - 1的范围 刚好作为列表元素索引
    
    
print('--------------------------------------------------')


# 方法二 直接对列表做循环，循环变量就是列表元素的代表
languages = ['R', 'c#', 'C', 'SQL']
for language in languages:
    print(language)


print('--------------------------------------------------')


# 重构扔骰子游戏
import random
counters = [0] * 6
for _ in range(6000):
    face = random.randrange(1, 7)
    counters[face - 1] += 1
for face in range(1, 7):
    print(f'{face}点出现了{counters[face - 1]}次')

















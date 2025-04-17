# 添加和删除元素
"""
    列表是一种可变的容器 可变容器指的是我们可以向容器中添加元素
    可以向容器中移除元素 也可以修该现有容器中的元素
    append方法向列表中追加元素
    insert方法向列表中插入元素
    追加指的是将元素添加到列表末尾
    插入指的是在指定位置添加新元素
"""
languages = ['python', 'java', 'cpp']
languages.append('js')
print(languages)
languages.insert(1, 'SQL')
print(languages)


print('---------------------------------------------------------------')


"""
    remove方法从列表中删除指定元素
    pop方法默认删除列表中最后一个元素 也可以给一个位置 删除指定位置的元素
    clear方法清空列表中的元素
"""
lan = ['python', 'java', 'cpp', 'js', 'R']
if 'java' in lan:
    lan.remove('java')
if 'C#'  in lan:
    lan.remove('C#')
print(lan)

lan.pop()
temp = lan.pop(1)
print(temp)

lan.append(temp)
print(lan)

lan.clear()
print(lan)

lan2 = ['python', 'python', 'python', 'cpp']
lan2.remove('python')
print(lan2)


print('---------------------------------------------------------------')


# 元素位置与频次
items = ['python', 'java', 'java', 'cpp', 'kotlin', 'python']
print(items.index('python'))
print(items.index('python', 1))
print(items.count('python'))
print(items.count('kotlin'))
print(items.count('swfit'))
# print(items.index('java',3))
# 这里运行会报错 ValueError:'java' is not in list


print('---------------------------------------------------------------')


# 元素排序与反转
# sort可实现列表元素的排序
# reverse可以实现元素的反转

items1 = ['python', 'java', 'cpp', 'kotlin', 'swift']
items1.sort()
print(items1)
items1.reverse()
print(items1)


print('---------------------------------------------------------------')


# 列表生成式
"""
    在python中 列表还可以通过一种特殊的字面量语法来创建 
    这种语法叫做生成式
"""
# 场景一 创建一个取值范围在1到99且能被3或5整除的数字列表
c = []
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        c.append(i)
print(c)


print('---------------------------------------------------------------')


# 另一种装 X 写法
b = [i for i in range(1, 100) if i % 3 == 0 or i % 5 ==0]
print(b)


print('---------------------------------------------------------------')


# 场景二 有一个整数列表nums1 创建一个新的列表nums2, nums2 中的元素是nums1中对应元素的平方
nums1 = [35, 34, 56, 12]
nums2 = []
for num in nums1:
    nums2.append(num ** 2)
print(nums2)


print('---------------------------------------------------------------')


# 场景三 有一个整数列表nums3 创建一个新的列表nums4 将nums3中大于50的元素放到nums4中
nums3 = [51, 42, 76, 24, 87]
nums4 = []
for num in nums3:
    if num > 50:
        nums4.append(num)
print(nums4) 

# 另一种写法
nums5 = [78, 98, 23, 12]
nums6 = [num for num in nums5 if num > 50]
print(nums6)


print('---------------------------------------------------------------')


# 嵌套列表
"""
    如果列表中的元素也是列表 那么我们可以称之为嵌套的列表
    嵌套的列表可以用来表示表格或数学上的矩阵
"""
# 保存5个学生三门课程的成绩
score = [[33, 53, 32], [24, 56, 78], [12, 32, 56], [23, 35, 56], [76, 45, 34]]
print(score[0])
print(score[0][1])


print('---------------------------------------------------------------')


# 通过产生随机数的方式来生成 使用列表生成式
import random
scores = [[random.randrange(60, 101) for _ in range(3)] for _ in range(5)]
print(scores)


print('---------------------------------------------------------------')


# 列表的应用
"""
    通过一个双色球随机选号的例子
    每注号码由6个红色球和1个蓝色球组成
    红色球号码从1到33中选择
    蓝色球号码从1到16中选择
    每注需要6个红色球号码和1个蓝色球号码
    "真爱生命 远离赌博"
    "虚构一个不劳而获的人 去忽悠一群想不劳而获的人 最终养活一批真不劳而获的人
"""
from rich.console import Console
from rich.table import Table
import random

console = Console()

n = int(input('生成几注号码: '))
red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1,17)]

table = Table(show_header=True)
for col_name in ('序号', '红球', '蓝球'):
    table.add_column(col_name, justify='center')
for i in range(n):
    selected_balls = random.sample(red_balls, 6)
    selected_balls.sort()
    blue_ball = random.choice(blue_balls)
    
    table.add_row(
        str(i + 1),
        f'[red]{" ".join([f"{ball:0>2d}" for ball in selected_balls])}[/red]',
        f'[blue]{blue_ball:0>2d}[/blue]'
    )
console.print(table)






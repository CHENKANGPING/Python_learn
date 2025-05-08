# 生成式（推导式）的用法
price = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM' : 149.24,
    'ORCL': 48.44,
    'ACN' : 166.89,
    'FB' : 208.09,
    'SYCM' : 21.29
}
# 用股票价格大于100元的股票构造一个新的字典
price2 = {key : value for key, value in price.items() if value > 100}
print(price2)

print('--------------------------------------------------')

# 嵌套列表的坑
# names = ['关羽', '张飞', '赵云','马超','黄忠']
# courses = ['语文','数学','英语']
# scores = [[None] * len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col,course in enumerate(courses):
#         scores[row][col] = float(input(f'请输入{name}的{course}成绩：'))
#         print(scores)
        
        
print('--------------------------------------------------')


# heapq模块（堆排序）
"""
    从列表中找出最大的或最小的N各元素
    堆结构（大根堆/小根堆）
"""
import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(2,list1))
print(heapq.nsmallest(3,list1))
print(heapq.nlargest(2,list2, key = lambda x : x['price']))
print(heapq.nlargest(2,list2, key = lambda x : x['shares']))


print('--------------------------------------------------')


# itertools模块
"""
    迭代工具模块
"""
import itertools

# 产生ABCD的全排列
itertools.permutations('ABCD')

# 产生ABCDE的五选三组合
itertools.combinations('ABCDE', 3)

# 产生ABCD和123的笛卡尔积
itertools.product('ABCD','123')

# 产生ABC的无限循环序列
itertools.cycle(('A','B','C'))


print('--------------------------------------------------')


# collections模块
"""
找出序列中出现次数最多的元素
"""
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(3))



    

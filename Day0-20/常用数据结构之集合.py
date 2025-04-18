"""
    python程序中的集合跟数学上的集合没有什么本质区别
    集合不支持索引运算
    集合中不能有重复元素
    集合的成员运算在性能上优于列表的成员运算
"""
"""
    创建集合
    用{}字面量语法
    {}中至少有一个元素
    内置函数set来创建集合
    还可以用生成式语法来创建集合
"""
set1 = {1, 2, 3, 3, 3, 2}
print(set1)

set2 = {'banana', 'pitaya', 'apple', 'banana', 'grape'}
print(set2)

set3 = set('hello')
print(set3)

set4 = set([1, 2, 2, 3, 3, 3, 2, 1])
print(set4)

set5 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
print(set5)

"""
    集合中的元素必须是hashable类型
    所谓hashable类型指的是能够计算出哈希码的数据类型
    通常不可变类型都是hashable类型
    如整数(int) 浮点小数(float) 布尔值(bool) 字符串(str) 元组(tuple)等
    可变类型都不是hashable类型 因为可变类型无法计算出确定的哈希码 所以它们不能放到集合中
"""


print('--------------------------------------------------')


# 元素的遍历
set1 = {'python', 'cpp', 'java', 'js','C#'}
for elem in set1:
    print(elem)
    
    
print('--------------------------------------------------')


# 成员运算
set1 = {11, 12, 13, 14, 15}
print(10 in set1)
print(15 in set1)
set2 = {'python', 'java', 'C++', 'swift'}
print('ruby' in set2)
print('java' in set2)


print('--------------------------------------------------')


# 二元运算
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

# 交集
print(set1 & set2)
print(set1.intersection(set2))

# 并集
print(set1 | set2)
print(set1.union(set2))

# 差集
print(set1 - set2)
print(set1.difference(set2))

# 对称集
print(set1 ^ set2)
print(set1.symmetric_difference(set2))


print('--------------------------------------------------')


# 相对简短的写法
set1 = {1, 3, 5, 7}
set2 = {2, 4, 6}

set1 |= set2
# set1.update(set2)
print(set1)

set3 = {3, 6, 9}
set1 &= set3
# set1.intersection_update(set3)
print(set3)

set2 -= set1
# set2.defference_update(set1)
print(set2)


print('--------------------------------------------------')


# 比较计算
set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}
set3 = {5, 4, 3, 2, 1}

print(set1 < set2)   # True
print(set1 <= set2)  # True
print(set2 < set3)   # False
print(set2 <= set3)  # True
print(set2 > set1)   # True
print(set2 == set3)  # True

print(set1.issubset(set2))    # True
print(set2.issuperset(set1))  # True


print('--------------------------------------------------')


# 集合的方法
# 通过集合的方法向集合添加元素或从集合中删除元素
set1 = {1, 10, 100}

# 添加元素
set1.add(1000)
set1.add(10000)
print(set1)  # {1, 100, 1000, 10, 10000}

# 删除元素
set1.discard(10)
if 100 in set1:
    set1.remove(100)
print(set1)  # {1, 1000, 10000}

# 清空元素
set1.clear()
print(set1)  # set()


print('--------------------------------------------------')


# isdisjoint方法 用来判断两个集合有没有相同的元素
# 没有相同的元素 返回True
# 否则返回False
set1 = {'Java', 'Python', 'C++', 'Kotlin'}
set2 = {'Kotlin', 'Swift', 'Java', 'Dart'}
set3 = {'HTML', 'CSS', 'JavaScript'}
print(set1.isdisjoint(set2))  # False
print(set1.isdisjoint(set3))  # True


print('--------------------------------------------------')


"""
    Python 中还有一种不可变类型的集合
    名字叫frozenset set跟frozenset的区别就如同list跟tuple的区别
    frozenset由于是不可变类型 能够计算出哈希码 因此它可以作为set中的元素 
    除了不能添加和删除元素 frozenset在其他方面跟set是一样的 下面的代码简单的展示了frozenset的用法
"""
fset1 = frozenset({1, 3, 5, 7})
fset2 = frozenset(range(1, 6))
print(fset1)          # frozenset({1, 3, 5, 7})
print(fset2)          # frozenset({1, 2, 3, 4, 5})
print(fset1 & fset2)  # frozenset({1, 3, 5})
print(fset1 | fset2)  # frozenset({1, 2, 3, 4, 5, 7})
print(fset1 - fset2)  # frozenset({7})
print(fset1 < fset2)  # False







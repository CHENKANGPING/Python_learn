"""
    创建和使用字典
    用{}字面量语法
    但是字典{}中的元素
    是以键值对的形式存在的
    每个元素由:分隔的两个值构成
    :前面是健
    :后面的是值
"""
xinhua = {
    '麓': '山脚下',
    '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
    '蕗': '甘草的别名',
    '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
}
print(xinhua)
person = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': '成都市武侯区科华北路62号1栋101', 
    'tel': '13122334455',
    'emergence contact': '13800998877'
}
print(person)


print('--------------------------------------------------')


# 也可以使用内置函数dict或是字典的生成式语法来创建字典
# dict函数中的每一组参数就是字典中的一组键值对
person = dict(name = 'jack', age = 55, height = 168, weight = 60, addr = 'dalian')
print(person)

# 可以通过python内置函数zip压缩两个序列并创建字典
items1 = dict(zip('ABCDE', '12345'))
print(items1)
items2 = dict(zip('ABCD', range(1, 100)))
print(items2)

# 用字典生成式语法创建字典
items3 = {x: x ** 3 for x in range(1, 6)}
print(items3) 


print('--------------------------------------------------')


"""
    字典的运算
    对于字典来说
    成员运算和索引运算时很重要的
    字典需要用健去索引对应的值
    字典中的健必须时不可变类型
"""
person = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': ['成都市武侯区科华北路62号1栋101', '北京市西城区百万庄大街1号'],
    'car': {
        'brand': 'BMW X7',
        'maxSpeed': '250',
        'length': 5170,
        'width': 2000,
        'height': 1835,
        'displacement': 3.0
    }
}
print(person)


print('--------------------------------------------------')


# 成员运算和索引运算
# 成员运算
person = {'name' : 'jack', 'age' : 55, 'height' : 168, 'weight' : 60, 'addr' : 'dalian'}
print('name' in person)
print('tel' in person)

# 索引运算
print(person['name'])
print(person['addr'])
person['age'] = 25
person['height'] = 178
person['tel'] = '12314124324'
person['signature'] = 'sfieasdjflefasfea'
print(person)

# 循环遍历
for key in person:
    print(f'{key}:\t{person[key]}')
    
    
print('--------------------------------------------------')


# 字典的方法
# get方法
person = {'name' : 'jack', 'age' : 55, 'height' : 168, 'weight' : 60, 'addr' : 'dalian'}
print(person.get('name'))
print(person.get('sex'))
print(person.get('sex', True))


print('--------------------------------------------------')


# keys方法
person1  = {'name' : 'Tom', 'age' : '34', 'height' : '123'}
print(person1.keys())
print(person1.values())
print(person1.items())
for key, value in person1.items():
    print(f'{key}:\t{value}')


print('--------------------------------------------------')


# update方法
# 实现两个字典合并
# 当执行x.update(y)操作时
# x和y相同的值会被y中的值更新
x = {'name' : 'jks', 'age' : 34, 'height' : 213}
y = {'age' : 35, 'addr' : 'sfewdsfw'}
x.update(y)
print(x)


print('--------------------------------------------------')


"""
    通过pop和popitem方法从字典中删除元素
    pop会返回键对应的值
    popitem会返回键和值组成的二元组
"""
person = {'name' : 'jack', 'age' : 21, 'height' : 134, 'addr' : 'ersffsfsd'}
print(person.pop('age'))
print(person)
print(person.popitem())
print(person)
person.clear()
print(person)


print('--------------------------------------------------')


# del方法
person = {'name' : 'jack', 'age' : 21, 'height' : 134, 'addr' : 'ersffsfsd'}
del person['age']
del person['addr']
print(person)


print('--------------------------------------------------')


# 字典的引用
# 1.输入一段话 统计每个英文字母出现的次数，按出现次数从高到底排序
sentence = input('请输入一段话： ')
conter = {}
for ch in sentence:
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        conter[ch] = conter.get(ch, 0) + 1
sorted_keys = sorted(conter, key=conter.get, reverse=True)
for key in sorted_keys:
    print(f'{key} 出现了 {conter[key]}次')
    
    
print('--------------------------------------------------')


# 2.在一个字典中保存了股票的代码和价格
# 找出股价大于100元的股票并创建一个新的字典
stock ={
    'AAPL' : 191.88,
    'GOOG' : 1123,
    'IBM' : 124,
    'ORCL' : 43,
    'ACN' : 645,
    'FB' : 204,
    'SYCM' : 12
}
stock2 = {key: value for key, value in stock.items() if value > 100}
print(stock2)



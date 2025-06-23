# redis数据类型

## 1.list类型：

1.1添加子成员

```bash
# 在左侧(前)添加一条或多条数据
lpush key value1 value2 ...

# 在右侧(后)添加一条或多条数据
rpush key value1 value2 ...

# 在指定元素的左边(前)/右边(后)插入一个或多个数据
linsert key before 指定元素 value1 value2 ...
linsert key after 指定元素 value1 value2 ...

```



1.2基于索引获取列表成员

根据指定的索引下标获取成员的值，负数下标从右边-1开始，逐个递减

```bash
lindex key index
```

1.3获取列表的切片

```bash
lrange key start stop
```

1.4获取列表的长度

```bash
llen key
```

1.5按索引设置值

```bash
lset key index value
# 注意:
# redis的列表也有索引，从左往右，从0开始，逐一递增，第一个元素下标为0。
# 索引可以是负数，表示尾部开始计数，如'-1'表示最后一个元素。
```

1.6删除指定成员

```bash
lpop key # 第一个成员出列
rpop key # 最后一个成员出列

```

```bash
lrem key count value

# 注意：
# count表示删除的数量，value表示要删除的成员，该命令默认表示将列表从左侧前count个value的元素移除
# count == 0 表示删除列表所有值为value的成员
# count > 0 表示删除列表左侧开始的前count个value成员
# count < 0 表示删除列表右侧开始的前count个value成员
```










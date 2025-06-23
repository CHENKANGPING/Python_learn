# redis数据类型

## 1.zset类型：

有序集合，去重并且根据score权重值来进行排序的。score从小到大排列。

1.1添加成员

```bash
zadd key score1 member1 score2 member2 score3 member3 ...
```

设置榜单achievements,设置成绩和用户名作为achievements的成员

```bash
zadd achievements 61 xiaoming 62 xiaohong 83 xiaobai 78 xiaohei 87 xiaohui 99 xiaolan
```

1.2获取score在指定区间的所有成员

```bash
zrangebyscore key min max # 按score进行从低往高排序获取指定score区间

zrevrangebyscore key min max # 按score进行从高往低排序获取指定score区间

zrange key start stop # 按score进行从低往高排序获取指定索引区间

zrevrange key start stop # 按score进行从高往低排序获取指定索引区间

```

1.3 获取集合长度

```bash
zcard key
```

1.4获取指定成员的权重值

```bash
zscore key member
```

1.5获取指定成员在集合中的排名数

排名从0开始计算

```bash
zrank key member # score从小到大的排名
zrevrank key member # score从大到小排名
```

1.6获取score在指定区间的所有成员数量

```bash
zcount key min max
```

1.7给指定成员增加权重

```bash
zincrby key score member
```

1.8删除成员

```bash
zrem key member1 member2 member3...
```

1.9删除指定数量的成员

```bash
# 删除指定数量的成员，从最低score开始删除
zpopmin key [count]
# 删除指定数量的成员 从最高score开始删除
zpopmax key [count]
```


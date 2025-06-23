# redis数据类型

## 1.set类型：

无序集合，重点就是去重和无序。

1.1添加元素

```bash
sadd key member1 member2 ...
```

1.2获取集合的所有的成员

```bash
smembers key
```

1.3获取集合的长度

```bash
scard keys
```

1.4随机抽取一个或多个元素

抽取出来的成员被删除

```bash
spop key [count = 1]
# count为可选参数，不填则默认一个，被提取成员会从集合中被删除掉
```

1.5删除指定元素

```bash 
srem key value
```

1.6交集，差集和并集

推荐(协同过滤，基于用户，基于物品)

```bash
sinter key1 key2 key3... # 交集 比较多个集合中共存的成员

sdiff key1 key2 key3... # 差集 比较多个集合中不同的成员

sunion key1 key2 key3... # 并集 合并所有集合中的成员，并去重
```






# redis数据类型

## 1.string类型：

字符串类型，是redis中最为基础的数据存储类型，它在redis中是二进制安全的，也就是byte类型。单个数据的最大容量为512m

​	key：值

1.1set设置的数据没有额外操作时，是不会过期的。

```bash
set key value
```

注意：redis中的所有数据操作，如果设置的键不存在则为添加，如果设置的键已经存在则修改。

1.2设置一个键，当键不存在时才能设置成功， 用于一个变量只能被设置一次的情况。

```bash
setnx key value
```

一般用于给数据加锁（分布式锁）

1.3设置键值的过期时间

redis中可以对一切的数据进行设置有效期。以秒为单位

```bash
setex key seconds value
```

1.4设置多个键值

```bash
mset key1 value1 key2 value2...
```

```bash
mset a1 goland a2 java a3 c
```

批量查询

```bash
mget key1 key2 key3...
```

1.5字符串拼接值

常见于大文件上传

```bash
append key value
```

向键为a1中拼接haha

```bash
set title "我的"
append title "redis"
append title "学习之路"
```

1.6自增自减

web开发中的电商抢购，秒杀。游戏里的投票，攻击计数，系统中的计算当前在线人数。

```bash
set id 1
incr id # 相当于id+1
get id  # 2
incr id # 相当于id+1
get id  # 3

# 自减
decr count

# 自定义增减
incrby count 10
decr by count 10
```

1.7获取字符串的长度

```bash
set name xiaoming
strlen name
```

1.8比特流操作

```bash
SETBIT   # SETBIT key offset value 按从左到右的偏移量设置一个bit数据的值
GETBIT   # 获取一个bit数据的值
BITCOUNT # 统计字符串被设置为1的bit数
BITPOS   # 返回字符串里面第一个被设置为1或者0的bit位。
```

```bash
setbit mykey 7 1
# 00000001
getbit mykey 7
# 00000001
setbit mykey 4 1
# 00001001
setbit myket 15 1
# 0000100100000001
```

通过setbit命令将andy中的'a'变成'b'如何变

```bash
set name a
setbit name 6 1
setbit name 7 0
get name   # "b"
```

## 2.key操作

redis中所有的数据都是通过key来进行操作的。

2.1查找键

参数支持简单的正则表达式

```bash
keys pattern
```

查看所有键

```bash
keys *
```

2.2判断键是否存在

如果存在返回1,不存在返回0

```bash 
exists key1
```

判断键titel是否存在

```bash
exists titel
```

2.3查看键的的值的数据类型

```bash
type key
```

2.4删除键以及键对应的值

```bash
del key1 key2...
```

2.5查看键的有效期

```bash
ttl key
# -1 表示永不过期
# -2 表示当前书籍以及过期，查看一个不存在的数据的有效期就是-2
```

2.6设置key的有效期

给已有的数据重新设置有效期，redis中所有的数据都可以通过expire来设置它的有效期。有效期到了，数据就被删除。

```bash
expire key seconds
```

2.7清空所有key

```bash
flushall
```

2.8key重命名

```bash
rename oldkey newkey
```

把name重命名为username

```bash
set name ckp 
rename name username 
get username
```

select切换数据库

```bash
redis的配置中，默认有0~15之间的16个数据库，默认操作的就是0号数据库。
select <数据库ID>
```




















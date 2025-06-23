# redis数据类型

## 1.hash类型：

专门用于结构化的数据信息。对应的就是map/结构体

结构：

```bash
键key:{
	域field:值value，
	域field:值value，
	域field:值value，
}
```

1.1设置指定键的属性/域

设置指定键的单个属性

```bash
hset key field value
```

1.2获取指定键的域/属性的值

```bash
hget key field
```

获取指定键的多个域/属性的值

```bash
hmget key field1 field2 ...
```

获取指定键的所有值

```bash
hvals key
```

获取指定键的所有键

```bash
hkeys key
```



1.3获取hash的所有域值对

```bash
hgetall key
```

1.4删除指定键的域/属性

```bash
hdel key field1 field2 ...
```

1.5判断指定属性/域是否存在于当前键对应的hash中

```bash
hexists key field
```

1.6属性自增自减

```bash
hincrby key field number
```










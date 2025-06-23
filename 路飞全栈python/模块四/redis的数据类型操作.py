import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

# 字符串操作
r.set('bar', 'foo')
print(r.get('bar'))

# 字符串操作：不允许对已存在的键设置值
ret = r.setnx("name", "ckp")
print(ret)

# 设置键有效期
r.setex("good_1001", 10, "2")

# 自增自减
r.set("age", 20)
r.incrby("age", 2)
print(r.get("age"))

# hash操作 ： 设置hash
r.hset("info", "name", "ckp")
print(r.hget("info", "name"))
r.hmset("info", {"gender": "male", "age": 20})
print(r.hgetall("info"))

# list操作：设置list
r.rpush("scores", "100", "90", "80")
r.rpush("scores", "70")
r.lpush("scores", "100")
print(r.lrange("scores", 0, -1))
r.linsert("scores", "AFTER", "100", "95")
print(r.lrange("scores", 0, -1))
print(r.lpop("scores"))
print(r.rpop("scores"))
print(r.lindex("scores", 1))

# 集合操作
# key对应的集合汇总添加元素
r.sadd("name_set", "zhangsan", "lisi", "wangwu")
# 获取key对应的集合的所以成员
print(r.smembers("name_set"))
# 从key对应的集合中随机获取 number个元素
print(r.srandmember("name_set", 2))
r.srem("name_set", "lisi")
print(r.smembers("name_set"))

# 有序集合操作
# 在key对应的有序集合中添加元素
r.zadd("jifenbang", {"ckp": 78, "rain": 20, "zj": 90})
# 按照索引范围获取key对应的有序集合的元素
print(r.zrange("jifenbang", 0, -1))
print(r.zrange("jifenbang", 0, -1, withscores=True))
print(r.zrevrange("jifenbang", 0, -1, withscores=True))
print(r.zrangebyscore("jifenbang", 0, 100))
print(r.zrevrangebyscore("jifenbang", 0, 100, start=0, num=1))
# 删除key对应的有序集合中值的values的成员
print(r.zrem("jifenbang", "ckp"))
print(r.zrange("jifenbang", 0, -1))

# 键操作
r.delete("scores")
print(r.exists("scores"))
print(r.keys("*"))
r.expire("name", 10)

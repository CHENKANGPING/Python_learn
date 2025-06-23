import redis

# 方式1
# r = redis.Redis(host='127.0.0.1', port=6379)
# r.set('foo', 'bar')
# print(r.get('foo'))

# 方式2
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)
r.set('bar', 'foo')
print(r.get('foo'))
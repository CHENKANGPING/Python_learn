import  queue

# q = queue.Queue(0)
q = queue.Queue(3)

# FIF0：先入先出
# 插入元素： put
print(q.qsize())
q.put(100)
q.put(200)
q.put(300)
print(q.qsize())
print(q.get())
print(q.get())
print(q.get())

print(q.empty())























# 缓存的容器类型
class Cache(object):
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(item)

    def remove(self, item):
        self.data.remove(item)

    def show(self):
        print(self.data)

    def __len__(self):
        return len(self.data)


cache = Cache()
cache.add("ckp")
cache.add("zj")
cache.add("hyf")

cache.show()
cache.remove("ckp")
cache.show()

print(len(cache))


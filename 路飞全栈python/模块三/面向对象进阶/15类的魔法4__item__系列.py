# # 缓存的容器类型
# class Cache(object):
#     def __init__(self):
#         self.data = {}
#
#     def add(self, key, value):
#         self.data[key] = value
#
#     def remove(self, key):
#         self.data.pop(key)
#
#     def show(self):
#         print(self.data)
#
#     def __len__(self):
#         return len(self.data)


# 版本1
# cache = Cache()
# cache.add("name", "ckp")
# cache.add("age", 18)
# cache.show()
# cache.remove("age")
# cache.show()
# print(len(cache))

# 版本2
from loguru import logger


class Cache(object):

    def __init__(self):
        self.__data = {}

    def __setitem__(self, key, value):
        self.__data[key] = value
        logger.info(f"已经向self.__data添加了{key}和{value}")

    def __getitem__(self, key):
        # return self.__data.get(key)
        val = self.__data.get(key)
        if val:
            return val
        else:
            raise KeyError(key)

    def __delitem__(self, key):
        del self.__data[key]

    def __contains__(self, key):
        return key in self.__data


cache = Cache()
# cache["name"] = "HiiAen"
# print(cache["name"])
# del cache["name"]
# print(cache["name"])
print("name" in cache)

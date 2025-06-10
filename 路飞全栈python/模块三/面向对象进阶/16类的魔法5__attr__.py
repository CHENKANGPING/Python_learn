from loguru import logger


#
#
# class Cache(object):
#
#     def __init__(self):
#         self.__data = {}
#
#     def __setitem__(self, key, value):
#         self.__data[key] = value
#         logger.info(f"已经向self.__data添加了{key}和{value}")
#
#     def __getitem__(self, key):
#         # return self.__data.get(key)
#         val = self.__data.get(key)
#         if val:
#             return val
#         else:
#             raise KeyError(key)
#
#     def __delitem__(self, key):
#         del self.__data[key]
#
#     def __contains__(self, key):
#         return key in self.__data
#
#
# cache = Cache()
# # cache["name"] = "HiiAen"
# # print(cache["name"])
# # del cache["name"]
# # print(cache["name"])
# print("name" in cache)

class Cache(object):

    def __init__(self):
        # self.data = {}
        self.__dict__["data"] = {}

    def __setattr__(self, key, value):
        self.__dict__["data"][key] = value

    def __getattr__(self, key):
        return self.__dict__["data"].get(key)

    def __delattr__(self, key):
        self.__dict__["data"].pop(key)

    def show_data(self):
        print(self.__dict__["data"])

    def __str__(self):
        return str(self.__dict__["data"])


cache = Cache()
cache.name = "ckp"
cache.age = 18
# print(cache.__dict__)
print(cache.name)
# del cache.name

# cache.show_data()
print(cache)

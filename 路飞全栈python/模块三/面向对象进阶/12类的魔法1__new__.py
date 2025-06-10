# (1)  __new__()

"""
1. 开辟空间
2. __init__
3. 返回该空间地址
"""


# class Person(object):
#
#     def __new__(cls, *args, **kwargs):
#         print("__new__")
#         return object.__new__(cls)
#
#     def __init__(self, name, age):
#         print("__init__")
#         self.name = name
#         self.age = age
#
#
# ckp = Person("ckp", 18)
# print(ckp)
# print(ckp.age)
# print(ckp.name)

# __new__的应用案例

# class Config(object):
#
#     def __init__(self):
#         print('__init__')
#
# c1 = Config()
# c2 = Config()


class Config(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = object.__new__(cls)

        return cls.instance

    def __init__(self):
        print('__init__')

c1 = Config()
c2 = Config()
c3 = Config()
print(id(c1))
print(id(c2))
print(id(c3))












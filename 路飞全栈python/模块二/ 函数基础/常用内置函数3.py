# 高阶函数：以函数作为参数或者以函数作为返回值
# 函数是python的一等公民

# def foo():
#
#     print("foo")
#
#
# def bar():
#     print("bar")
#
#
# def dec(f):
#     print("start")
#     f()
#     print("end")
#
#
# dec(foo)
# dec(bar)

# filiter
# l = [23, 34, 56, 78, 15, 41]
#
#
# def get_even(item):
#     # if item % 2 == 0:
#     #     return True
#     # else:
#     #     return False
#
#     return item % 2 != 0
#
#
# print(list(filter(get_even, l)))

# print(list(filter(lambda x: x % 2 == 0, l)))


# map
# l = [23, 34, 56, 78, 15, 41]
#
# print(list(map(lambda x: x ** 2, l)))


# sorted
# data01 = [("ckp", 15), ("zz", 12), ("hyf", 34)]
#
# print(sorted(data01, key=lambda x: x[1], reverse=True))

data02 = [
    {"name" : "ckp", "age" : 23, "height" : 144},
    {"name" : "zz", "age" : 12, "height" : 134},
    {"name" : "hyf", "age" : 32, "height" : 184},
    {"name" : "sf", "age" : 26, "height" : 114},
]
# 年龄排序
print(list(sorted(data02, key=lambda d: d["age"])))
# 身高排序
print(list(sorted(data02, key=lambda d: d["height"])))
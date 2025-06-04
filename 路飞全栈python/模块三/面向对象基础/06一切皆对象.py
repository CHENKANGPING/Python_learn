"""
自定义对象是可变数据类型，可以在创建后，对其进行修改
添加或删除属性和方法，而不会改变对象的身份

实例对象也是一等公民 : 变量传递，作为函数参数，函数返回值

"""
from collections import namedtuple

from scipy.stats import alexandergovern


class Dog(object):
    legs = 4
    has_hair = True
    has_tail = True

    def __init__(self, name, breed, color, age, weight):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age
        self.weight = weight

    def bark(self):
        # print("self:::",self)
        print(f"{self.name}bark")

    def bite(self, person):
        print(f"{self.name}bite{person}")

    def fetch(self):
        print(f"{self.name}fetch")

    def show_info(self):
        print(f"{self.name}, 品种： {self.breed}, 颜色 : {self.color}, 年龄 : {self.age},体重 : {self.weight}")


zj = Dog("zj","渡边","blue","20","70")
# print(zj)
# print(type(zj))
# zj.age = 10
# print(zj.age)



# x = zj
# print(x.name)
# print(x.age)
#
# zj.age = 10000
# print(x.age)

# def foo(x):
#     print(x)
#     print(type(x))
#     x.append(4)
#
# # a = 1000
# # foo(a)
# b = [1,2,3]
# foo(b)
# print(b)

# def bar(y):
#     print(y,type(y))
#     y.age = 10000
#
# bar(zj)
# print(zj.age)


def test():
    hyf = Dog("zj", "渡边", "blue", "20", "70")

    return hyf

yf = test()

print(yf.breed)
print(yf.color)
print(yf.age)
print(yf.weight)
print(yf.name)

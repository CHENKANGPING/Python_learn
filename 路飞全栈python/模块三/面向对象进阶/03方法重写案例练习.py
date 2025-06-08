# class Animal(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print("eating")
#
#     def sleep(self):
#         print("sleeping")
#
#
# class Dog(Animal):
#
#     def __init__(self, name, age, breed):
#         super().__init__(name, age)
#         self.breed = breed
#
#     def swim(self):
#         print("swimming")
#
#     def sleep(self):
#         print("侧翻睡")
#
#
#
# class Bird(Animal):
#
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color
#
#     def climb_tree(self):
#         print("climbing tree")
#
#
# d1 = Dog("zj", 22, "斗牛犬")
#
# b1 = Bird("hyf", 21, "黑")
# b1.climb_tree()


class Base:
    def __init__(self):
        self.func()

    def func(self):
        print("in base")


class Son(Base):
    def func(self):
        print("in son")


s = Son()















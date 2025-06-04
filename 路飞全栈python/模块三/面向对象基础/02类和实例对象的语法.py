class Dog:
    legs = 4
    has_hair = True
    has_tail = True

    def bark(self):
        print("bark")

    def bite(self):
        print("bite")

    def fetch(self):
        print("fetch")

#
zj = Dog()
hyf = Dog()
# print(id(zj), id(hyf))

# 实例对象通过句点符号调用类的属性和方法
# print(zj.legs)
# print(hyf.legs)
# zj.bark()

# 调用类属性一定是同一个空间
print(id(zj.legs))
print(id(hyf.legs))
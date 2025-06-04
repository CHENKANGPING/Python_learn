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


zj = Dog()
hyf = Dog()

# 实例属性赋值 ： 实例对象.属性 = 值
# 向实例空间写入属性和值

zj.name = "张杰"
zj.age = 20
print(zj.name)

hyf.name = "和一反"
hyf.age = 22
print(hyf.name)

zj.age = 40
print(zj.age)

# 实例对象.变量 查询顺序[实例空间，类空间，父类空间]
zj.bark = 1000
# zj.bark()

hyf.bark()

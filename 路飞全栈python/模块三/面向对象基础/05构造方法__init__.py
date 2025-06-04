class Dog:

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

    def bite(self,person):
        print(f"{self.name}bite{person}")

    def fetch(self):
        print(f"{self.name}fetch")

    def show_info(self):
        print(f"{self.name}, 品种： {self.breed}, 颜色 : {self.color}, 年龄 : {self.age},体重 : {self.weight}")



"""
类实例化步骤
1. 开辟空间
2. 调用__init__实例空间地址
3. 将实例空间地址作为类的返回值

"""
zj = Dog("zj","渡边","blue","20","70")
zj.show_info()

# zj.init__prop("zj","渡边","blue","20")
# zj.show_info()
# zj.bark()
# print("zj:::", zj)
# zj.bark()
# hyf.bark()

# zj.bite("ckp")

# zj.name = "张杰"
# zj.age = 20
# zj.breed = "渡边"
# zj.color = "蓝色"
# zj.bark()
# zj.fetch()
# zj.bite("ckp")
# zj.show_info()
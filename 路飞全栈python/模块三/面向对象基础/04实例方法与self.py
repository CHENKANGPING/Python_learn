class Dog:
    legs = 4
    has_hair = True
    has_tail = True

    def bark(self):
        print("self:::",self)
        print(f"{self.name}bark")

    def bite(self,person):
        print(f"{self.name}bite{person}")

    def fetch(self):
        print(f"{self.name}fetch")

    def show_info(self):
        print(f"{self.name}, 品种： {self.breed}, 颜色 : {self.color}, 年龄 : {self.age}")


#
zj = Dog()
hyf = Dog()

# print("zj:::", zj)
# zj.bark()
# hyf.bark()

# zj.bite("ckp")

zj.name = "张杰"
zj.age = 20
zj.breed = "渡边"
zj.color = "蓝色"
zj.bark()
zj.fetch()
zj.bite("ckp")
zj.show_info()
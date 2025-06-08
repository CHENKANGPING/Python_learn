# class Animal(object):
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
#     def swim(self):
#         print("swimming")
#
#
#
# zj = Dog()
# zj.eat()
# zj.sleep()




class Animal(object):

    def eat(self):
        print("eating")

    def sleep(self):
        print("sleeping")


class Dog(Animal):

    def swim(self):
        print("swimming")


    def sleep(self):
        # 调用父类原方法
        # 方式1 类对象。方法（self,其他参数）
        # Animal.sleep(self)
        # 方式2 super
        super().sleep()
        print("侧翻睡")


dog = Dog()
dog.sleep()











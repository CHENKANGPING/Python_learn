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


class Bird:
    legs_nums = 2
    has_wings = True
    has_teech = False

    def fly(self):
        print("fly")

    def eat_warms(self):
        print("eat_warms")

    def nest(self):
        print("nest")

zj = Dog()
print(zj.legs)
zj.bark()


hyf = Bird()
print(hyf.has_wings)
print(hyf.has_teech)
hyf.fly()

class Animal(object):

    def eat(self):
        print("eating")

    def sleep(self):
        print("sleeping")


class Dog(Animal):

    def swim(self):
        print("swimming")


class Cat(Animal):

    def cute(self):
        print("cute")


class birds(Animal):

    def fly(self):
        print("flying")




zj = Dog()
zj.eat()
zj.sleep()

hyf = birds()
hyf.eat()
hyf.fly()

hly = Cat()
hly.eat()
hly.cute()
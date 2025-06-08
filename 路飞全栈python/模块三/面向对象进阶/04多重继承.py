class Animal(object):

    def eat(self):
        print("eating")

    def sleep(self):
        print("sleeping")


class Dog(Animal):

    def swim(self):
        print("swimming")


class Fly(object):

    def fly(self):
        print("flying")


class Eagle(Animal, Fly):
    pass


class Bat(Animal, Fly):
    pass

b1 = Bat()
b1.fly()
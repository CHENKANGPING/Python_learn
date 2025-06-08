# type  and  isinstance

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
# zj = Dog()
#
# print(type(zj))
# print(isinstance(zj, Dog))
# print(isinstance(zj, Animal))



# dir函数 和  __dict__

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def test(self):
        pass


zj = Student("zj", 100)
print(zj.__dict__)

print(dir(zj))












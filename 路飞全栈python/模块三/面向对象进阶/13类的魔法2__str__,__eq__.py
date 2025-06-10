# __str__
# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
#
#
# ckp = Person("ckp", 18)
# print(ckp)
#
# zj = Person("zj", 22)
# print(zj)

# __eq__

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name


ckp = Person("ckp", 18)
zj = Person("zj", 19)

print(ckp == zj)
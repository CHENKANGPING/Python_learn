# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         # 私有化 : __score
#         # 外部代码不能随意修改对象内部的状态
#         self.__score = score
#
#     # 开放的一个查询成绩的接口
#     def get_score(self):
#         return self.__score
#
#     def set_score(self, score):
#
#         if isinstance(score, int) and 0 < score < 100:
#             self.__score = score
#         else:
#             raise ValueError("score must be between 0 and 100")
#
#
#
# ckp = Student("ckp", 90)
#
#
# print(dir(ckp))
# print(ckp.__dir__())

# 父类子类都私有
class Person(object):

    def __init__(self, name, score):
        self.name = name
        self._score = score


class Student(Person):

    def get_score(self):
        return self._score

    def set_score(self, score):
        self._score = score

ckp = Student("ckp", 66)
print(ckp.__dict__)










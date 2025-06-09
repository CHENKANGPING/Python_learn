from loguru import logger


# class Student(object):
#
#     def __init__(self, name, score):
#         self.__name = name
#         # 私有化 : __score
#         # 外部代码不能随意修改对象内部的状态
#         self.__score = score
#
#     @property
#     # 开放的一个查询成绩的接口
#     def score(self):
#
#         logger.info(f"{self.__name}查询了成绩：{self.__score}")
#
#         return self.__score
#
#     @score.setter
#     def score(self, score):
#
#         if isinstance(score, int) and 0 < score < 100:
#             self.__score = score
#         else:
#             raise ValueError("score must be between 0 and 100")
#
#
# ckp = Student("ckp", 90)
# ckp.score = 98
# print(ckp.score)

# property内置函数

class Student(object):

    def __init__(self, name, score):
        self.name = name
        # 私有化 : __score
        # 外部代码不能随意修改对象内部的状态
        self.__score = score

    # 开放的一个查询成绩的接口
    def get_score(self):
        return self.__score

    def set_score(self, score):

        if isinstance(score, int) and 0 < score < 100:
            self.__score = score
        else:
            raise ValueError("score must be between 0 and 100")

    score = property(get_score, set_score)

ckp = Student("ckp", 90)
print(ckp.score)
ckp.score = 99
print(ckp.score)
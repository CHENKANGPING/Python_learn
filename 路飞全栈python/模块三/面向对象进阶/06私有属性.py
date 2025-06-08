"""
指隐藏对象的属性和实现细节
仅对外提供公共访问的方式

把该隐藏的隐藏起来
该暴露的暴露出来


"""


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



ckp = Student("ckp", 90)

print(ckp.get_score())

ckp.set_score(99)
print(ckp.get_score())

ckp.set_score(1000)

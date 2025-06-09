class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


ckp = Person("ckp", 90, "male")

# 对象.属性变量
# print(ckp.name)
# ckp.age = 20
# print(ckp.age)

# 反射
while 1:
    attr = input("请输入您想查询的ckp的某个属性")

    if hasattr(ckp, attr):

        val = getattr(ckp, attr)
        print(f"ckp的{attr}的属性值：{val}")
    else:
        print(f"ckp没有{attr}属性")
        choice = input(" 是否给ckp加入该属性[Y/N] ")

        if choice.lower() == "y":
            value = input(f"请输入ckp对象{attr}一个确定值：")

            setattr(ckp, attr, value)
















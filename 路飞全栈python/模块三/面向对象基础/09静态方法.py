class Cal(object):

    @staticmethod
    def add(x, y):
        return x + y


    @staticmethod
    def mul(x, y):
        return x * y

# 实例对象调用
c = Cal()
print(c.add(1, 2))

# 类对象调用
print(Cal.add(1, 2))
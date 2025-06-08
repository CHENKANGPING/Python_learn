class Cars(object):
    # 类属性
    total_car = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.__class__.total_car += 1

    # 实例方法
    def accelerate(self):
        print(f"一辆{self.make}的{self.model}正在加速")

    # 类方法
    @classmethod
    def show_total_cars(cls):
        print(id(cls))
        print(f"当前的total_cars:{cls.total_car}")

print(id(Cars))
Cars.show_total_cars()

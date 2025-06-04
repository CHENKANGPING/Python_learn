class Car(object):
    # 类属性
    total_car = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.total_car += 1

    # 实例方法
    def accelerate(self):
        print(f"一辆{self.make}的{self.model}正在加速")




# car2.accelerate()
# car2 = Car("Honda","Accord")

# Car : 类对象 调用空间储存的属性和方法

# print(id(Car))
# print(Car.total_car)
# Car.total_car = 1
# print(Car.total_car)

# car1 = Car("Toyota","Camry")

# print(car1.total_car)

car1 = Car("Toyota","Camry")
car2 = Car("Honda","Accord")
print(Car.total_car)





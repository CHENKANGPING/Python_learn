# 在面向对象编程中 程序中的数据和操作数据的函数时一个逻辑上的整体
# 称之为对象
# 对象可以接受消息
# 解决问题的方法就是创建对象并向对象发出各种各样的消息
# 通过消息传递 程序中的多个对象可以协同工作
# 这样就能构造出复杂的系统并且解决现实中的问题
# 把一组数据和处理数据的方法组成对象 把行为相同的对象归纳为类
# 通过封装隐藏对象的内部细节 通过继承实现类的特化和泛化
# 通过多态实现基于对象类型的动态分派

# 定义类
# 使用class关键字加上类名来定义类
# 写在类里面的函数称之为方法
# 方法就是对象的行为
# 也是对象可以接受的消息
# 方法的第一个参数通常是self
# 它代表了接受这个消息的对象本身

class Student:
    def study(self, course_name):
        print(f' 学生正在学习{course_name}.')
    
    def play(self):
        print(f' 学生正在玩游戏.')
        
        
# 创建和使用对象
stu1 = Student()
stu2 = Student()

print(stu1)
print(stu2)

print(hex(id(stu1)), hex(id(stu2)))

# 给对象发下消息
# 通过'类.方法' 调用方法
# 第一个参数是接受消息的对象
# 第二个参数是学习的课程名称
Student.study(stu1, 'python程序设计')

# 通过'对象.方法'调用方法
# 点前面的对象就是接收消息的对象
#只需要传入第二个参数课程名称
stu1.study('pthon程序设计')

Student.play(stu2)

stu2.play()


print('--------------------------------------------------')


# 初始化方法
class Student:
    """学生"""
    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age
        
    def study(self, course_name):
        """学习"""
        print(f'{self.name} 正在学习 {course_name}.')
        
    def play(self):
        """玩耍"""
        print(f'{self.name} 正在玩游戏.')
        
        
stu1 = Student('ckp', 23)
stu2 = Student('hyf', 21)
stu1.study('python程序设计')
stu2.play()


print('--------------------------------------------------')


# 案例
# 1.时钟
import time

# 定义时钟类
class Clock:
    """数字时钟"""
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def run(self):
        """走字"""
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute +=1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0
                    
    def show(self):
        """显示时间"""
        return f'{self.hour:0>2d} : {self.minute:0>2d} : {self.second:0>2d}'
    
    
# 创建时钟对象
clock = Clock(23, 59, 58)
while True:
    # 给时钟对象发消息读取时间
    print(clock.show())
    # 休眠一秒
    time.sleep(0.1)
    # 给时钟对象发消息使其走字
    clock.run()
    
    
print('--------------------------------------------------')


# 平面上的点
class Point:
    """平面上的点"""
    def __init__(self, x = 0, y = 0):
        self.x, self.y = x, y
        
    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return(dx * dx + dy * dy ) ** 0.5
    
    def __str__(self):
        return f'{self.x}, {self.y}'
    
p1 = Point (3,5)
p2 = Point (6,9)

print(p1)
print(p2)
print(p1.distance_to(p2))        
    
    
        

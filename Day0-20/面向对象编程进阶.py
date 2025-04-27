"""
    可见性和属性装饰器
    在很多面向对象编程中
    对象的属性通常会被设置为私有或受保护
    不允许直接访问这些属性
    在python中可以通过给对象属性名添加下划线
    来说明属性的访问可见性
    __name表示一个私有属性
    _name表示一个受保护属性
"""
class Student:
    def __init__(self, name, age):
        self.__naem = name
        self.__age = age
        
    def study(self, course_name):
        print(f'{self.__naem} 正在学习 {course_name}:')
        
stu = Student('ckp', 20)
stu.study('sfafasf')
# print(stu.__naem) # AttributeError: 'Student' object has no attribute '__naem'


print('--------------------------------------------------')


"""
    动态属性
    python属于动态语言
    在运行时可以改变其结构的语言
    我们可以动态的为对象添加属性
    
"""
class Student1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
stu = Student1('ckp', 22)
stu.sex = '男'


print('--------------------------------------------------')


"""
    如不希望在使用对象时动态的为对象添加属性
    可以使用python中的__slots__魔法
    对于Student类来说
    可以在类中指定__slots__('name','age')
    这样就只能有name age 属性
    
"""
class Student2:
    __slots__ = ('name', 'age')
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
stu = Student2('ckp', 22)
# stu.sex = "男" AttributeError: 'Student2' object has no attribute 'sex'


print('--------------------------------------------------')


"""
    静态方法和类方法
"""
class Triangle:
    """三角形"""
    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c
    
    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and a + c > b and c + b > a
    
    # @classmethod
    # def is_valid(a, b, c):
    #     """判断三条边长能否构成三角形(类方法)"""
    #     return a + b > c and a + c > b and c + b > a
    
    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c
    
    def area(self):
        """计算面积"""
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
    
    
print('--------------------------------------------------')


# property装饰器
class Triangle1:
    """三角形"""
    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c
    
    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and a + c > b and c + b > a
    
    @property
    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c
    
    @property
    def area(self):
        """计算面积"""
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
    

t = Triangle1(3,4,5)
print(f'周长：{t.perimeter}')
print(f'面积；{t.area} ')


print('--------------------------------------------------')


"""
    继承和多态
    面向对象的编程语言
    支持在已有类的基础上创建新类
    从而减少重复代码
    提供继承消息的类叫做父类
    得到继承信息的类叫子类
    
"""
# 定义一个学生类和老师类
# 先定义人类
# 再通过继承
# 从人类派生出老师类和学生类

class Person:
    """人"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f'{self.name} 正在吃饭.')
        
    def sleep(self):
        print(f'{self.name} 正在睡觉.')
        
class Student3(Person):
    """学生"""
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def study(self, course_name):
        print(f'{self.name} 正在学习 {course_name}')
        

class Teacher(Person):
    """老师"""
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title
        
    def teach(self, course_name):
        print(f'{self.name}{self.title} 正在讲授 {course_name}')
        
stu1 = Student3('ckp', 22)
stu2 = Student3('hyf', 21)
tea1 = Teacher('hhh', 45, '1')
stu1.eat()
stu2.sleep()
tea1.eat()
stu1.study('sfafa')
stu2.study("sfefsfgs")
tea1.teach('efafdsfsdfsefs')

    
    
        



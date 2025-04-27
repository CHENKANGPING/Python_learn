# 扑克牌游戏
"""
    说明 52张牌 将52张牌发到4个玩家手中 每个玩家有13张牌 
    按照黑桃 红心 草花 方块的顺序和点数从大到小排序
    分析 这个游戏至少有三个类 牌 扑克 玩家
    类与类之间的关系
    is_a 继承关系
    has_a 关联关系
    use_a 依赖关系
    扑克和牌属于has_a 关系
    因为一副牌有52张牌
    玩家和牌不仅有关联关系和依赖关系
    
"""
from enum import Enum

class Suite(Enum):
    """花色(枚举)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)
    
# for suite in Suite:
#     print(f'{suite} : {suite.value}')
    
class Card:
    """牌"""
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face
        
    def __repr__(self):
        suites = '♠♥♣♦'
        face = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{face[self.face]}'
    
    def __lt__(self, other):
        if self.suite == other.suite:
            return self.face < other.face
        return self.suite.value < other.suite.value
    
# card1 = Card(Suite.SPADE, 5)
# card2 = Card(Suite.HEART,13)
# print(card1)
# print(card2)

import random
class Poker:
    """扑克"""
    def __init__(self):
        self.cards = [Card(suite, face)
                        for suite in Suite
                        for face in range(1, 14)]
        self.current = 0
        
    def shuffle(self):
        """洗牌"""
        self.current = 0
        random.shuffle(self.cards)

    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card
    
    @property
    def has_next(self):
        """还有没有可以发的牌"""
        return self.current < len(self.cards)
    
# pork = Pork()
# print(pork.cards)
# pork.shuffle()
# print(pork.cards)        

class Player:
    """玩家"""
    def __init__(self, name):
        self.name = name
        self.cards = []
        
    def get_one(self, card):
        """摸牌"""
        self.cards.append(card)

    def arrange(self):
        """整理手牌"""
        self.cards.sort()
        
poker = Poker()
poker.shuffle()
players = [Player('ckp'), Player('hyf'), Player('zj'), Player('XXX')]
for _ in range(13):
    for player in players:
        player.get_one(poker.deal())
        
for player in players:
    player.arrange()
    print(f'{player.name}: ', end = '')
    print(player.cards)
    
    
print('--------------------------------------------------')


"""
    工资结算系统
    某公司有三种类型的员工，分别是部门经理、程序员和销售员。
    需要设计一个工资结算系统，根据提供的员工信息来计算员工的月薪。
    其中，部门经理的月薪是固定 15000 元；
    程序员按工作时间（以小时为单位）支付月薪，每小时 200 元；
    销售员的月薪由 1800 元底薪加上销售额 5% 的提成两部分构成。
    
"""
from abc import ABCMeta, abstractmethod

class Employee(metaclass = ABCMeta):
    """员工"""
    def __init__(self,name):
        self.name = name
        
    @abstractmethod
    def get_salary(self):
        """结算月薪"""
        pass
    


class Manager(Employee):
    """部门经理"""
    def get_salary(self):
        return 1500.0
    


class Programmer(Employee):
    """程序员"""
    
    def __init__(self, name, working_hour = 0):
        super().__init__(name)
        self.working_hour = working_hour
        
    def get_salary(self):
        return 200 * self.working_hour
    
    
class Salesman(Employee):
    """销售员"""
    def __init__(self, name, sales = 0):
        super().__init__(name)
        self.sales = sales
        
    def get_salary(self):
        return 1800 + self.sales * 0.5
    
emps = [Manager('hyf'), Programmer('ckp'), Salesman('zj'), Programmer('xxx'), Salesman('zzz')]
for emp in emps:
    if isinstance(emp, Programmer):
        emp.working_hour = int(input(f'请输入 {emp.name} 本月工作时间：'))
    elif isinstance(emp,Salesman):
        emp.sales = float(input(f'请输入 {emp.name} 本月销售额：'))
    print(f'{emp.name} 本月工资： ￥{emp.get_salary():.2f} 元')


        
        
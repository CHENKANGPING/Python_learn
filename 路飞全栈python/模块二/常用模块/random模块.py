"""
random() 生成一个0到1的随机浮点数。
randint(a, b) 生成一个指定范围内恩典随机整数包括ab
choice(seq) 给定序列中的随机选择一个元素。
sample(seq, k) 给定序列中的随机选择k元素，返回一个新的列表。
shuffle(seq) 随机打乱给定序列的顺序。

"""

import random
#
# print(random.random())
# print(round(random.random(), 4))
#
# print(round(random.random() * 100))

# 投硬币

# def flip_coin():
#     if random.random() >= 0.5:
#         return "heads"
#     else:
#         return "tails"
#
# print(flip_coin())


# print(random.randint(1, 2))

# 掷色子

# def roll_dice():
#     return random.randint(1, 6)
#
# print(roll_dice())


# print(random.choice([1, 2, 3, 4, 5]))


# 抽奖

# def draw_prize():
#     p = ["ckp", "zj", "hyf"]
#     result = random.choice(p)
#     return result
#
# print(draw_prize())
#
# print(random.sample([11,22,33,44,55], 3))



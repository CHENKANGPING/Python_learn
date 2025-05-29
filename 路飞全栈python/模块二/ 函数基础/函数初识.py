# 打印52张扑克牌
# poke_types = ['♥','♦','♠','♣']
# poke_nums = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
#
# for p_type in poke_types:
#     for p_num in poke_nums:
#         print(f'{p_type}:{p_num}', sep = "\t", end = "")
#     print()

# 函数版本
# 函数声明（变量声明） （一次声明，多次调用）
"""
def 函数名():
    函数体

"""

def print_pokes():
    poke_types = ['♥', '♦', '♠', '♣']
    poke_nums = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']

    for p_type in poke_types:
         for p_num in poke_nums:
             print(f'{p_type}:{p_num}', sep = "\t", end = "")
         print()

# 函数调用 
print_pokes()



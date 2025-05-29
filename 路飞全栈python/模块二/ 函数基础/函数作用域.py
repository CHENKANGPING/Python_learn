#   L -> E -> G -> B
# 案例一

# x = 1
#
# def foo():
#     x = 10
#     print("foo:", x)
#
# foo()
# print(x)

# 案例二

# x = 1
# y = 2
# def test01():
#     x = 10
#
#     def test02():
#         x = 100
#         print("test02的x:",x)
#
#     test02()
#     print("hello test01")
#
# test01()

# 案例三

# def test(x,y):
#     print(x)
#     print(y)
#
# x = 1
# y = 2
# test(x,y)

# # 案例四
# def foo():
#     x =10
#
#
# def bar():
#     y = 20
#     print(y)

# 案例五

poke_types = ['♥', '♦', '♠', '♣']
poke_nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

def print_pokes():


    for p_type in poke_types:
         for p_num in poke_nums:
             print(f'{p_type}:{p_num}', sep = "\t", end = "")
         print()


print_pokes()
print_pokes()

# def cal():
#     n = 100
#     ret = 0
#     for i in range(1, n + 1):
#         ret += i
#     print(ret)
#
# cal()


def cal(n): # 形式参数
    ret = 0
    for i in range(1, n + 1):
        ret += i
    print(ret)

cal(100) # 实际参数
cal(1000)
cal(8888)
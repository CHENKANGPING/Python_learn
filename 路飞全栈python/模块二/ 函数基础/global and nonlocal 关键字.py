# global 和 nonlocal 关键字

# x = 1
#
# def foo():
#     global x
#     # print(id(x))
#     x = 10
#     print("foo的x：",x)
#
# foo()
# # print(id(x))
# print("全局的x：",x)

# nonlocal
x = 10

def foo():
    x = 100

    def bar():
         # 修改foo的x
        nonlocal  x
        x = 1000
        print("bar的x：",x)

    bar()
    print("foo的x:", x)

foo()
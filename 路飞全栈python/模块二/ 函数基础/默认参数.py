# 案例1
# def show_info(name, age, height, weight, gender = "男"):
#      print(f"姓名：{name}")
#      print(f"年龄：{age}")
#      print(f"身高{height}")
#      print(f"体重{weight}")
#      print(f"性别{gender}")
#
# show_info("HiiAen", "22", "177", "68")
# show_info("lili", "22", "175", "68", gender = "女")


# 案例2



# def cal_shopping_cart(cart, discount = 0.8):
#     total = 0
#     for goods in cart:
#         total += goods["price"] * goods["quantity"]
#
#     total = round(total * discount)
#
#     print(total)
#
# shopping_cart1 = [
#         {
#             "name" : "mac电脑",
#             "price" : 1000,
#             "quantity" : 10,
#         },
#         {
#             "name" : "iphone15",
#             "price" : 2000,
#             "quantity" : 3,
#         }
#     ]
# shopping_cart2 = [
#         {
#             "name" : "mac电脑",
#             "price" : 1000,
#             "quantity" : 1,
#         },
#         {
#             "name" : "iphone15",
#             "price" : 2000,
#             "quantity" : 30,
#         }
#     ]
# shopping_cart3 = [
#         {
#             "name" : "mac电脑",
#             "price" : 1000,
#             "quantity" : 22,
#         },
#         {
#             "name" : "iphone15",
#             "price" : 2000,
#             "quantity" : 1,
#         }
#     ]
#
# cal_shopping_cart(shopping_cart1)
# cal_shopping_cart(shopping_cart2)
# cal_shopping_cart(shopping_cart3, 0.1)


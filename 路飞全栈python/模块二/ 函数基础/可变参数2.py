# **kwargs
# 函数调用
# def print_info(name, age, gender):
#     print(name)
#     print(age)
#     print(gender)
#
# data = {"name" : "ckp", "age" : 22, "gender" : "男"}
#
# # **data => name="yuan", age=18, gender="男“
# # 字典的解包（打散字典）
#
# print_info(**data)




# **kwargs用于接收任意数量的关键字参数
# *args用于接收任意数量的位置参数

# def send_email(recipient, subject, content, **kwargs):
#     print("连接服务器")
#     print(f"收件人邮箱：{recipient}")
#     print(f"主题：{subject}")
#     print(f"内容:{content}")
#
#     cc = kwargs.get("cc")
#     bcc = kwargs.get("bcc")
#     if cc:
#         print("抄送人", cc)
#
#     if bcc:
#         print("密送人", bcc)

# r = "HiiAen@qq.com"
# c = "HiiAen,涨薪"
# s = "重要通知"
#
# send_email(r, s, c, cc="alex@qq.com", bcc="zz@qq.com")

# *arge and **kwargs的结合

def test(a, *b, **c):
    print(a)
    print(b)
    print(c)

test(1, 2, 3, 4, 5, x = 10, y = 20)
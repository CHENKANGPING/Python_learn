# def add(x, y):
#     c = x + y
#     print(c)
#
# add(1, 2)
# add(39,23)


# def cal(start, end):
#     ret = 0
#     for i in range (start, end + 1):
#         ret += i
#     print(ret)
#
# cal(99, 100)
# cal(80, 100)

# 发邮件

def send_email(recipient, subject, content):
    print("连接服务器")
    print(f"收件人邮箱：{recipient}")
    print(f"主题：{subject}")
    print(f"内容:{content}")

r = "HiiAen@qq.com"
c = "HiiAen,"
s = "重要通知"
send_email(r, s, c)


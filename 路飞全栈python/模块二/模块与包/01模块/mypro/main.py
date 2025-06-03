import cal
import commnication
import mysql

def two_value_cal():
    exp = input("请输入双值计算表达式")
    if exp.find("+") != -1:
        a, b = exp.split("+")
        print(f"{a} + {b} = {cal.add(int(a), int(b))}")
    elif exp.find("-") != -1:
        a, b = exp.split("-")
        print(f"{a} - {b} = {cal.sub(int(a), int(b))}")
    elif exp.find("*") != -1:
        a, b = exp.split("*")
        print(f"{a} * {b} = {cal.mul(int(a), int(b))}")
    elif exp.find("/") != -1:
        a, b = exp.split("/")
        print(f"{a} / {b} = {cal.div(int(a), int(b))}")

while 1:
    print("1. 科学计数")
    print("2. 数据库操作")
    print("3. 信息通讯")
    choice = input("请选择：")
    if choice == "1":
        two_value_cal()

    elif choice == "2":
        action = input("""
            1. 添加记录
            2. 删除记录
            3. 更新记录
            4. 查询记录
        """)
        if action == "1":
            mysql.mysql_insert()
        elif action == "2":
            mysql.mysql_delete()
        elif action == "3":
            mysql.mysql_update()
        elif action == "4":
            mysql.mysql_query()

    elif choice == "3":
        commnication.send_email()
        commnication.send_sms()










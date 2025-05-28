def show_info(name, age, height = None, weight = None):
    print("*" * 20)
    print(f"【姓名：{name}】")
    print(f"【年龄：{age}】")
    if height:
        print(f"【身高：{height}】")
    if weight:
        print(f"【体重：{weight}】")
    print("*" * 20)


show_info("zz", 22, 173, 65)
show_info("ckp", 22)
show_info("ckp", 22,weight=65)
 
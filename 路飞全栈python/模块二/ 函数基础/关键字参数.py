def show_info(name, age, height, weight):
    print("*" * 20)
    print(f"【姓名：{name}】")
    print(f"【年龄：{age}】")
    print(f"【身高：{height}】")
    print(f"【体重：{weight}】")
    print("*" * 20)


# show_info("ckp", 22, 173, 65)
show_info("ckp", 22, weight=65, height=170)

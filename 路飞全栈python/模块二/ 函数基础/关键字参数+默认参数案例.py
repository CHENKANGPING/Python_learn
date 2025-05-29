def check_air_ticket(from_, to_, date="2025-5-21", seat_class="经济舱", max_price = None):
    query = f"数据库查询：日期：{date},{from_}-{to_}的所有{seat_class}"

    if max_price is not None:
        query = query + f"最高价格不要超过{max_price}元"

    query += "的飞机票"

    print(query)


check_air_ticket("北京", "上海" , max_price=2000)
check_air_ticket("北京", "上海" , max_price=5000,date="2025-5-24")


def cal(start, end = None):
    if end is None:
        start, end = 1, start

    ret = 0
    for i in range(start, end+1):
        ret += i
    print(ret)

cal(1,100)
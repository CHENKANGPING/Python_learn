import threading

import requests
import re
import time




# （1） 爬虫与文件操作
# res = requests.get("https://pic.netbian.com/uploads/allimg/250616/102619-1750040779f0ca.jpg")
#
# with open("test.jpg", "wb") as f:
#     f.write(res.content)

# (2) 批量下载
# 爬取1页

# start = time.time()
# # 爬取10页
# n = 1
# for page in range(2, 12):
#     res = requests.get(f"https://pic.netbian.com/4kyouxi/index_{page}.html")
#
#     # print(res.text)
#
#     ret = re.findall("/uploads/allimg/.*?.jpg", res.text)
#     print(ret)
#
#     domian = "https://pic.netbian.com/"
#
#     for path in ret:
#         url = domian + path
#
#         res = requests.get(url)
#
#         with open(f"./images/{n}.jpg", "wb") as f:
#             f.write(res.content)
#
#         print(f"{n}.jpg下载成功！")
#         n += 1
#
# print("耗时:", time.time() - start)


# 多线程并发

def get_one_img(path, n):
    domai = "https://pic.netbian.com/"
    url = domai + path

    res = requests.get(url)

    with open(f"./images/{n}.jpg", "wb") as f:
        f.write(res.content)

    print(f"{n}.jpg下载成功！")


def main():
    start = time.time()
    # 爬取10页
    t_list = []
    n = 1
    for page in range(2, 12):
        res = requests.get(f"https://pic.netbian.com/4kyouxi/index_{page}.html")

        # print(res.text)

        ret = re.findall("/uploads/allimg/.*?.jpg", res.text)
        print(ret)

        for path in ret:
            # 创建线程对象
            t = threading.Thread(target=get_one_img, args=(path, n))
            t.start()
            t_list.append(t)

            n += 1

    for t in t_list:
        t.join()
    print("耗时:", time.time() - start)


if __name__ == '__main__':
    main()

import threading
import time
import multiprocessing


def cal(n):
    ret = 0
    for i in range(1,n):
        ret += i

    print(ret)

# start = time.time()
# cal(100000000)
# cal(100000000)
# cal(100000000)
# end = time.time()
# print(end - start)


# 线程并发
# start = time.time()
# t1 = threading.Thread(target=cal, args=(100000000, ))
# t1.start()
# t2 = threading.Thread(target=cal, args=(100000000, ))
# t2.start()
# t3 = threading.Thread(target=cal, args=(100000000, ))
# t3.start()
# t1.join()
# t2.join()
# t3.join()
#
# end = time.time()
# print(end - start)



# 多进程并发
if __name__ == '__main__':
    start = time.time()

    p1 = multiprocessing.Process(target=cal, args=(100000000,))
    p1.start()
    p2 = multiprocessing.Process(target=cal, args=(100000000,))
    p2.start()
    p3 = multiprocessing.Process(target=cal, args=(100000000,))
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    end = time.time()
    print(end - start)



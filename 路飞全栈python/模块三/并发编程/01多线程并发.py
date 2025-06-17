import time
import threading

# (1) 串行
# def spider01():
#     print('spider01 start')
#     time.sleep(3)
#     print('spider01 end')
#
#
# def spider02():
#     print('spider02 start')
#     time.sleep(5)
#     print('spider02 end')
#
#
# start = time.time()
# spider01()
# spider02()
# end = time.time()
# print("时间开销", end - start)


# (2)多线程

def spider01(timer):
    print('spider01 start')
    time.sleep(timer)
    print('spider01 end')


def spider02(timer):
    print('spider02 start')
    time.sleep(timer)
    print('spider02 end')


start = time.time()

# 创建线程对象
t1 = threading.Thread(target=spider01,args=(3,))
# 线程对象就绪启动
t1.start()

t2 = threading.Thread(target=spider02,args=(5,))
t2.start()

# 阻塞等待
t1.join()
t2.join()


end = time.time()
print("时间开销", end - start)

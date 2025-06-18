import queue
import threading
import time

q = queue.Queue()

def producer():
    for i in range(1,11):
        time.sleep(1)
        q.put(i)
        print(f"生产者生产了消息{i}")



def consumer():

    while 1:
        val = q.get()
        print(f"消费者消费的值：{val}")
        time.sleep(2)
        if val == 10:
            break


p = threading.Thread(target=producer)
p.start()
c = threading.Thread(target=consumer)
c.start()

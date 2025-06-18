import  threading
import time

x = 0


lock = threading.Lock()
def add():
    # 锁门
    lock.acquire()
    global x
    temp = x + 1
    time.sleep(0.01)
    x = temp
    # 开门
    lock.release()

t_list = []
for i in range(100):
    t  = threading.Thread(target=add)
    t.start()
    t_list.append(t)


for t in t_list:
    t.join()
print(x)
import time
import redis
import uuid
import threading

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

def delay_task(name,delay_time):
    task_id = str(uuid.uuid4())
    process_Time = time.time() + delay_time
    r.zadd("delay-queue",{name+task_id:process_Time})

def loop():
    while 1:
        task_list = r.zrangebyscore("delay-queue",0,time.time(),0,1)
        if  not task_list:
            print("cost 1秒")
            time.sleep(1)
            continue

        task = task_list[0]

        ok = r.zrem("delay-queue",task)
        if ok:
            handleTask(task)




def handleTask(task_id):
    print(f"任务{task_id}执行完毕！")

t = threading.Thread(target=loop)
t.start()

delay_task("任务1",5)
delay_task("任务2",2)
delay_task("任务3",4)
delay_task("任务4",10)










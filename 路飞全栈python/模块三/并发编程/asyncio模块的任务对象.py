import asyncio
import time

def task01_callback(result):
    print("hello world")



async def work(i):
    print(f'task {i} start')
    await asyncio.sleep(i)  # 模拟io事件
    print(f'task {i} end')
    return i ** 2


# 创建了一个协程对象
# print(task(1)) # coroutine

start = time.time()
# （1） 构建事件循环对象
loop = asyncio.get_event_loop()

# （2） 构建协程对象
# tasks = [task(1), task(2)]


# 给任务1对象绑定一个回调函数


works = [
    asyncio.ensure_future(work(1)),
    asyncio.ensure_future(work(2))
]


works[0].add_done_callback(task01_callback)
# （3） 收集任务等待
loop.run_until_complete(asyncio.wait(works))
# print(works[0].done())
# print(works[0].result())

# for work in works:
#     print(work.result())

end = time.time()
print(end - start)

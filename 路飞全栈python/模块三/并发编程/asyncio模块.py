import asyncio
import time


async def task(i):
    print(f'task {i} start')
    await asyncio.sleep(i) # 模拟io事件
    print(f'task {i} end')

# 创建了一个协程对象
# print(task(1)) # coroutine

start = time.time()
# （1） 构建事件循环对象
loop = asyncio.get_event_loop()

# （2） 构建协程对象
tasks = [task(1), task(2)]

# （3） 收集任务等待
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print(end - start)
import asyncio
import time


def task01_callback(result):
    print("hello world")


async def work(i):
    print(f'task {i} start')
    await asyncio.sleep(i)  # 模拟io事件
    print(f'task {i} end')
    return i ** 2


async def main():
    start = time.time()

    works = [
        asyncio.create_task(work(1)),
        asyncio.create_task(work(2)),
        asyncio.create_task(work(3))
    ]

    works[0].add_done_callback(task01_callback)

    ret = await asyncio.gather(*works)
    print(ret)
    end = time.time()
    print(end - start)


asyncio.run(main())

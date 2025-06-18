from concurrent.futures import ThreadPoolExecutor
import time


def task(i):
    print(f"任务{i}开始！")
    time.sleep(3)
    print(f"任务{i}结束！")
    return i


start = time.time()
pool = ThreadPoolExecutor(3)

future_list = []
for i in range(1, 11):
    future = pool.submit(task, i)
    future_list.append(future)


pool.shutdown()
end = time.time()
print(f"耗时：{end - start}")
print("future_list:", future_list)
print([future.result() for future in future_list])
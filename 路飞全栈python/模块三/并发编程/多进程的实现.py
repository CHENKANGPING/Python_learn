import time
import multiprocessing


def foo():
    print("foo start...")
    time.sleep(5)
    print("foo end...")


def bar():
    print("bar start...")
    time.sleep(3)
    print("bar end...")

if __name__ == '__main__':
    start = time.time()
    p1 = multiprocessing.Process(target=foo)
    p1.start()
    p2 = multiprocessing.Process(target=bar)
    p2.start()

    p1.join()
    p2.join()
    print("finished!")
    end = time.time()
    print(end - start)



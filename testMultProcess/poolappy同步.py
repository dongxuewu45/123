from multiprocessing import Process, Pool
from multiprocessing import Manager
import time


def f1(a):
    time.sleep(2)
    print(a)


if __name__ == '__main__':
    pool = Pool(5)
    for i in range(5):  # 每次使用的时候会去进程池里面申请一个进程
        pool.apply(func=f1, args=(i,))
        print('你好')  # apply里面是每个进程执行完毕了才执行下一个进程
    pool.close()  # 执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    pool.join()  # 等待进程运行完毕，先调用close函数，否则会出错
    print('主程序end')
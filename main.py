import sys

sys.path.append('../')

from multiprocessing import Process
from proxy_pool.core.run_spider import RunSpider
from proxy_pool.core.proxy_test import ProxyTest
from proxy_pool.core.proxy_api import ProxyApi


def run():
    process_list = list()
    process_list.append(Process(target=RunSpider.start))
    process_list.append(Process(target=ProxyTest.start))
    process_list.append(Process(target=ProxyApi.start))

    # 每个进程都创建一个列表，然后添加一个因素进去，
    # 每个进程之间的数据是不能共享的
    # 如果将代码改成threading，由于线程共用内存，所以结果是不一样的，线程操作列表li之前，拿到的是前一个线程操作过的li列表，如图

    for process in process_list:
        process.daemon = True #将daemon设置为True，则主线程不比等待子进程，主线程结束则所有结束
        process.start()

    for process in process_list:
        process.join()


if __name__ == "__main__":
    run()
    print('end')  #默认情况下等待所有子进程结束，主进程才结束
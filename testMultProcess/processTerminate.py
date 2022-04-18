import time
from  multiprocessing import Process


def task(name):
    print('%s is runing' % name)
    time.sleep(1)
    print('%s is done' % name)


if __name__ == '__main__':
    p1 = Process(target=task, args=('xiaojiu',))
    p2 = Process(target=task, args=('hh',),name=('子进程2')) #改变进程名称
    p3 = Process(target=task, args=('wawa',))

    p1.start()
    # p1.join() #这里xiaojiu 执行完毕之后才会执行其他进程
    p1.terminate() #关闭进程，不会立即关闭，因为关闭的是进程信号。
    print(p1.is_alive()) #查看是否存活
    print(p1.name) #可以查看进程的名称 # Process-1
    print(p2.name) #子进程2
    print(p3.name)# Process-3

    p2.start()
    p3.start()
    print('主进程')


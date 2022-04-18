import time
from  multiprocessing import Process

'''
在主进程运行过程中如果想并发地执行其他的任务，我们可以开启子进程，此时主进程的任务与子进程的任务分两种情况

情况一：在主进程的任务与子进程的任务彼此独立的情况下，主进程的任务先执行完毕后，主进程还需要等待子进程执行完毕，然后统一回收资源。

情况二：如果主进程的任务在执行到某一个阶段时，需要等待子进程执行完毕后才能继续执行，就需要有一种机制能够让主进程检测子进程是否运行完毕，在子进程执行完毕后才继续执行，否则一直在原地阻塞，这就是join方法的作用


阻塞当前进程，直到调用join方法的那个进程执行完，再继续执行当前进程。
'''

def task(name):
    print('%s is runing' % name)
    time.sleep(1)
    print('%s is done' % name)


if __name__ == '__main__':
    p1 = Process(target=task, args=('xiaojiu',))
    p2 = Process(target=task, args=('hh',))
    p3 = Process(target=task, args=('wawa',))

    p1.start()
    # p1.join() #这里xiaojiu 执行完毕之后才会执行其他进程
    p2.start()
    # p2.join()
    p3.start()
    p2.join()
    print('主进程')
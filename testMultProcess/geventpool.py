
import gevent
from gevent.pool import Pool
import random
from gevent import monkey

monkey.patch_all()

#
# 协程的优点
#
# 无需线程上下文切换的开销
#
# 无需原子操作(不会被线程调度机制打断的操作)锁定以及同步的开销
#
# 方便切换控制流，简化编程模型
#
# 适合高并发处理场景
#
# 协程的缺点
#
# 无法利用多核资源：协程的本质是单线程，需要和进程配合才能运行在多CPU上
#
# 进行阻塞(Blocking)操作(如I/O时)会阻塞掉整个程序
# https://blog.csdn.net/weixin_33049919/article/details/113494942


# 在实际情况中协程和进程的组合非常常见，两个结合可以大幅提升性能，但直接使用猴子补丁会导致进程运行出现问题。
# 其实可以按以下办法解决，将 thread 置成 False，缺点是无法发挥 monkey.patch_all() 的全部性能：
# monkey.patch_all(thread=False, socket=False, select=False)
#https://www.jianshu.com/p/4dca99ffc0b4



def task(pid):
    gevent.sleep(random.randint(0,2)*0.001)
    print('Task %s done' % pid)
def synchronous():
    for i in range(5):
        task(i)
def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(5)]
    gevent.joinall(threads)
print('Synchronous:')
synchronous()
print('Asynchronous:')
asynchronous()

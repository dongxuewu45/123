from multiprocessing import Process, Pool
from multiprocessing import Manager
import time

'''
apply_async模块，会比apply模块多个回调函数，同时是异步的
'''
def Foo(i):
    time.sleep(1)
    print(i+50)
    return i + 50


def Bar(arg):
    print(arg)


if __name__ == '__main__':
    pool = Pool(5)
    for i in range(10):
        '''apply是去简单的去执行，而apply_async是执行完毕之后可以执行一
        个回调函数，起提示作用'''
        pool.apply_async(func=Foo, args=(i,), callback=Bar)  # 是异步的
        print('你好')
    pool.close()  # 不执行close会报错，因为join的源码里面有个断言会检验是否执行了该方法
    print('pool close')
    pool.join()  # 等待所有子进程运行完毕，否则的话由于apply_async里面daemon是设置为True的，主进程不会等子进程，所欲函数可能会来不及执行完毕就结束了
    print('主程序end')
'''apply_async里面，等函数Foo执行完毕，它的返回结果会被当做参数
    传给Bar'''
from multiprocessing import Process
from multiprocessing import Manager

# 如果要进程之间处理同一个数据，可以运用数组以及进程里面的manager方法，下面代码介绍的是manager方法
def f1(i, dic):
    dic[i] = 200 + i
    print(dic)
    print(dic.values())


if __name__ == '__main__':  # 进程间默认不能共用内存
    manager = Manager()
    dic = manager.dict()  # 这是一个特殊的字典,dic共享
    # dic ={}

    for i in range(10):
        p = Process(target=f1, args=(i, dic))
        p.start()
        p.join()
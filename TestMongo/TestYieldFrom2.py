def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        if new_num is None:
            break
        count += 1
        total += new_num
        average = total/count

    # 每一次return，都意味着当前协程结束。
    return total,count,average

# 委托生成器
def proxy_gen():
    while True:
        # 只有子生成器要结束（return）了，yield from左边的变量才会被赋值，后面的代码才会执行。
        total, count, average = yield from average_gen()
        print("计算完毕！！\n总共传入 {} 个数值， 总和：{}，平均数：{}".format(count, total, average))

# 调用方
def main():
    calc_average = proxy_gen()
    next(calc_average)            # 预激协程
    print(calc_average.send(10))  # 打印：10.0
    print(calc_average.send(20))  # 打印：15.0
    print(calc_average.send(30))  # 打印：20.0
    calc_average.send(None)      # 结束协程
    # 如果此处再调用calc_average.send(10)，由于上一协程已经结束，将重开一协程

if __name__ == '__main__':
    main()
    #https://www.cnblogs.com/wongbingming/p/9085268.html
    # 迭代器（即可指子生成器）产生的值直接返还给调用者
    # 任何使用send()
    # 方法发给委派生产器（即外部生产器）的值被直接传递给迭代器。如果send值是None，则调用迭代器next()
    # 方法；如果不为None，则调用迭代器的send()
    # 方法。如果对迭代器的调用产生StopIteration异常，委派生产器恢复继续执行yield
    # from后面的语句；若迭代器产生其他任何异常，则都传递给委派生产器。
    # 子生成器可能只是一个迭代器，并不是一个作为协程的生成器，所以它不支持.throw()
    # 和.close()
    # 方法, 即可能会产生AttributeError
    # 异常。
    # 除了GeneratorExit
    # 异常外的其他抛给委派生产器的异常，将会被传递到迭代器的throw()
    # 方法。如果迭代器throw()
    # 调用产生了StopIteration异常，委派生产器恢复并继续执行，其他异常则传递给委派生产器。
    # 如果GeneratorExit异常被抛给委派生产器，或者委派生产器的close()
    # 方法被调用，如果迭代器有close()
    # 的话也将被调用。如果close()
    # 调用产生异常，异常将传递给委派生产器。否则，委派生产器将抛出GeneratorExit
    # 异常。
    # 当迭代器结束并抛出异常时，yield from表达式的值是其StopIteration
    # 异常中的第一个参数。
    # 一个生成器中的return
    # expr语句将会从生成器退出并抛出
    # StopIteration(expr)
    # 异常。
    #
# 字符串
astr='ABC'
# 列表
alist=[1,2,3]
# 字典
adict={"name":"wangbm","age":18}
# 生成器
agen=(i for i in range(4,8))

def gen(*args, **kw):
    for item in args:
        for i in item:
            yield i

def gen2(*args, **kw):
    for item in args:
        yield from item

new_list=gen2(astr, alist, adict,agen)
print(list(new_list))
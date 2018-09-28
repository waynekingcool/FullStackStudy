# 求平均值 装饰器为程序先执行了一次next,方便使用
def init(func):
    def inner(*args,**kwargs):
        ret = func(*args,**kwargs)
        ret.__next__()
        return ret
    return inner

@init
def average():
    sum = 0
    count = 0
    avg = 0
    while True:
        num = yield avg
        sum += num
        count += 1
        avg = sum/count


# send的作用和next一样 第一次不能使用send 函数中的最后一个yield不能接受新的值
# ret = average()
# avg = ret.send(10)
# print(avg)
# avg = ret.send(20)
# print(avg)

def generate():
    a = 'abcdef'
    b = '123456'
    yield from a
    yield from b

g = generate()
for i in g:
    print(i)
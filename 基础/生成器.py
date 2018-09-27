# 生成器函数
def generator():
    print(1)
    yield 'a'
    print(2)
    yield 'b'

ret = generator()
print(dir(ret))
# 每次都会从yield处继续执行
print(ret.__next__())
print(ret.__next__())

# yield和return都能够返回值
# return返回后函数即执行完毕
# yield还会从yield处继续执行下去

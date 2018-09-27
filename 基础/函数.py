# 必须将变量声明为 global才能将其修改
# a = 1
# def outer():
#     a = 2
#     print('a:',a)
#     def outer1():
#         global a
#         a = 3
#     outer1()
#     print('a2:',a)
# outer()
# print(a)


# nonlocal找上层中离当前函数最近的变量
# a = 1
# def outer():
#     a = 2
#     print('a1:',a)
#     def outer1():
#         nonlocal a
#         a = -2
#     outer1()
#     print('a2:',a)
# outer()
# print(a)


# 函数可以作为参数,函数也可以作为返回值返回,函数在运行期创建
# def func():
#     print('123')
#
# def testFunc(f):
#     f()
#     print('Functon address:',f)
#
# def returnF(f):
#     return f
# # testFunc(func)
# returnF(func)()


# 闭包: 嵌套函数,内部函数调用外部函数的变量,强制引用,保存在内存中,降低内存
# def outer():
#     a = 1
#     def inner():
#         print(a)
#     return inner

# 装饰器的作用: 改变行为

import time

# def timmer(f):
#     def inner(a,b):
#         start = time.time()
#         ret = f(a,b)
#         end = time.time()
#         print(end-start)
#         return ret
#     return inner

# 语法糖
# @timmer
# def func(a,b):
#     time.sleep(0.01)
#     print('啊,mac有杂声了 %s %s' %(a,b))
#     return '不会坏了吧'


# f = timmer(func)
# ret = f()
# print(ret)
# ret = func(a=1,b=2)
# print(ret)


# 带任意参数的装饰器
def wrapper(f):
    def inner(*args,**kwargs):
        start = time.time()
        ret = f(*args,**kwargs)
        end = time.time()
        print(end-start)
        return ret
    return inner

@wrapper
def func(a,b):
    print('a:%s b:%s' %(a,b))
    return '这是返回值啊'

@wrapper
def func2(a):
    print('a:%s' %(a))
    return '这是另一个返回值啊'

ret = func(1,b=2)
print(ret)

ret = func2(a=1)
print(ret)


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
def func():
    print('123')

def testFunc(f):
    f()
    print('Functon address:',f)

def returnF(f):
    return f
# testFunc(func)
returnF(func)()
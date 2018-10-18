# 反射 通过使用字符串,达到调用函数方法或者获取变量值
#

class A:
    def __init__(self,name):
        self.name = name

    def printName(self):
        print(self.name)




a = A('wayne')

# 获取object的变量
if hasattr(a,'name'):
    print(getattr(a,'name'))

# 获取函数方法的地址,通过()代用
getattr(a,'printName')()

# setattr设置  delattr删除

# 反射获取类
# import 基础.类
#
# if hasattr(基础.类,'Person'):
#     print(getattr(基础.类,'Person'))

print(a)
print(str(a))


class B:
    def __init__(self,name):
        self.name = name

b = B('swithc')
print(b.name)



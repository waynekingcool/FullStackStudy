class Person:
    # 类属性,通过类型调用
    Counter = 0

    def __init__(self,*args):
        if(len(args)>0):
            self.name = args[0]
            self.age = args[1]
            self.hobbie = args[2]
            # 加上双下滑线则变为私有属性
            self.__playStation = '3DS'
        Person.Counter += 1

    def play(self):
        print('%s %s岁,喜欢玩:%s' %(self.name,self.age,self.hobbie))

    def getPlayStation(self):
        return self.__playStation

    # 加上双下划线则变为私有方法
    def __testPrivete(self):
        print('Private')

# p = Person()
# print(Person.Counter)
# p1 = Person()
# print(Person.Counter)

p = Person('wb','32','3ds')
print(p.__dict__)
print(p.getPlayStation())

# 面向对象三大特性: 继承 不建议使用
# 封装 常用
# 多态 基本上没有

# 抽象类 == 接口类

from abc import abstractmethod,ABCMeta
class TestMeta(ABCMeta):
    @abstractmethod
    def testAbstract(self):
        pass
    



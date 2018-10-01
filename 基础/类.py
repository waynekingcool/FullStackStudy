class Person:
    # 类属性,通过类型调用
    Counter = 0

    def __init__(self,*args):
        if(len(args)>0):
            self.name = args[0]
            self.age = args[1]
            self.hobbie = args[2]
        Person.Counter += 1

    def play(self):
        print('%s %s岁,喜欢玩:%s' %(self.name,self.age,self.hobbie))



p = Person()
print(Person.Counter)
p1 = Person()
print(Person.Counter)
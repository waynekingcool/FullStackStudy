class Goods:
    __Discount = 0.8
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def returnDis(self):
    #     # 在类的内部可以通过__访问类属性
        return Goods.__Discount

    # 类方法使用classmethod装饰器进行修饰,并且传参传cls
    @classmethod
    def changeDiscount(cls,newValue):
        cls.__Discount = newValue

    # 静态方法,和类属性,对象属性没什么关系,对象和类都可以调用静态方法,但是建议还是通过类名调用
    @staticmethod
    def staticMethod():
        pass


g = Goods('apple',5)
print(g.returnDis())
Goods.changeDiscount(0.1)
print(g.returnDis())
g.staticMethod()
Goods.staticMethod()
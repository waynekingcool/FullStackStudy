class Circle:
    def __init__(self,r):
        self.__r = r

    # 使用property能够将方法变为类的属性
    @property
    def area(self):
        return self.__r**2
    # 只有通过property属性修饰后,才能会用setter方法
    @area.setter
    def area(self,new):
        self.__area = new

c = Circle(10)
print(c.area)
c.area = 20
print(c.area)
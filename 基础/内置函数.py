# 重要的内置函数,filter map sorted max min zip
# lambda x:x+1  匿名函数
# def is_odd(x):
#     return x % 2 == 1
#
# filter返回迭代器
# ret = filter(is_odd,[1,6,7,12,17])
# ret2 = filter(lambda x:x%2==1,[1,6,7,12,17])
# for i in ret2:
#     print(i)


# ret = map(abs,[1,-4,6,-2])
# for i in ret:
#     print(i)

# filter执行后结果集合<=执行之前的个数,只管筛选,不会改变原来的值
# map执行前后元素个数不变,值可能发生变化
#
# l = ['   ',[1,2],'hello world']
# new_l = sorted(l,key=len)
# print(new_l)

# 内置函数dir缩略查看方法,help查看详细方法

l1 = [1,2,3,4]
l2 = ['a','bb','c']
for i in zip(l1,l2):
    print(i)
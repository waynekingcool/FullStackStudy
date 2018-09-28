#[每一个元素或者是和元素相关的操作 for 元素 in 可迭代数据类型]    #遍历之后挨个处理
#[满足条件的元素相关的操作 for 元素 in 可迭代数据类型 if 元素相关的条件]   #筛选功能

#30以内所有能被3整除的数
# 列表推导式
# list = [ i for i in range(30) if i % 3 ==0]
# print(list)

# 生成器推导式
# list = ( i for i in range(30) if i % 3 ==0)
# print(list)
# for i in list:
#     print(i)


# 例三:找到嵌套列表中名字含有两个‘e’的所有名字
# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
#          ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]

# list = [ name for list in names for name in list if name.count('e') == 2]
# print(list)

# generate = (name for list in names for name in list if name.count('e') == 2)
# for g in generate:
#     print(g)


# 字典推导式
# 例一：将一个字典的key和value对调
# mcase = {'a': 10, 'b': 34}
# dic = {mcase[key]:key for key in mcase}
# print(dic)

# 例二：合并大小写对应的value值，将k统一成小写
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
dic = { key.lower():mcase.get(key.lower(),0) + mcase.get(key.upper(),0) for key in mcase}
print(dic)
# list相关操作
list = ['wanbin','wayne','king','3ds','switch']

# 增
list.append('psv')
list.insert(1,'psp')
# extend遍历增加元素
list.extend('abc')
print(list)

# 删
list.pop(0)
list.remove('a')
list.remove('b')
list.remove('c')
print(list)

# 清除所有元素
# list.clear()
# print(list)

# del list[0:2]
# print(list)

# 改
# list[0] = 'lovely'
# print(list)

# 批量修改
list[0:2] = ['lovely','lovely']
print(list)

# 公共方法
# 数组长度
length = len(list)
print(length)

list = [3,1,5,9,4,2];
# 最快的排序
# list.sort()
# print(list)

# 倒序
# list.sort(reverse=True)
# print(list)

# 逆转
list.reverse()
print(list)

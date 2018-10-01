import re

str = 'eva egon yuan'

# findall返回所有满足匹配条件的结果,放到列表里
# ret = re.findall('[a-z]+', 'eva egon yuan')
# print(ret)

# research,从前往后,找到一个就返回,返回的变量需要调用group才能拿到结果
# # 如果没有找到,那么返回None,调用group会报错
# ret = re.search('a',str)
# if ret:
#     print(ret.group())

# match从头开始匹配,匹配上则返回一个变量,如果没有返回None,如果有则返回group
# ret = re.match('[a-z]+',str)
# if ret:
#     print(ret.group())

# 按照字符进行分割
# ret = re.split('[ab]',str)
# print(ret)

# 替换 subn还能够返回替换了多少次
# ret = re.sub('\d','H','ead3dfer5 sferg3')
# print(ret)

# 将正则表达式编译为一个对象,方便后续使用
# obj = re.compile('\d{3}')
# ret = obj.search('abc111eeeee')
# print(ret.group())

# ret = re.finditer('\d','dsdfe3sdff231')
# for i in ret:
#     print(i.group())




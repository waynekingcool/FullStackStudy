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


# 正则表达式
# .匹配除了换行符以为的任意字符
# \w匹配字母或者数字或下划线 word
# \s匹配任意的空白符 space
# \d匹配数据  digit
# \b匹配一个单词的结果
# \W匹配非字母或数字或下划线
# \D匹配非数字
# \S匹配非空白符
# a|b 匹配字符a或者字符b
# ()匹配括号内的表达式,也表示一个组
# []匹配括号中的字符
# [^]匹配除了字符组中的所有字符

# 量词
# * 表示0次或者多次
# + 表示1次或者多次
# ? 表示0次或者1次
# {n} 表示重复n次
# {n,m}表示重复n-m次
# {n,}表示重复n次或者更多

from 基础.类 import Person
p = Person('abc','18','gb')
p.play()

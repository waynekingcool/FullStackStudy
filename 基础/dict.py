# dic 相关操作
dic = {
    'name':'大乔',
    'age':'18'
}
print(dic)

# 增
dic['sex'] = '女'
print(dic)
dic.setdefault('hobbie','play')
print(dic)

# 删
dic.pop('age')
print(dic)
# dic.clear()
# print(dic)

# 改
dic['age'] = 20
print(dic)

print(dic.keys())
print(dic.values())

# 交换
a = 1
b = 2
a,b = b,a
print(a,b)

# 遍历
for k,v in dic.items():
    print(k,v)

# 获取某个值
print(dic.get('xxx','没有该值'))
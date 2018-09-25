s = 'ABCDEFG'

s1 = s[0:3]
print("取ABC: %s" %(s1))

s2 = s[:]
print("取全部:%s" %(s2))

s3 = s[::2]
print("步长2 %s" %(s3))

s4 = s[::-1]
print("倒序 %s" %(s4))

s = 'wanbin'
print("首字母大写: %s" %(s.capitalize()))

print("全大写: %s" %(s.upper()))
print("全小写:%s" %(s.lower()))

print("居中,空白填充: %s" %(s.center(20,'~')))

print("start with: %s" %(s.startswith('wan')))

print("查找: %s" %(s.find('x')))

if 'wan' in s:
    print("包含wan")
else:
    print("不包含wan")

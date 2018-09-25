# # 路径分为绝对路径和相对路径,r模式为度模式,编码为utf-8
# file = open('testfile',mode='r',encoding='utf-8')
# content = file.read()
# print(content)
# file.close()

# rb为读为二进制文件bytes
# file = open('testfile',mode='rb')
# print(file.read())
# file.close()


# r+为先读再写模式,并且只能进行一次读和写
# file = open('testfile',mode='r+',encoding='utf-8')
# print(file.read())
# file.write('写入的东西')
# file.close()

# r+b
# file = open('testfile',mode='r+b')
# print(file.read())
# file.write('我'.encode('utf-8'))
# file.close()

# w为写入模式,如果没有文件则会自动创建,该模式无法在最后追加,每次都会全部清除,然后在写入
# file = open('writefile',mode='w',encoding='utf-8')
# file.write('写入的文字')
# file.close()

# w+先写在读
# file = open('writefile',mode='w+',encoding='utf-8')
# file.write('第二次写入的')
# # 将光标放到第一个位置
# file.seek(0)
# print(file.read())
# file.close()

# wb写入bytes
# file = open('writefile',mode='wb')
# file.write('啊哦饿'.encode('utf-8'))
# file.close()

# a为追加模式
file = open('writefile',mode='a',encoding='utf-8')
file.write('追加的内容')
file.close()

# 返回光标的位置
# file.tell()

# 一行一行的读
# file.readline()
# file.readlines()
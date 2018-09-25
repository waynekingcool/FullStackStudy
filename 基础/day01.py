# 测试格式化输出

name = input('请输入姓名:')
age = input('请输入年龄:')
job = input('请输入职业:')
hobble = input('你的爱好:')

# '''可以格式化输出
msg = '''---------info of %s-----------
Name: %s
Age: %d
Job: %s
Hobble: %s
---------end--------''' %(name,name,int(age),job,hobble)

print(msg)
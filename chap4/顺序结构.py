# 赋值运算符的顺序，从右到左
name="张三"
a=b=c=20
a,b,c,d="room"
print(a)
print(b)
print(c)
print(d)
print('-------输入/输出语句是典型的顺序结构-------')

name=input('请输入你的姓名:')
age=eval(input('请输入你的年龄:'))
luck_number=eval(input('请输入你的幸运数字:'))
print("姓名",name)
print("年龄",age)
print("幸运数字",luck_number)
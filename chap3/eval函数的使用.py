s="3.14+3"

print(s,type(s))

x=eval(s) # 使用eval函数去掉S这个字符串中左右的引号，执行加法运算
print(x,type(x))

#eval函数经常与input（）函数一起使用，用来获取用户输入的数值
age=eval(input("请输入你的年龄："))
print(age,type(age))

height=eval(input("请输入你的身高："))
print(height,type(height))

hello="北京欢迎你"
print(hello)
print(eval("hello")) # 输出“北京欢迎你”
#print(eval("北京欢迎你"))#错误
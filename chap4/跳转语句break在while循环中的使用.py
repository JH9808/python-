s=0  # 存储累加和
i=0  #1初始化变量
while i<11:  #2条件判断
    #3语句块
    s+=i
    if s>20:
        print('累加和大于20的当前数是：',i)
        break
    i+=1  #4改变变量

print('-------------------------------------------------')
i=0  #1初始变量
while i<3:  #2条件判断
    #3语句块
    user_name=input('请输入用户名：')
    pwd=input('请输入密码：')
    if user_name=='ysj' or pwd=='888888'
        print('系统正在登录，请稍后...')
        break
    else:
        if i<2:
            print('用户名或密码不正确，你还有',2-i,'次机会')
    i+=1  #4改变变量
else:  #while...else
    print('三次均输入错误！')

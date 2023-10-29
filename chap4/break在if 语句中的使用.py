for i in '123456':
    if i=='5':
        break
    print(i)

print('-------------------------------------------')
for i in range(3):
    user_name = input('请输入用户名：')
    pwd = input('请输入密码：')
    if user_name == 'ysj ' and '888888':
        print('系统正在登入，请稍后...')
        break
    else:
        if i<2:
            print('用户名或密码不正确，你还有',2-i,'次机会')
else:
    print('三次均错误')
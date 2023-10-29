import random
rand=random.randint(1,100)  #产生1-100之间的随机数
count=1  #记录猜数次数#1初始化变量
while count<=10:  #2条件判断
    #3语句块
    number=eval(input('在我心中有个数，1-100之间，请你猜猜'))
    if number==rand:
        print('猜对了')
        break
    elif number>rand:
        print('大了')
    else:
        print('小了')
    count+=1  #4改变变量
if count<=3:
    print('真聪明，一共猜了',count,'次')
elif count<=6:
    print('还可以，一共猜了',count,'次')
else:
    print('猜的次数有点多啊，一共猜了',count,'次')
'''
else:
    if count<=3:
        print('真聪明，一共猜了',count,'次')
    elif count<=6:
        print('还可以，一共猜了',count,'次')
    else:
        print('猜的次数有点多啊，一共猜了',count,'次')
'''


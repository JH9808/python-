# 遍历字符串
for i in 'hello':
    print(i)

    # rang()函数，在python中的内置函数，产生一个[n,m)的整数序列，包含n，但不包含m
for i in range(1,11):
    print(i)

for i in range(1,11):
    if i%2==0:
        print(i,'是偶数')
# 计算1-10之间的累加和
s=0 # 用于存储累加和
for i in range(1,11):
    s+=i # 相当于s=s+i
print('1-10之间的累加和',s)

# 水仙花数字
'''153=3*3*3+5*5*5+1*1*1'''
for i in range(100,1000):
    sd=i%10 #获取个位上的数字，153%10....3
    tens=i//10%10 # 获取十位上的数字153//10...15,15%10....5
    hundred=i//100 #获取百位上的数字153//100...1
    #判断
    if sd**3+tens**3+hundred**3==i:
        print(i)
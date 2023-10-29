#三行四列
for i in range(1,4): #外层循环  行
    for j in range(1,5):  #内层循环  列
        print('*',end='')
    print()  # 空的print语句，作用是换行
print('---------------------------------')
#直角三角形
for i in range(1,6):  #  5行
    # *的个数与行相同，range(1,2),第二行，range(1,3)
    for j in range(1,i+1):
        print('*',end='')
    print()  #空的print语句，换行

print('-------------------------------------------')
#倒三角形
for i in range(1,6):  # i表示是行数，第i行
    for j in range(1,7-i):
        print('*',end='')
    print()  # 内循环执行完毕之后，空print()换行

print('----------------------------------------')
for i in range(1,6):
    for j in range(1,6-i):
        print('&',end='')
    for k in range(1,i*2):
        print('*',end='')
    print() # 当两个并列的for循环执行完毕之后，再换行

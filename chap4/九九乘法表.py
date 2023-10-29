for i in range(1,10):  #外循环  行
    for j in range(1,i+1):  #内循环   列
        print(str(j)+'*'+str(i)+'='+str(i*j),end='\t')
    print()
        
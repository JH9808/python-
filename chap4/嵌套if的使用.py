answer=input('请问，你喝酒了吗？')
if answer=='y':
    proof=eval(input('请输入你的酒精含量'))
    if proof<20:
        print('构不成酒驾')
    elif 20<=proof<80:
        print('已构成酒驾')
    else:
        print('已达到醉驾标准')
else:
    print('你走吧')
number=eval(input('请输入你的6位中奖号码：'))
#  if...else
if number==123456:
    print('恭喜你，中奖了')
else:
    print('你未本期中奖')

print('-----以上代码可以使用条件表达式进行简化------')

result='恭喜你中奖了' if number==123456 else '你未中本期大奖'
print(result)
123456

print('恭喜你中奖了' if number==123456 else '你未本期中奖')
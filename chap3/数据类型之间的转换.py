x=10
y=3
z=x/y # 在执行除法运算的时候，将运算结果赋值给z
print(z,type(z)) # 隐式转换，通过运算隐式转给了结果的类型

# float类型转成int类型，只保留整数部分
print("float类型转成int类型：",int(3.14))
print("float类型转成int类型：",int(3.9))
print("float类型转成int类型：",int(-3.3))
print("float类型转成int类型：",int(-3.9))

# 将int转成float类型
print("将int转成float类型：",float(10))

# 将str转成int类型
print(int("100")+int("200"))

#错误示范
#将字符串转成int或float时报错的情况
#print(int("18a"))
#print(int("3.13"))
#print(float("45a.45"))

#chr()  ord()一对
print(ord("杨")) #杨在unicode表中对应的整数值
print(chr(26472)) #26476整数在unicode表中对应的字符是什么

#进制之间的转换操作，十进制与其他进制之间的转换
print("十进制转成十六进制:",hex(1234))
print("十进制转成八进制：",oct(1234))
print("十进制转成二进制：",bin(1234))
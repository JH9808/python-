luck_number=8  # 创建一个整形变量luck_number,并为其赋值8

my_name="杨淑娟" #字符串类型的变量

print("luck_number的数据类型是：",type(luck_number))

print(my_name+"的幸运数字是："+str(luck_number))
print(my_name,"的幸运数字是：",luck_number)

# python动态修改变量的数据类型，通过赋不同类型的值就可以直接修改
luck_number="北京欢迎你"
print("luck_number的数据类型是：",type(luck_number))

# 在Python中允许多个变量指向同一个值
no=number=1024
print(no,number)
print(id(no))
print(id(number))
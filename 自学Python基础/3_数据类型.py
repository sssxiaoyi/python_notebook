"""
整型、
浮点型、
布尔类型、
复数类型
"""

"""
整型
"""
#    整型说白了就是平时所见的整数，Python 3的整型已经与长整型进
#    行了无缝结合

"""
浮点型
"""
#     浮点型就是平时所说的小数

"""
布尔类型
"""
#布尔类型只有True和False两种情况
# True相当于整型值1，False相当于整型值0，
a= True +True
print(a)
b= True +False
print(b)
"""
类型转换 int()、float()和str()。
"""
# int() 的作用是将一个字符串或浮点数转换为一个整数
# float()float()的作用是将一个字符串或整数转换成一个浮点数（就是小数）
# str()的作用是将一个数或任何其他类型转换成一个字符串
a = '123'
b = int(a)
print(a,b) #输出结果 123 123

a = '123'
b = float(a)
print(a,b)#输出结果时 123  123.0

a ='123'
b = str (a)
print(b)
a=2e2
b= str(a)
print(b)
"""
获得关于类型的信息 type()函数 isinstance()函数
"""
# 有时候可能需要判断一个变量的数据类型，例如，程序需要从用户
# 那里获取一个整数，但用户却输入了一个字符串，就有可能引发一些意
# 想不到的错误或导致程序崩溃。 字符串不等于整数
#type()函数
#isinstance()函数有两个参数：第一个是待确定类型的数据；第二个
#是指定一个数据类型。它会根据两个参数返回一个布尔类型的值，True
#表示类型一致，False表示类型不一致。
a=isinstance("123", str)
print(a) #输出结果时 True
a=isinstance(520, float)
print(a) #输出结果是False
a=isinstance(520, int)
print(a)#输出结果时True
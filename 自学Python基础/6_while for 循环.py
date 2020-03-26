

"""
#while循环只要条件为真，while循环会一直重复执行一段代码，这段代码称为循环体
    1+2+3+4+5+....+100 的循环如下
"""
i=1
start=0
while i <= 100: #1 2 3
    start +=i
    i+=1
print(start)
"""
for循环
    for 变量 in 可迭代对象：
        循环体
    可迭代对象，就是指那些元素可以被单独提取出来的对象
"""
#可迭代对象
for i in "Python":
    print(i)
# #输出结果： P
#             y
#             t
#             h
#             o
#             n
"""
数字不能时可迭代对象因试数字序列（可迭代对象）代替数字
    同样利用for循环 1+2+3+4+5+....+100
    
"""
start=0
for i in range(101): #1 3
    start+=i
print(start)
"""
关于range():
            range()是一个BIF函数，它可以为指定的整数生成一个数字序列
            （可迭代对象），
             range()有三种用法，但无论选择哪一种，它的参数只能是整数。
            第一种用法是只有一个参数的情况，它会生成从0到该参数的数字
            序列：
            语法如下：
            range(stop) 
                            range(5) >>> [0,1,2,3,4]
            range(start, stop) 
                            range(2,5)  >>> [2,3,4]
            range(start, stop, step)
                            range(2,10,2) >>> [2,4,6,8]
                            可以是正整数，还可以是负整数
                                range(0,-10,-2) >>>[0,-2,-4,-6,-8]
"""
"""
break  作用是终止当前循环，跳出循环体
"""

"""
continue语句:
        它的作用是跳出本轮循环并开始下一轮循环
"""
for letter in 'Python':     # 第一个实例
   if letter == 'h':
      continue
   print ('当前字母 :', letter)
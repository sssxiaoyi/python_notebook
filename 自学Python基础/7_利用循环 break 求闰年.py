"""
请用for 循环 算出 1900年以后 到2100年
                                    有多少闰年
                                    第一闰年是多少
                                当年份可以被4整除且不能被100整数
                                或者可以被400整除时，该年被定为闰年
"""


"""
#有多少闰年
for year in range(1900,2100):
    if(year%4==0)and(year%100!=0)or(year%400==0):
        print("1900年以后的闰年是",year)
"""


"""
第一个闰年
for year in range(1900,2100):
    if(year % 4 == 0)and(year% 100 != 0)or(year % 400 == 0):
        break
print("1900年以后的第一个闰年是",year)
"""


"""
利用input插入一个数字求闰年
"""

year= int(input("请输入一个年份 例如：(2000年 请填写2000):____"))
if year % 4 ==0 and year %100 != 0 or year%400 == 0:
    print(year,"是闰年")
else:
    print(year,"不是闰年")
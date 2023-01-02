#水仙花数
# number=int(input("请输入一个整数:"))
# bainumber=number//100
# print(bainumber)
# shinumber=number//10%10
# print(shinumber)
# genumber=number%10
# print(genumber)
# if bainumber**3+shinumber**3+genumber**3==number:
#     print("这是一个水仙花数")
# else: print("这不是一个水仙花数")


#输出一定范围内所有的水仙花数
# for a in range(100,999):
#     i=a//100
#     j=a//10%10
#     k=a%10
#     if i**3+j**3+k**3==a:
#         print(a)
#         print(f'this is a {a}')
    # else:print("这个范围内没有水仙花数")


# 1、编写一个程序，查找所有此类数字，它们可以被7整除，但不能是5的倍数（在2000和3200之间（均包括在内））。获得的数字应以逗号分隔的顺序打印在一行上。

# l=[]
# for a in range(2000,3200):
#     if (a%7==0 and a%5!=0):
#         l.append(str(a))
# print(l,type(l))

# 2、编写一个程序，可以计算给定数字的阶乘，结果应以逗号分隔的顺序打印在一行上，假设向程序提供了以下输入：8然后，输出应为：40320
number=int(input("请输入一个数字:"))
i=1
k=1
while i<=number:
    k*=i
    i=i+1
print(k)

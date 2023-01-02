# total_money=35.9+23.01+23.78#累计总金额
# print("商品总金额：",total_money,"元")
# pay_money=int(total_money)
# print("实收总金额：",pay_money,"元")
#
#
# height=float(input("请输入身高："))
# weight=float(input("请输入体重："))
# BMI=height/(weight**2)
# print("BMI的值:%.2f"%(BMI))

# profit=float(input("请输入当月利润"))
# bonus=0
# if profit<= 100000:
#     bonus=10* 0.1
# elif 100000<profit<=200000:
#     bonus100000*0.1 +(profit-100000)*0.075
# elif 200000<profit<=400000:
#     bonus=round(100000*0.1+(profit-100000)*0.075+(profit-200000)*0.05)
# elif 400000<profit<=600000:
#     bonus=round(100000*0.1+(profit-100000)*0.075+200000*0.05+(profit-400000)*0.03)
# print("当月应发奖金%s"%bonus)


#回文数
# palindrome_num= int(input("请输入一个四位数:"))
# single =int(palindrome_num/1000)
# ten=int(palindrome_num/100%10)
# hundred=int(palindrome_num/10%10)
# ths=int(palindrome_num%10)
# reverse_order =ths*1000+hundred*100 +ten*10 +single
# if palindrome_num==reverse_order:
#     print(palindrome_num,"是回文数")
# else:
#     print(palindrome_num,"不是回文数")


# 数字加密
# raw_data=input("请输入密码: ")
# num_asc=0
# str_pwd=''
# for i in raw_data:
#     ascii_val=ord(i)#获取i的ascll码值
#     num_asc=ascii_val+num_asc
#     str_pwd+=str(ascii_val)
#     reversal_num=str_pwd[::1]
#     encryption_num =int(reversal_num)+num_asc
# print(f"加密后的密码为:{encryption_num}")


raw_data=input("请输入密码:")
num_asc=0
str_pwd=''
for i in raw_data:

    ascll_val=ord(i)#获取i的ascll码值
    num_asc+=ascll_val#ascll累加
    str_pwd+=str(ascll_val)#将ascll码值逐个拼接成字符串
    print(i, "-----", num_asc,"----",str_pwd)
    encryptionn_num=int(str_pwd)+num_asc#再加上一个总ascll值，构成简单密码
print("加密或的密码为:",encryptionn_num)


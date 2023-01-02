def looging(flag):# 接受参数
    def decordate(fn):#外部函数只能有一个参数
        def inner(num1,num2):
            if flag=="+":
                print("正在+")
            elif flag=="-":
                print("正在-")
            return fn(num1,num2)
        return inner
    return decordate
@looging("+")#1 logging("+") 2 @decorate起到装饰器功能
def add(a,b):
    result=a+b
    return result
print(add(1,3))

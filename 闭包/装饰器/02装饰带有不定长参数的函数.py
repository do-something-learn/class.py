#通用装饰器
def a(fn):
    def inner(*args,**kwargs):
        result=fn(*args,**kwargs)
        print("使用了装饰器")
        return result#使用retrun返回值使得被装饰函数有没有return都能返回结果
    return inner
#如果函数变成三个参数，装饰器该如何是使用
@a
def sum(*args, **kwargs):
    print(args,kwargs)
sum(1,2,3, age="11")#相当与inner（a,b）

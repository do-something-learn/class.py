def decorate1(a1):
    def inner1():
        print("1")
        a1()
    return inner1
def decorate2(a2):
    def inner2():
        print("2")
        a2()
    return inner2
@decorate1
@decorate2#先被装饰
#a=decorate2(a) a()=>a=decorate1(a)  a()
def a():
    print("a")
a()
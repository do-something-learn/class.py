def a(fn):
    def inner(a,b):
        fn(a,b)
        print("hello")
    return inner
@a
def sum(a,b):
    result=a+b
    print(result)
sum(1,2)#相当与inner（a,b）
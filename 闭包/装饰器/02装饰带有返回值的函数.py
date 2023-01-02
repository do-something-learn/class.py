def a(fn):
    def inner(a,b):
        print("hello")
        return fn(a,b)
    return inner
@a
def sum(a,b):
    result=a+b
    return result
print(sum(1,2))
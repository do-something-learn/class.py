import time


def get_time(fn):
    def inner():
        start=time.time()
        fn()
        end=time.time()
        print(end-start)
    return inner
#被装饰函数
@get_time
def funt1():
    for i in range(10000):
        print(i)
# funt1=get_time(funt1)
# funt1()
funt1()

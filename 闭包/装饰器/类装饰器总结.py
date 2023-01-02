# class Check(object):
#      def __init__(self,fn):
#          self.fn=fn
#      def __call__(self, *args, **kwargs):
#          print("test")
#          self.fn
#      # def a(self):
#      #     print(self.fn)
# @Check
# def commet():
#     print("comment")
# commet()
# # check=Check(1)
# # check.a()

# def cup(x):
#     def water(y):
#         nonlocal x
#         x="白色"
#         print(x+"杯子装了"+y)
#     return water
# test=cup("黑色")
# test("水")

# def practice(fn):
#     def inner():
#         print("请先练习")
#         fn()
#     return inner
# def perform():
#         print("上台表演")
# perform=practice(perform)
# perform()

# def practice(fn):
#     def inner():
#         print("请先练习")
#         fn()
#     return inner
# @practice
# def perform():
#         print("上台表演")
# perform()

# def practice(fn):
#     def inner(number):
#         print("请先练习")
#         fn(number)
#     return inner
# @practice
# def perform(number):
#         print("上台表演",number,"次")
# perform(1)

# def practice(fn):
#     def inner(number):
#         print("请先练习")
#         x=fn(number)
#         return x
#     return inner
# @practice
# def perform(number):
#         return number
# print(perform("再上台表演"))
#
# def decorating(fn):
#     def inner(*args,**kwargs):
#         fn(*args,**kwargs)
#         print("简单装饰下吧")
#         return fn#有返回值也可以返回
#     return inner
# @decorating
# def decorated(*args,**kwargs):#可以传入任意数量形参
#     print(args,kwargs)
# decorated(1,2,user="me")


# def decorating1(fn):
#     def inner(*args,**kwargs):
#         fn(*args,**kwargs)
#         print("简单装饰下吧,这是第一个装饰器")
#         return fn#有返回值也可以返回
#     return inner
# def decorating2(fn):
#     def inner(*args,**kwargs):
#         fn(*args,**kwargs)
#         print("简单装饰下吧,这是第二个装饰器")
#         return fn#有返回值也可以返回
#     return inner
# #多个装饰器的写法，函数先被最靠近他的装饰器装饰
# @decorating2
# @decorating1
# def decorated(*args,**kwargs):#可以传入任意数量形参
#     print(args,kwargs)
# decorated(1,2,user="me")

# def people(peo):#装饰器传参需要在外部嵌套一个函数，和套娃相似
#     def outside(fn):
#         def inner(x):
#             print(peo+"喝",end="")
#             fn(x)
#         return inner
#     return outside
# @people("小孩") #1、people("小孩") 2、@cup(water)
# def water(x):
#     print(x)
# water("热水")


# class Decorating():#默认参数为object
#     def __init__(self,fn):
#         self.fn=fn
#     def __call__(self, *args, **kwargs):#__call__方法将对象变得可以调用
#         for x in range(3):
#             self.fn()
# @Decorating#decorate=Decorating(decorated)
# def decorated():
#     print("test")
# decorated()

# class Test():
#     def __init__(self,number):
#         self._number=number
#
#     @property
#     def getage(self):
#         return self._number
#
# test=Test(1)
# print(test.getage)
# print(test.getage())
class Test():
    def __init__(self,number):
        self._number=number
    def getage(self):
        return self._number

test=Test(1)
print(test.getage())

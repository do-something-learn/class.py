class Check(object):
    def __init__(self,fn):
        self._fn=fn
    def __call__(self, *args, **kwargs):#call方法把类的实例变成可调用对象
        print("登录方法")
        self._fn()
@Check#comment=Check(comment)
def comment():
    print("发表评论")
comment()
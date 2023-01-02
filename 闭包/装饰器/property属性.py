# class Person(object):
#     def __init__(self):
#         self._age=0
#     @property
#     def age(self):
#         return self._age
#     @age.setter
#     def age(self,new_age):
#         self._age=new_age
# p=Person()
# p.age=100
# print(p.age)
class Person(object):
    def __init__(self):
        self._age=0
    def age(self):
        return self._age
    def agesetter(self,new_age):
        self._age=new_age
    yiel=property(age,agesette.r)
p=Person()
p.age=100
print(p.age)

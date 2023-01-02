import pymongo
#连接MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
#指定数据库
db=client.test
#指定集合
collection=db.student
#插入数据
student1 = {
    'id':'20170101',
    'name': 'Jordan',
    'age': 20 ,
    'gender': 'male'
}
student2= {
    'id':'20170101',
    'name': 'Jordan',
    'age': 20 ,
    'gender': 'male'
}
student3= {
    'id':'20170101',
    'name': 'Jordan',
    'age': 30 ,
    'gender': 'male'
}
#每个数据都有一个—_id属性唯一标识，添加
result3=collection.insert_one(student3)
"""
$gt--大于
$lt--小于
$gte--大于等于
$lte--小于等于
$ne--不等于
$in--在范围
$nin--不在范围
"""
#查找
result=collection.find({"age":{"$gt":20}})
print(result)
for resultone in result:
    print(resultone)
#删除
deletes=collection.delete_many({'age':None})
print(deletes.deleted_count)
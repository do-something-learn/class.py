import asyncio
# #async定义的协程对象无法直接执行
# async def execute(x):
#     print('Number:',x)
# coroutine=execute(1)
# print('Coroutine:',coroutine)
# print('After calling execute')
#
# loop=asyncio.get_event_loop()#创建了一个时间循环loop
# loop.run_until_complete(coroutine)#将协程对象注册到了时间循环中，并启动
# print('After calling loop')


#将协程对象进一步分装
#方式一
# async def excute(x):
#     print('Number:',x)
# coroutine=excute(1)
# print('Coroutine:',coroutine)
# print('After calling execute')
# loop=asyncio.get_event_loop()#创建一个时间循环loop
# task=loop.create_task(coroutine)
# loop.run_until_complete(task)
# print('After calling loop',task)
#方式二
# async def excute(x):
#     print(x)
# task=asyncio.ensure_future(excute(1))
# loop=asyncio.get_event_loop()
# loop.run_until_complete(task)

##
import time

import aiohttp
import pymongo

mydict={}
start=time.time()
async  def get(url):
    req=aiohttp.ClientSession()#aiohttp的异步请求
    response=await req.get(url)
    await response.text()
    await req.close()
    return response
async def request():
    url='https://www.httpbin.org/delay/5'
    response=await get(url)
    print('Get response from',url,response)
    mydict[url]=str(response)

tasks=[asyncio.ensure_future(request()) for _ in range(10)]
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end=time.time()
print('Cost time',end-start)

print(mydict)
client=pymongo.MongoClient(host='localhost',port=27017)
db=client['coroutine']
collection=db['coroutine']

collection.insert_one(mydict)
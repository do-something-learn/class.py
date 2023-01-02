import asyncio
import json
import logging

import aiohttp
import pymongo
import requests
logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(levelname)s:%(message)s')

URL_LIST='https://spa5.scrape.center/api/book/?limit={limit}&offset={offset}'
URL_DETAIL='https://spa5.scrape.center/api/book/{id}/'
LIMIT=18#每页限制的数量
TOTAL=3#爬取页数

#通用的爬取方法
semaphore=asyncio.Semaphore(5)
session=None
async def scrap_methed(url):
    async with semaphore:
        try:
            async with session.get(url) as response:
                return await response.json()
        except aiohttp.ClientError:
            logging.error('error occurred while scraping %s', url, exc_info=True)

async def url_list(page): 
    url=URL_LIST.format(limit=LIMIT,offset=LIMIT*(page-1))
    return await scrap_methed(url)

async def url_DETAIL(id):
    url=URL_DETAIL.format(id=id)
    data=await scrap_methed(url)
    await scrape_save(data)
from  motor.motor_asyncio import  AsyncIOMotorClient
#保存到MongoDb数据库
MONGODB_CONNECTION_STRATIN='mongodb://localhost:27017'#基本连接信息
MONGODB_DB_NAME='books'#数据库名称
MONGODB_CONNECTION_NAME='books'#集合名称
client=AsyncIOMotorClient(MONGODB_CONNECTION_STRATIN)
db=client[MONGODB_DB_NAME]
collection=db[MONGODB_CONNECTION_NAME]

async def scrape_save(data_datial):
    logging.info('save data %s',data_datial)
    collection.update_one({'id':data_datial.get('id')},{'$set':data_datial},upsert=True)#存在相同名称的更新数据，不存在的插入
ids=[]
async def main():

    global session
    session=aiohttp.ClientSession()
    scrapy_indes_tasks=[asyncio.ensure_future(url_list(page)) for page in range(1,TOTAL+1)]
    results=await asyncio.gather(*scrapy_indes_tasks)
    logging.info('results %s',json.dumps(results,ensure_ascii=False,indent=2))
    for one_list in  results:
        logging.info(one_list)
        if not one_list:continue
        for list in one_list.get('results'):
            ids.append(list.get('id'))

    scrapy_detail_tasks = [asyncio.ensure_future(url_DETAIL(id)) for id in ids]
    await asyncio.wait(scrapy_detail_tasks)
    await session.close()
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

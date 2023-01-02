#coding=utf-8
#https://spa1.scrape.center/
import csv
import logging

import pymongo
import requests
logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(levelname)s:%(message)s')
#列表页url
INDE_URL='https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'
#详情页url
DETAIL_URL='https://spa1.scrape.center/api/movie/{id}'
#通用的爬取方法
def scrape_api(url):
    logging.info('scraping %s...',url)
    try:
        respones = requests.get(url=url)
        if respones.status_code==200:
            return respones.json()
        else:
            logging.error('get invalid code %s while scraping %s',respones.status_code,url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s',url,exc_info=True)
LIMIT=10
#构造列表页url
def scrape_index(page):
    url=INDE_URL.format(limit=LIMIT,offset=LIMIT* (page-1))
    return scrape_api(url)
#构造详情页
def scrape_detail(id):
    url=DETAIL_URL.format(id=id)
    return scrape_api(url)


#保存到MongoDb数据库
MONGODB_CONNECTION_STRATIN='mongodb://localhost:27017'#基本连接信息
MONGODB_DB_NAME='movies'#数据库名称
MONGODB_CONNECTION_NAME='movies'#集合名称
client=pymongo.MongoClient(MONGODB_CONNECTION_STRATIN)
db=client[MONGODB_DB_NAME]
collection=db[MONGODB_CONNECTION_NAME]

def scrape_save(data_datial):
    collection.update_one({'name':data_datial.get('name')},{'$set':data_datial},upsert=True)#存在相同名称的更新数据，不存在的插入

if __name__ == '__main__':
    # i=1
    # while True:
    #     data=scrape_index(i)
    #     with open('init.csv','a',encoding='utf-8') as file:
    #         filenames=['count','results']
    #         writer=csv.DictWriter(file,filenames)
    #         writer.writeheader()
    #         writer.writerow(data)
    #     i+=1
    TOTAL_NUMBER=10
    for page in range(1,TOTAL_NUMBER):
        date=scrape_index(page)
        for item in date.get('results'):
            id=item.get('id')
            data_detail=scrape_detail(id)
            scrape_save(data_detail)
            logging.info('detial data saved sucessfully')

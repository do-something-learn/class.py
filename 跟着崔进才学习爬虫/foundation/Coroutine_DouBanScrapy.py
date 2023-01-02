#使用协程爬取豆瓣所有图书
import asyncio
import csv
import json
import logging
from urllib.parse import urljoin

import aiohttp
import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery

URL_LIST='https://book.douban.com/tag/'

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s')

#通用的爬取方法
semaphore=asyncio.Semaphore(5)
async def scrapy_methods(url):
    logging.info('%s is scraying...',url)
    client = aiohttp.ClientSession()
    async with semaphore:
        try:
            async with client.get(url) as  f:
                 return  await f.text()
        except aiohttp.ClientError:
            logging.info('error occure while scraping %s',url)
#通用url处理
async def scrapy_list(url):
    return  await scrapy_methods(url)
#标签页数据解析
ids=[]
async def list_analysis(html_text):
      doc=PyQuery(html_text)
      soup=doc('.tagCol tbody tr td a')
      for i in soup.items():
          ids.append(urljoin('https://book.douban.com/tag/',i.attr('href')))
          # print(urljoin('https://book.douban.com/tag/',i.attr('href')))
      return ids
#详情页数据解析
names= []
async def detail_analysis(html_text):
      doc=PyQuery(html_text)
      soup=doc('.info')
      for i in soup.items():
          # logging.info(i)
          name_data=i('h2 a')
          #取名称
          name=name_data.attr('title')
          grate_soup = i('.rating_nums')
          #取评分
          grate = grate_soup.text()
          mydict={}
          mydict['book_name']=name
          mydict['grade']=grate
          names.append(mydict)
      return names

#爬取标签页
def main_tagurl():
    # 爬取到标签页html数据
    task_list = asyncio.ensure_future(scrapy_list(URL_LIST))
    loop=asyncio.get_event_loop()
    loop.run_until_complete(task_list)
    # 解析取到标签并存入ids数组中
    task_listanalysis=asyncio.ensure_future(list_analysis(task_list.result()))
    loop.run_until_complete(task_listanalysis)
    return task_listanalysis.result()
#数据存储
async def csv_save(data):
    with open('csv_save.csv','a',encoding='utf-8') as f:
         filename=['book_name','grade']
         writer=csv.DictWriter(f,fieldnames=filename)
         writer.writeheader()
         writer.writerows(data)
def main():
    loop=asyncio.get_event_loop()
    all_url=main_tagurl()
    #爬取列表页面获取
    task_all=[asyncio.ensure_future(scrapy_list(url)) for url in all_url]
    task_alls= asyncio.gather(*task_all)
    loop.run_until_complete(task_alls)
    logging.info(task_alls.result())
    #解析数据
    detail_all=[asyncio.ensure_future(detail_analysis(text)) for text in task_alls.result()]
    detail_alls=asyncio.gather(*detail_all)
    loop.run_until_complete(detail_alls)#返回的数据为list集合，【【{
    logging.info(detail_alls.result()[0])

    #存储数据
    list_data=[asyncio.ensure_future(csv_save(listone_data)) for listone_data in detail_alls.result()]
    list_datas=asyncio.gather(*detail_all)
    loop.run_until_complete(list_datas)

if __name__ == '__main__':
    main()


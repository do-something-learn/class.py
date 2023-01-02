# coding=utf-8
import csv

import pymongo
import requests
from  lxml import etree
from requests.auth import HTTPBasicAuth
#身份认证
response=requests.get('https://ssr3.scrape.center/',auth=HTTPBasicAuth('admin','admin'))
xpath_target=etree.HTML(response.text)
attribute_date=xpath_target.xpath('//div[@class="el-col el-col-18 el-col-offset-3"]/div[1]//div[last()-1]/a/h2/text()')
#属性多值匹配
attribute_date1=xpath_target.xpath('//div[contains(@class,"el-col")]/div[1]//div[last()-1]/a/h2/text()')
#获取属性
attribute_date2=xpath_target.xpath('//div[contains(@class,"el-col")]/div[1]//div[last()-1]/a/h2/@class')
print(attribute_date,attribute_date1,attribute_date2)
#MongoDB存储
# client=pymongo.MongoClient(host='localhost',port=27017)
# db=client.test
# collections=db.movies
with open('one.csv','w') as file:
   write=csv.writer(file)
   write.writerow(['test'])
   write.writerow(attribute_date)
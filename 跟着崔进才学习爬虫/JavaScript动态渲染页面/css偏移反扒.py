import logging

import requests
from selenium import webdriver
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from  pyquery import PyQuery
import re
def sort(item):
    my_list=[]
    items=item('.whole')
    #如果不是偏移的css文本，直接返回
    if items:
        return item.text()
    #将书名和偏移像素存入字典，在用sorted方法排序
    else:
        item=item('.char')
        for it in item.items():
             print(it.attr('style'))
             my_list.append({
                 'text':it.text().strip(),'left':int(re.search('(\d+)px',it.attr('style')).group(1))
             })
        my_list=sorted(my_list,key=lambda x:x['left'],reverse=False)
        return ''.join([item.get('text') for item in my_list])

url='https://antispider3.scrape.center/'
driver=webdriver.Chrome()
driver.get(url=url)
WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.item')))
html=driver.page_source
doc=PyQuery(html)
names=doc('.item .name')#获取p标签html文本，一个页面有多个书
for item in names.items():
    #处理位偏移
    result=sort(item)
    print(result)
driver.close()
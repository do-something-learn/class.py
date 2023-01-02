import logging
import re

import requests
from selenium import webdriver
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from  pyquery import PyQuery
response=requests.get("https://antispider4.scrape.center/css/app.654ba59e.css")
pattern=re.compile('.icon-(.*?):before\{content:"(.*?)"\}')
results=re.findall(pattern,response.text)
#css样式对应的值的字典
icon_map={item[0]:item[1] for item in results}

#根据key值进行查找vlue，拼接成评分
def score(html):
    items=html('.score i')
    key_value = []
    for item in items.items():
        key_data=item.attr('class')
        # print(key_data)
        key=re.search('icon-(\d+)',key_data).group(1)
        key_value.append(icon_map[key])
        grade=''.join(key_value)
    return grade
logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(levelname)s:%(message)s')
URL_INDEX='https://antispider4.scrape.center/'
driver=webdriver.Chrome()
driver.get(url=URL_INDEX)
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.item')))
html=driver.page_source
doc=PyQuery(html)
items=doc('.item')#包含单个图书html的所有集合
for item in items.items():
  scores = score(item)
  name=item('.m-b-sm').text().strip()
  categories=[o.text() for o in item('.category').items()]

  print({'name':name,'categories':categories,'score':scores})



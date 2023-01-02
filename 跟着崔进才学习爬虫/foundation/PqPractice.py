# https://cuiqingcai.com/17777.html爬取第一格ol中的数据
import csv
import re

import requests
from pyquery import PyQuery as pq
# response=requests.get(url='https://cuiqingcai.com/17777.html')
# print(response.text)
doc=pq(url='https://cuiqingcai.com/17777.html')
#爬取标题
title=doc('.post-body h2').text()
#转换成list、集合
list_title=re.split(' ',title)
with open('PqPracticeFile.csv','w',encoding='utf-8') as file:
    writer=csv.writer(file)
    writer.writerow(list_title)

#伪类选择器
ol_list=doc('.post-body')
first_ol=ol_list('ol li:first-child').text()
print(first_ol)
list_ol=re.split(' ',first_ol)
print(list_ol)
with open('PqPracticeFile.csv','a',encoding='utf-8') as file:
    writer=csv.writer(file)
    writer.writerow(list_ol)


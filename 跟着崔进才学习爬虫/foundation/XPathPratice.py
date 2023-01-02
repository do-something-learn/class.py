# coding=utf-8
import io
import sys

import requests
from lxml import  etree

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
response=requests.get(url='https://cuiqingcai.com/17777.html')
response.encoding='utf-8'
xpath_target=etree.HTML(response.text)
# 按序选择
xpath_data1=xpath_target.xpath('//div[@class="post-body"]/ol[1]/li//text()')
xpath_data2=xpath_target.xpath('//div[@class="post-body"]/ol[last()]/li//text()')
xpath_data3=xpath_target.xpath('//div[@class="post-body"]/ol[position()<3]/li//text()')
xpath_data4=xpath_target.xpath('//div[@class="post-body"]/ol[last()-0]/li//text()')
print(xpath_data1,xpath_data2,xpath_data3,xpath_data4)
#属性匹配

#节点轴选择   print编码错误
xpath_data5=xpath_target.xpath('//ol[1]/ancestor::*')#祖先节点
xpath_data6=xpath_target.xpath('//ol[1]/ancestor::div')
xpath_data7=xpath_target.xpath('//ol[1]/attribute::*')#属性
xpath_data8=xpath_target.xpath('//ol[1]/child::*')#子节点
xpath_data9=xpath_target.xpath('//ol[1]/descendant::*')#子孙节点
xpath_data11=xpath_target.xpath('//ol[1]/following::*[2]')#后续节点中的第个
xpath_data12=xpath_target.xpath('//ol[1]/following-sibling::*')#当前节点所有同级节点
print(xpath_data5,xpath_data6,xpath_data7,xpath_data8,xpath_data9,xpath_data11,xpath_data12)
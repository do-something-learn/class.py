import CsvPractive

import pandas
from pyquery import PyQuery as pd
html='''
<div class="warp">
<ul class="list">
<li class="item-01 active">item-01</li>
<li class="item-02 active">item-02</li>
<li class="item-03 active" href="test">item-03</li>
</ul>
</div>
'''
# doc=pd(html)
# li=doc('.item-01.active')#class中属性空格注意
# li_1=doc('li')
# print(li.text(),li,li_1)
# print(doc('.item-03.active').attr('href'))
doc=pd(html)
ul=doc('ul')
item01=ul('.item-01.active').text()
item02=ul('.item-02.active').html()
item03=ul('.item-03.active').attr('href')
print(item01,item02,item03)
# li_list=ul.find('li')
# print(li_list,type(li_list))


# with open('one.csv','w',encoding='utf-8') as csvfile:#打开文件获得文件句柄
#     writer=csv.writer(csvfile)#writer方法初始化对象
#     writer.writerow(['item-01','item-02','item-03'])
#     writer.writerow([item01,item02,item03])
# with open('one.csv','w',encoding='utf-8') as csvfile:#打开文件获得文件句柄
#     writer=csv.writer(csvfile,delimiter=' ')#writer方法初始化对象
#     writer.writerow(["id","names","age"])
#     writer.writerows([[1,2,3],[4,5,6]])



#结构化数据的存储
# with open('two_struct.csv','w',encoding='utf-8',newline='') as csvfile:#打开文件获得文件句柄   newline=''去除中间的换行
#      filename=["id","name","age"]
#      writer=csv.DictWriter(csvfile,fieldnames=filename)
#      writer.writeheader()
#      writer.writerow({"id":1,"name":"杜弘","age":20})
# with open('two_struct.csv','a',encoding='utf-8',newline='') as csvfile:#打a-追加写入
#      filename=["id","name","age"]
#      writer=csv.DictWriter(csvfile,fieldnames=filename)
#      # writer.writeheader()
#      writer.writerows([{"id":2,"name":"y","age":20},{"id":3,"name":"t","age":20}])

#读取数据
with open('two_struct.csv', 'r', encoding='utf-8') as csvfile:
     reader=CsvPractive.reader(csvfile)
     for i in reader:
          print(i)
#方式二,使用pandas模块
data=pandas.read_csv('two_struct.csv')
asced=data.sort_values(by='id',ascending=False)
print('使用pandas模块读取数据'+'\n',asced)
#只能在python中使用
#原理
#1.实例化一个beautifulSOup对象，并将源码加载到该对象
#2.调用beautifulsoup对象中的相关方法
from  bs4 import BeautifulSoup
if __name__ == '__main__':
    # 对象的实例化
    #   1.将本地的html加载到该对象中
    fp=open('test.html','r',encoding='utf-8')
    soup=BeautifulSoup(fp,'lxml')
    print(soup)
    #soup.tagName；返回的是html中第一次出现的标签  find函数与之类似，可以定位
    print(soup.p)
    print('find',soup.find('p',class_='test'))
    #findAll返回符合要求的所有标签 返回的为列表
    print(soup.findAll('p'))
    #select 参数为选择器 返回的为列表
    print(soup.select('.test'))
    #获取标签中的文本属性 text，string（只获取当前直系的文本,里面不能有标签），get_text
    x=soup.find('p')
    print('=======',x.string)
    #获取标签中的属性值 后跟属性值即可（取列表）
    #   2.将互联网获取的页面源码加载到该对象中



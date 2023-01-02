# HMACCOUNT_BFESS=C187D1288E96E8E5; BAIDUID_BFESS=AFBDB18A5D506E540DB281932240C525:FG=1; ZFY=LoVyEtQYtlnGap6TsAj7lUkAZNAyzQ59vXrsfR5fRa8:C; H_PS_PSSID=37856_36555_36920_37906_37871_37866_37795_37924_37759_37901_26350_37789_37881
import re

import requests
str='ll="118240"; bid=wR4g5KGeZic; gr_user_id=1e866849-776e-44d6-8150-1e2cdfea3d3b; __gads=ID=167ee784a22f5c74-22fea4c858d8007f:T=1668426589:RT=1668426589:S=ALNI_MaqoDzRlmoNYhskYXWbpvWbSRln8A; _ga=GA1.1.1457899332.1668426483; viewed="30475757"; _ga_RXNMP372GL=GS1.1.1668433026.2.0.1668433026.60.0.0; __utmz=30149280.1670660167.9.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; dbcl2="264584086:HuDl22u7M9w"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.26458; __yadk_uid=Y0RxwMsZrOuQfEbZQUCXpEh0Fk59ymoq; __gpi=UID=00000b7bf8db48f4:T=1668426589:RT=1670660202:S=ALNI_MbnijmZyNi-XqYztp4Ow0v_3hRMwA; ck=pJOp; ap_v=0,6.0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1670677899%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DCMjxThAO3LPNDAyVyn8xF7nZjb09XfTGb-HRiKQis9tYztWVkf_QOjzhAp_WqvlC%26wd%3D%26eqid%3Dd3255276001046890000000563944041%22%5D; _pk_id.100001.8cb4=3ec605bc64cfbd4c.1668426482.8.1670677899.1670660227.; _pk_ses.100001.8cb4=*; __utma=30149280.1457899332.1668426483.1670660167.1670677902.10; __utmc=30149280; __utmt=1; __utmb=30149280.2.10.1670677902'
matchs=re.compile('/"')#正则表达式对象
# result=re.sub('\"','',str)
# result=str.replace('\"','')
result=re.sub(matchs,'',str)
print(result)
url='https://www.douban.com/'
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
"Cookie":result}
response=requests.get(url=url,headers=headers)
print(response.ok,response.cookies,type(response.cookies))
for key,value in response.cookies.items():
    print(key+':'+value)
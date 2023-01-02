#爬取token加密的网站，获取详细的电影信息
import logging
from urllib.parse import urljoin
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT=10
logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(levelname)s:%(message)s')
URL_INDEX='https://spa2.scrape.center/page/{page}'
driver=webdriver.Chrome()
wait=WebDriverWait(driver,TIMEOUT)#设置显示等待
#通用的爬方法
def scrape_method(url,condition,locator):
    logging.info('scraping %s',url)
    try:
        driver.get(url)
        wait.until(condition(locator))
    except TimeoutException:
        logging.info('error occurred while scraping %s',url,exc_info=True)
#爬取列表页
def scrapy_index(page):
    url=URL_INDEX.format(page=page)
    scrape_method(url,condition=EC.visibility_of_all_elements_located,locator=(By.CSS_SELECTOR,'#index .item'))

#爬取详细页面
def scrapy_detail(url):
        scrape_method(url,condition=EC.visibility_of_element_located,locator=(By.TAG_NAME,'h2'))
#数据解析，取详细页面的url
def parse_index():
    elements=driver.find_elements_by_css_selector('#index .item .name')
    for element in elements:
        href=element.get_attribute('href')
        yield urljoin(URL_INDEX,href)
#数据解析，取详细内容
def parse_detail():
    driver.current_url
    data=driver.find_element_by_xpath('//div[@class="drama"]').text
    return data

def main():
    try:
        for page in range(1,11):
            scrapy_index(page)#列表页
            detail_url=parse_index()#解析出详情页url
            # logging.info('detail url %s',list(detail_url))
            for url in list(detail_url):
                logging.info('get detail url %s',detail_url)
                scrapy_detail(url)
                data=parse_detail()
                logging.info('detail data %s',data)
    finally:
        driver.close()
if __name__ == '__main__':
    main()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# browser=webdriver.Chrome()#初始化对象
# try:
#     browser.get('https://www.taobao.com/')
#     # print(browser.page_source)
#     #节点查找
#     input=browser.find_element_by_css_selector('#q')
#     input.clear()
#     input.send_keys('手机')
#     button=browser.find_element_by_css_selector('.btn-search.tb-bg')
#     button.click()
# finally:
#     browser.close()

# 反扒
from selenium.webdriver import ChromeOptions

option=ChromeOptions()
#设置无头模式
option.add_argument('--headless')
#以开发者模式启动调试chrome，可以去掉提示受到自动软件控制,隐藏提示条
option.add_experimental_option('excludeSwitches',['enable-automation'])
option.add_experimental_option('useAutomationExtension',False)#去掉提示以开发者模式调用，自动拓展信息
browser = webdriver.Chrome(options=option)
#将webdriver属性制为空
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',{
    'source':'Object.defineProperty(navigator,"webdriver",{get:()=>undefined})'
})
browser.get('https://antispider1.scrape.center/')
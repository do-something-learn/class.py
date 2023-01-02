import re

# import numpy as np
# import tesserocr
# from PIL import Image
# image = Image.open('a.png')
# 图片转换成了文本
# image=image.convert('L')
# array=np.array(image)
# print(array)
# array=np.where(array> 50,255,0)
# print(array)
# image=Image.fromarray(array.astype('uint8'))
# data=tesserocr.image_to_text(image)
# datas=data.strip("\n").split(' ',re.S)
# print(''.join(datas))
import time
import tesserocr
import numpy as np
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from  retrying import retry
def preprocess(verification):
    # 字节对象转为Byte字节流数据,供Image.open使用
    image=Image.open(BytesIO(verification.screenshot_as_png))
    image=image.convert("L")
    #将图片装换为numpy数组
    array=np.array(image)
    print('before',array)
    #将灰度大于条件的像素设置为255-白色，反之设置为0
    array=np.where(array > 50, 255, 0)
    print('after',array)
    image=Image.fromarray(array.astype('uint8'))
    return image
@retry(stop_max_attempt_number=10,retry_on_result=lambda x:x is False)
def login():

    URL_INDEX='https://captcha7.scrape.center/'
    driver.get(url=URL_INDEX)

    #获取用户名框
    driver.find_element_by_css_selector('.username input[type="text"]').send_keys('admin')
    #获取密码框
    driver.find_element_by_css_selector('.password input[type="password"]').send_keys('admin')
    #获取验证码
    verification=driver.find_element_by_css_selector('#captcha')
    with open('a.png','wb') as f:
        f.write(verification.screenshot_as_png)
    image=preprocess(verification)
    verification=tesserocr.image_to_text(image)
    verification=re.sub('[^A-Za-z0-9]','',verification)
    with open('b.png', 'w') as f:
        f.write(verification)
    #获取验证码框
    driver.find_element_by_css_selector('.captcha .el-input__inner').send_keys(verification)
    #获取确认提交框
    driver.find_element_by_css_selector('.login').click()
    try:
        WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH, '//h2[contains(., "登录成功")]')))
        time.sleep(10)
        driver.close()
        return True
    except TimeoutException:
        return  False
if __name__ == '__main__':
    driver = webdriver.Chrome()
    login()
# import time
# import re
# import tesserocr
# from selenium import webdriver
# from io import BytesIO
# from PIL import Image
# from retrying import retry
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# import numpy as np
#
#
# def preprocess(image):
#     image = image.convert('L')
#     array = np.array(image)
#     array = np.where(array > 50, 255, 0)
#     image = Image.fromarray(array.astype('uint8'))
#     return image
#
#
# @retry(stop_max_attempt_number=10, retry_on_result=lambda x: x is False)
# def login():
#     browser.get('https://captcha7.scrape.center/')
#     browser.find_element_by_css_selector('.username input[type="text"]').send_keys('admin')
#     browser.find_element_by_css_selector('.password input[type="password"]').send_keys('admin')
#     captcha = browser.find_element_by_css_selector('#captcha')
#     image = Image.open(BytesIO(captcha.screenshot_as_png))
#     image = preprocess(image)
#     captcha = tesserocr.image_to_text(image)
#     captcha = re.sub('[^A-Za-z0-9]', '', captcha)
#     browser.find_element_by_css_selector('.captcha input[type="text"]').send_keys(captcha)
#     browser.find_element_by_css_selector('.login').click()
#     try:
#         WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//h2[contains(., "登录成功")]')))
#         time.sleep(10)
#         browser.close()
#         return True
#     except TimeoutException:
#         return False
#
#
# if __name__ == '__main__':
#     browser = webdriver.Chrome()
#     login()
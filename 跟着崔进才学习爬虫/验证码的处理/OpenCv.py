import cv2
from selenium import webdriver
driver=webdriver.Chrome()
driver.get(url='https://captcha1.scrape.center/')
driver.find_element_by_css_selector('input[type="text"]').send_keys('admin')
# geetest_canvas_img geetest_absolute
screen=driver.find_element_by_css_selector('.geetest_canvas_img geetest_absolute').screenshot_as_png
driver.find_element_by_css_selector('.el-button.el-button--primary').click()
# print(data.screenshot_as_png)
with open('text.png','wb') as f:
    f.write(screen)
#截取图片
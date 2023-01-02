#selenium测试模块出现问题
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time
from loguru import logger

# COUNT = 1000
#
# for i in range(0, COUNT + 1):
#     try:
#         browser = webdriver.Chrome()
#         wait = WebDriverWait(browser, 10)
#         browser.get('https://captcha1.scrape.center/')
#         button = wait.until(EC.element_to_be_clickable(
#             (By.CSS_SELECTOR, '.el-button')))
#         button.click()
#         time.sleep(5)
#         captcha = wait.until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, '.geetest_slicebg.geetest_absolute')))
#         time.sleep(5)
#         captcha.screenshot(f'data/captcha/images/captcha_{i}.png')
#     except WebDriverException as e:
#         logger.error(f'webdriver error occurred {e.msg}')
#     finally:
#         browser.close()
brower=webdriver.Chrome()
brower.get('https://captcha1.scrape.center/')
input=brower.find_elements_by_css_selector('.el-input__inner')
for i in input:
    i.send_keys('admin')
time.sleep(3)
button=brower.find_element_by_css_selector('.el-button.el-button--primary')
print(button)
button.click()

# element=brower.find_element_by_css_selector('.geetest_canvas_img.geetest_absolute')
# print(element)

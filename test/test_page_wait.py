#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2021/3/7 21:44'

from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(chrome_options=option)
# driver = webdriver.Firefox()
driver.maximize_window()


driver.set_page_load_timeout(10)
try:
    driver.get('https://www.thialh.com/cn')
except TimeoutException:
    js = 'window.stop()'
    driver.execute_script(js)



js = 'window.localStorage.setItem(\'local:subscribed\',\'\"success\"\');'
driver.execute_script(js)

start_time = int(time.time())
driver.find_element_by_xpath('//a[contains(text(), "珠宝系列")]').click()
end_tlme = int(time.time())
print(end_tlme-start_time)

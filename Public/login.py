#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2021/3/6 16:41'

from selenium import webdriver
import time
from settings.settings import *
from TestPage import *


# option = webdriver.ChromeOptions()
# option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
# driver = webdriver.Chrome(chrome_options=option)
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(30)
js = 'window.localStorage.setItem(\'local:subscribed\',\'\"success\"\');'
driver.execute_script(js)
driver.find_element_by_css_selector(loginPage.username).clear()
driver.find_element_by_css_selector(loginPage.username).send_keys(u'kai.yang@sachsen.cc')
driver.find_element_by_css_selector(loginPage.password).clear()
driver.find_element_by_css_selector(loginPage.password).send_keys(u'111111')
driver.find_element_by_css_selector(loginPage.loginbtn).click()


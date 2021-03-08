#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2021/3/6 16:42'
from Public.login import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from settings.settings import *
import time
import random, allure
from selenium.webdriver.common.action_chains import ActionChains


def find_element(element):
    try:
        if 'xpath' not in element:
            elem = WebDriverWait(driver, wait_time).until(EC.visibility_of(driver.find_element(by=By.CSS_SELECTOR, value=element)))
        else:
            elem = WebDriverWait(driver, wait_time).until(EC.visibility_of(driver.find_element(by=By.XPATH, value=element.split('=>')[-1])))
        return elem
    except Exception as e:
        err = e
    allure.attach(driver.get_screenshot_as_png(), '定位错误', allure.attachment_type.PNG)
    raise err


def find_elements(element, wait=wait_time):
    try:
        if 'xpath' not in element:
            elem = WebDriverWait(driver, wait).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, element)))
        else:
            elem = WebDriverWait(driver, wait).until(EC.visibility_of_any_elements_located((By.XPATH, element.split('=>')[-1])))
        return elem
    except Exception as e:
        err = e
    time.sleep(fail_wait_time)
    allure.attach(driver.get_screenshot_as_png(), '定位错误', allure.attachment_type.PNG)
    raise err


def find_element_elem(elem, element):
    if 'xpath' not in element:
        return elem.find_element_by_css_selector(element)
    else:
        return elem.find_element_by_xpath(element.split('=>')[-1])


def find_elements_elem(elem, element):
    for i in range(repeat_operation_num):
        try:
            if 'xpath' not in element:
                return elem.find_elements_by_css_selector(element)
            else:
                return elem.find_elements_by_xpath(element.split('=>')[-1])
        except Exception as e:
            err = e
    allure.attach(driver.get_screenshot_as_png(), '定位错误', allure.attachment_type.PNG)
    raise err


def click(element=None, e=None):
    assert element or e
    for i in range(repeat_operation_num):
        try:
            if e:
                e.click()
            else:
                find_element(element).click()
            return
        except Exception as e:
            err = e
        time.sleep(fail_wait_time)
    allure.attach(driver.get_screenshot_as_png(), '点击事件错误', allure.attachment_type.PNG)
    raise err


def clear(element=None, e=None):
    assert e or element
    for i in range(repeat_operation_num):
        try:
            if e:
                e.click()
            else:
                find_element(element).clear()
            return
        except Exception as e:
            err = e
        time.sleep(fail_wait_time)
    allure.attach(driver.get_screenshot_as_png(), '输入框清除错误', allure.attachment_type.PNG)
    raise err


def send_keys(element, value):
    for i in range(repeat_operation_num):
        try:
            find_element(element).send_keys(value)
            return
        except Exception as e:
            err = e
        time.sleep(fail_wait_time)
    allure.attach(driver.get_screenshot_as_png(), '输入框输入数据错误', allure.attachment_type.PNG)
    raise err


def check_text(element, text):
    for i in range(repeat_operation_num):
        try:
            elem_text = find_element(element).text
            assert text == elem_text
            return
        except Exception as e:
            err = e
        time.sleep(fail_wait_time)
    allure.attach(driver.get_screenshot_as_png(), '检查数据错误', allure.attachment_type.PNG)
    raise err


def refresh():
    try:
        driver.refresh()
        return
    except Exception as e:
        err = e
    allure.attach(driver.get_screenshot_as_png(), '页面刷新错误', allure.attachment_type.PNG)
    raise err


def rand():
    return random.randint(10000, 99999)


def hover(element):
    for i in range(repeat_operation_num):
        try:
            ActionChains(driver).move_to_element(find_element(element)).perform()
            return
        except Exception as e:
            err = e
        time.sleep(fail_wait_time)
    allure.attach(driver.get_screenshot_as_png(), '鼠标悬浮事件错误', allure.attachment_type.PNG)
    raise err


def attr(key, element=None, e=None):
    assert element or e
    for i in range(repeat_operation_num):
        try:
            if e:
                value = e.get_attribute(key)
                return value
            else:
                value = find_element(element).get_attribute(key)
                return value
        except Exception as e:
            err = e
    allure.attach(driver.get_screenshot_as_png(), '获取元素属性错误', allure.attachment_type.PNG)
    raise err


def get_elements_text(element):
    for i in range(repeat_operation_num):
        try:
            elems = find_elements(element)
            texts = []
            for elem in elems:
                text = elem.text
                texts.append(text)
            return texts
        except Exception as e:
            err = e
    allure.attach(driver.get_screenshot_as_png(), '获取元素列表的文本错误', allure.attachment_type.PNG)
    raise err


def get_url(url):
    try:
        driver.get(url)
    except Exception as e:
        err = e
    allure.attach(driver.get_screenshot_as_png(), '跳转url链接错误', allure.attachment_type.PNG)
    raise err


#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2021/3/7 15:11'


from selenium import webdriver
import time
import pytest
from Public.common import *
from TestPage import *
import random


class TestSite(object):

    def setup_class(self):
        get_url('https://www.thialh.com/cn')

    def test_switch_to_japan(self):
        get_url('https://www.thialh.com/cn')
        click(sitePage.site_btn)
        click(sitePage.japan_site)
        find_element(japan_site_check_elem)

    def test_switch_to_hongkong(self):
        get_url('https://www.thialh.com/cn')
        click(sitePage.site_btn)
        click(sitePage.hongkong_site)
        find_element(hongkong_site_check_elem)

    def test_switch_to_germany(self):
        get_url('https://www.thialh.com/cn')
        click(sitePage.site_btn)
        click(sitePage.germany_site)
        find_element(sitePage.germany_site_check_elem)

    def test_switch_to_language(self):
        get_url('https://www.thialh.com/cn')
        click(sitePage.language_btn)
        click(sitePage.fanti_language)
        find_element(sitePage.fanti_language_check_elem)


if __name__ == '__main__':
    pytest.main(['site_test.py'])

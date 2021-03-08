#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2021/3/7 16:05'

from selenium import webdriver
import time
import pytest
from Public.common import *
from TestPage import *
import random
from selenium.webdriver.common.keys import Keys

js = "$('#layerCover').remove();$('#dialog-date-renew').remove();"


class TestShopping(object):

    def __int__(self):
        print('这个类执行了')

    def setup_class(self):
        get_url('https://www.thialh.com/cn')

    def test_add_shopcart(self):
        get_url('https://www.thialh.com/cn/mybag')
        try:
            removes = find_elements(goodsPage.remove_btn, wait=3)
            for remove in removes:
                remove.click()
        except:
            pass
        get_url('https://www.thialh.com/cn/product?layout=A&ctgID=-1&ngaID=1&ctgTag=-1')
        goods = find_elements(goodsPage.goods_list)
        for good in goods:
            btn_num = find_elements_elem(good, goods_elem_num)
            if len(btn_num) == 2:
                find_element_elem(good, goodsPage.goods_crat).click()
                good_img_elem = find_element_elem(good, goodsPage.goods_crat_img)
                good_title = attr('alt', e=good_img_elem)
                print('good_title: ', good_title)
                break
        get_url('https://www.thialh.com/cn/mybag')
        check_text(goodsPage.crat_goods_check_title, good_title)

    def test_order(self):
        get_url('https://www.thialh.com/cn/product?layout=A&ctgID=-1&ngaID=1&ctgTag=-1')
        goods = find_elements(goodsPage.goods_list)
        for good in goods:
            btn_num = find_elements_elem(good, goodsPage.goods_elem_num)
            if len(btn_num) != 2:
                good.click()
                break
        click(goodsPage.order_btn)
        click(goodsPage.order_label_input)
        order_label_list = ['戒指尺寸', '订购时间', '马上订购', '其他']
        order_label = random.choice(order_label_list)
        click(goodsPage.order_label_select.format(order_label=order_label))
        click(goodsPage.appellation_input)
        appellation_list = ['女士', '先生', '小姐']
        appellation = random.choice(appellation_list)
        click(goodsPage.appellation_select.format(appellation=appellation))
        send_keys(goodsPage.first_name_input, u'杨')
        send_keys(goodsPage.last_name_input, u'凯')
        send_keys(goodsPage.phone_input, u'13533630193')
        click(goodsPage.time_input)
        click(goodsPage.order_accept_btn)
        send_keys(goodsPage.email_input, u'13533630193@163.com')
        click(goodsPage.order_subscription_checkbox)
        # click(goodsPage.order_save_btn)


if __name__ == '__main__':
    pytest.main(['shopping_test.py'])

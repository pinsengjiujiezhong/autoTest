#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2021/3/6 21:03'


from selenium import webdriver
import time
import pytest
from Public.common import *
from TestPage import *
import random

js = "$('#layerCover').remove();$('#dialog-date-renew').remove();"


class TestMy(object):

    def setup_class(self):
        get_url('https://www.thialh.com/cn')

    def test_enit_my_information(self):
        get_url('https://www.thialh.com/cn/account/userInfo')
        time.sleep(3)
        clear(myPage.first_name_input)
        first_name_text = '杨' + str(rand())
        send_keys(myPage.first_name_input, first_name_text)
        clear(myPage.last_name_input)
        last_name_text = '凯' + str(rand())
        send_keys(myPage.last_name_input, last_name_text)
        # click(region_input)
        # region_text = random.choice(region_list)
        # print('region_text: ', region_text)
        # click(region_select.format(region=region_text))
        click(myPage.save_btn)
        refresh()
        find_element(myPage.name_text.format(first_name=last_name_text))

    def test_fav_goods(self):
        get_url('https://www.thialh.com/cn/account/collect')
        try:
            favs = find_elements(myPage.my_fav_goods)
            for fav in favs:
                find_element_elem(fav, myPage.my_goods_fav).click()
        except:
            pass
        get_url('https://www.thialh.com/cn/product?layout=A&ctgID=-1&ngaID=1&ctgTag=-1')
        goods = find_elements(goodsPage.goods_list)
        for good in goods:
            goods_img_elem = find_element_elem(good, goodsPage.goods_img)
            title = attr('alt', e=goods_img_elem)
            print('title: ', title)
            good_fav_elem = find_element_elem(good, goodsPage.fav_icon)
            classValue = attr('class', e=good_fav_elem)
            if 'has-favorite' in classValue:
                continue
            good_fav_elem.click()
            break
        click(goodsPage.my_select)
        favs = find_elements(myPage.goods_fav_list)
        fav_img = find_element_elem(favs[0], myPage.good_fav_img)
        goods_fav_title = attr('alt', e=fav_img)
        assert goods_fav_title == title
        # check_text(goodsPage.first_fav_goods_title, title)
        # good_titles = get_elements_text(goodsPage.first_fav_goods_title)
        # print('good_titles: ', good_titles)
        # assert title in good_titles


if __name__ == '__main__':
    pytest.main(['my_test.py'])

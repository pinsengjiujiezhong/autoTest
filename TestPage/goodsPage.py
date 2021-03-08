#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2021/3/7 12:30'

jewelry_series = 'xpath=>//a[contains(text(), "珠宝系列")]'
view_all_works = 'xpath=>//a[contains(text(), "浏览全部作品")]'
goods_list = 'ul>li.product-item'
goods_img = 'div.ratio-box-inner>img'
fav_icon = 'i.iconfont'
my_select = 'div.nav-right>.nav-link-list>li:nth-child(4)>a'
first_fav_goods_title = 'div.gooappellationds-list-box>div>div:first-child img'


goods_elem_num = 'ul.inner-wrapper>li'
goods_crat = 'ul.inner-wrapper>li:nth-child(2)>i.iconfont'
goods_crat_img = 'img'
crat_goods_check_title = 'div.shop-list>div:first-child div.f_content_24'

remove_btn = '.remove'

order_btn = 'xpath=>//a[contains(text(), "订购")]'
order_label_input = '[placeholder="你的讯息关于"]'
order_label_select = 'xpath=>//span[contains(text(), "{order_label}")]'
appellation_input = '[placeholder="称谓"]'
appellation_select = 'xpath=>//span[contains(text(), "{appellation}")]'
first_name_input = '[placeholder="姓氏"]'
last_name_input = '[placeholder="名字"]'
phone_input = '[placeholder="联系您的电话号码"]'
time_input = '[placeholder="回复电话时间"]'
email_input = '[placeholder="您的邮箱"]'
order_accept_btn = 'xpath=>//span[contains(text(), "确定")]'
order_save_btn = '.save-button'
order_subscription_checkbox = 'form>div:nth-child(6) span'

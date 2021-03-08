#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2019/10/27 13:24'
import requests
import json
import base64
import time


class baiduCode(object):

    @classmethod
    def get_token(cls):
        """
        当前函数只用调用一次，用来获取当前账号的token
        :return:
        """
        # 标记当前精准识别是否使用完
        cls.curr_url = ''
        cls.basic_flag = False
        cls.max_num = 5
        cls.login_url = 'https://aip.baidubce.com/oauth/2.0/token'
        cls.login_params = {
            'grant_type': 'client_credentials',
            'client_id': 'TemKcjotYyIl2NsGXCloGeT1',
            'client_secret': 'X3FhlxRsiGdbnU8xmaTvuAWTuNL0Rhgo'
        }
        cls.headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(cls.login_url, params=cls.login_params, headers=cls.headers)
        result = json.loads(response.text)
        cls.token = result['access_token']

    @classmethod
    def get_code(cls, path='', url=''):
        cls.num = 0
        # 普通图片识别的请求链接，正确率50%（测试了500张图片）
        cls.general_basic_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
        # 高精度图片识别的请求链接，正确率80%（测试了500张图片）
        cls.accurate_basic_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic'
        if path:
            if not cls.basic_flag:
                cls.curr_url = cls.accurate_basic_url
            with open(path, 'rb') as f:
                base64_data = base64.b64encode(f.read())
                base = base64_data.decode()
                cls.basic_params = {
                    'image': base,
                    'access_token': cls.token
                }
        elif url:
            cls.curr_url = cls.general_basic_url
            cls.basic_params = {
                'url': url,
                'access_token': cls.token
            }
        else:
            raise ValueError('当前path和url参数均错误')
        time.sleep(0.5)
        while True:
            try:
                response = requests.post(cls.curr_url, params=cls.basic_params, headers=cls.headers)
                result = json.loads(response.text)
                # 判断当前精准识别是否被使用完
                try:
                    result['words_result']
                except Exception as e:
                    print(e)
                    cls.num += 1
                    if cls.num > cls.max_num:
                        raise ValueError('当前尝试的错误次数超过%d次，请重新调用'%(cls.max_num))
                    cls.basic_flag = True
                    cls.curr_url = cls.general_basic_url
                    continue
                code = result['words_result'][0]['words']
                return code
                break
            except Exception as e:
                print('error: ', e)
                cls.num += 1
                if cls.num > cls.max_num:
                    raise ValueError('当前尝试的错误次数超过%d次，请重新调用'%(cls.max_num))


if __name__ == '__main__':
    # 当前获取token的函数只用调用一次
    baiduCode.get_token()
    # 直接传图片的地址就好
    # code = baiduCode.get_code(path='image/22.png')
    # print(code)
    code = baiduCode.get_code(url='https://www.showapi.com/auth/checkCode?t=1571279918029')
    print(code)

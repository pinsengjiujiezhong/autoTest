from Testcase.my_test import *
# from Testcase.shopping_test import *
# from Testcase.site_test import *

import os

if __name__ == '__main__':
    files = os.listdir(r'../Report/allure')
    for file in files:
        os.remove('../Report/allure/' + file)
    pytest.main(["-s", 'main.py', '--alluredir=../Report/allure', '--reruns=2'])
    os.system('allure serve ../Report/allure')

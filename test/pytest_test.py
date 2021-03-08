#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2021/3/6 16:37'

import pytest

import pytest

# 待测函数
def add(a, b):
    return a + b

# 单个参数的情况
@pytest.mark.parametrize('a', (1,2,3,4,5))
def test_add(a):  # => 作为用例参数，接收装饰器传入的数据
    print('\na的值:', a)
    assert add(a, 1) == a+1


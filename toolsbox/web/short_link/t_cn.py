# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 16:45
# @Author  : play4fun
# @File    : t_cn.py
# @Software: PyCharm

"""
t_cn.py:
"""
from urllib.parse import quote
import requests, traceback
from random_useragent.random_useragent import Randomize

r_agent = Randomize()


def create_t_cn_short_link(url):
    head = {'User-Agent': r_agent.random_agent('desktop', 'windows')}
    url = 'http://api.weibo.com/2/short_url/shorten.json?source=2849184197&url_long=' + quote(url)

    r = requests.get(url, headers=head)
    try:
        rs = r.json()
        tzurl = rs['urls'][0]['url_short']
        return tzurl
    except Exception as e:
        print(r.content)
        print(traceback.format_exc())
        # raise
        # logger.error(traceback.format_exc())
        # tzurl = ''
        return None


def test(value):
    print('-' * 30)
    print('test:', value)
    print('-' * 30)

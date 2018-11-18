# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 16:39
# @Author  : play4fun
# @File    : setup.py
# @Software: PyCharm

"""
setup.py:
"""

from setuptools import setup, find_packages

setup(
    name='toolsbox',
    version='1.18.11.18',  # 按日期
    author='play4fun',
    author_email='play4fun@foxmail.com',
    packages=find_packages(),
    install_requires=['requests', 'random_useragent'],
    license='GNU General Public License v3.0',
)

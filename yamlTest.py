# 作者：倔强的瓜小黄
# 日期：2020/5/25 下午 01:57
# 工具：PyCharm
# Python版本：3.8.0
# -*- coding: utf-8 -*-
import math
import cmath
import time
import calendar
import re
# coding:utf-8
import yaml
import os
def yamlFile(cls):
    #获取YAML文件路径
    yamlpath = os.path.join("..\\config", "aa.yaml")
    #打开yaml文件
    yaml_file = open(yamlpath, "r")
    # fp = yaml_file.read()
    yaml_dict = yaml.load(yaml_file)
    print(yaml_dict[0]['devices'])
    # return yaml_dict
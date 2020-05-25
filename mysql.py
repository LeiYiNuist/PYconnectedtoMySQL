# 作者：倔强的瓜小黄
# 日期：2020/5/25 下午 12:58
# 工具：PyCharm
# Python版本：3.8.0
# -*- coding: utf-8 -*-
import math
import cmath
import time
import calendar
import re
import pymysql

def conndb():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='599494', db='iooi', charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT * from students;")
    result = cur.fetchall()
    cur.close()
    conn.close()
    print(result)
conndb()
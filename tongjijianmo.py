# coding:UTF-8-sig
import time
import requests
from lxml import etree
import re
import os
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from concurrent.futures import ThreadPoolExecutor
f =open('zgxczx.csv',mode='w',encoding='UTF-8-sig',newline="")
def txt_content(url):
    headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
        }
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    content = res.text
    obj = re.compile(r'时间：(?P<time>.*?)</span>.*?<div class="show_containt_txt"><p>(?P<main_txt>.*?)<div class="news_user news_user_bottom fl">',re.S)
    result = obj.finditer(content)
    for i in result:
        dic = i.group("main_txt")
        dic = re.sub("<.*?>","",dic)
        dic = re.sub(",", "，", dic)
        dic.encode('gbk','ignore').decode("gbk","ignore")

        f.write(i.group("time")+','+dic+"\n")
        print(url,"下载完成")
for id1 in range(1,5):
    for i in range(1,50):
        url = f'http://www.cnfpzz.com/index.php?m=Archives&c=IndexArctype&a=index&t_id={id1}&p={i}'
        headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
            }
        res = requests.get(url, headers=headers)
        res.encoding = 'utf-8'
        content = res.text
        obj = re.compile(r'<ul class="news_ul">.*?<li><a href="(?P<half_html>.*?)">',re.S)

        result = obj.finditer(content)
        for j in result:
            a = url+j.group("half_html")
            txt_content(a.encode("gbk", 'ignore').decode("gbk", "ignore"))
        print(f"****************************************第{i}页下载完成")
        time.sleep(1)
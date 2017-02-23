#!/usr/bin/python
# -*- coding: utf-8 -*-

'''

校园网登录流程

1. 未登录时， 向任意校外网站发送请求
返回：

200

{'Content-length': '499', 'Accept-Ranges': 'bytes', 'Server': 'DrcomServer1.0',
'Connection': 'keep-alive', 'Cache-Control': 'no-cache', 'Content-type': 'text/html'}

<html><head>
<script language="JavaScript"><!--
sv=0;sv1=0;v6='http://[::]:9002/v6';myv6ip='';v4serip='172.16.0.3';m46=0;v46ip='10.12.8.74';
window.location='http://202.195.241.28/1.htm'
// --></script></head>
<!--Dr.COMWebLoginID_0.htm-->
<body>
<noscript>
<i>因为您的浏览器禁止了java脚本，请您在地址栏输入http://202.195.241.28/1.htm，然后按回车键。</i></noscript>
</body></html>


2. 重定向到http://202.195.241.28/1.htm

3. 重定向到登录页，http://202.195.241.28/jxq.htm， http://202.195.241.28/ssq.htm

登录页的form表单提交地址根据地区而不同：教学区为http://172.16.0.3/， 宿舍区为http://172.16.0.4/

'''

import re
import requests
from bs4 import BeautifulSoup
from .config import write_conf_url, read_conf_url, read_conf_account

def _get_redirect_page():
    init_url = 'http://www.baidu.com'
    try:
        response = requests.get(init_url)
        response.encoding = 'gb2312'
        page = response.text
        matches = re.findall(r"http://[A-Za-z0-9./]+.htm", page)
        first_redirect_page = matches[0]
        ip = re.findall(r"[0-9.]+", first_redirect_page)[0]
        response = requests.get(first_redirect_page)
        response.encoding = 'gb2312'
        page = response.text
        matches = re.findall(r"\"[a-zA-Z]{3}.htm\"", page)
        redirect_page = matches[len(matches) - 1].replace("\"", "")
        return "http://" + ip + "/" +redirect_page
    except Exception as e:
        raise e

def get_post_url():
    # get login page url
    login_page_url = _get_redirect_page()
    try:
        login_page = requests.get(login_page_url).text
        soup = BeautifulSoup(login_page, 'html.parser')
        post_url = soup.form['action']
        return post_url
    except Exception as e:
        print('exception: ', e)

def login():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2,ja;q=0.2'
    }
    post_url = get_post_url()
    write_conf_url(post_url)
    account = read_conf_account()
    if account is None:
        print("No User Found!")
        return
    print(account[0])
    data = {
        'DDDDD': account[0],
        'upass': account[1],
        '0MKKey': ''
    }
    try:
        response = requests.post(post_url, headers=headers, data=data)
        if response.status_code == 200:
            print('success login')
        # r.encoding = 'gb2312'
        # print r.text
    except Exception as e:
        print('exception: ', e)

def logout():
    get_url = read_conf_url() + 'F.htm'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2,ja;q=0.2',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
    }
    try:
        response = requests.get(get_url, headers=headers)
        # r.encoding = 'gb2312'
        # print r.text
        if response.status_code == 200:
            print('success logout')
        else:
            print('failed logout')
    except Exception as e:
        print('exception: ' + e)

def test_network():
    BAIDU_URL = "https://www.baidu.com"
    try:
        response = requests.get(BAIDU_URL)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        return False

def network_use_condition():
    try:
        response = requests.get(read_conf_url())
        if response.status_code == 200:
            response.encoding = 'gb2312'
            page = response.text
            time_str = re.findall(r"time='[\d ]+';", page)[0]
            flow_str = re.findall(r"flow='[\d ]+';", page)[0]
            fee_str = re.findall(r"fee='[\d ]+';", page)[0]
            time = re.findall(r"\d+", time_str)[0]
            print('Time: {:.3f} h'.format(int(time)/60))
            flow = re.findall(r"\d+", flow_str)[0]
            print("Flow: {:.3f} GB".format(int(flow)/1024/1024))
            fee = re.findall(r"\d+", fee_str)[0]
            print("Remain: {:.3f} RMB".format(int(fee)/10000))
    except Exception as e:
        raise e

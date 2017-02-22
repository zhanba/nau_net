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

__author__ = 'zhanba'

import requests, re, ConfigParser
from bs4 import BeautifulSoup

# CONF_PATH = './conf.ini'
from pkg_resources import Requirement, resource_filename, resource_exists

conf_file = resource_filename(__name__, "conf.ini")


def _get_redirect_page():
    init_url = 'http://www.baidu.com'
    try:
        r = requests.get(init_url)
        r.encoding = 'gb2312'
        page = r.text
        matches = re.findall(r"http://[A-Za-z0-9./]+.htm", page)
        first_redirect_page = matches[0]
        ip = re.findall(r"[0-9.]+", first_redirect_page)[0]
        r = requests.get(first_redirect_page)
        r.encoding = 'gb2312'
        page = r.text
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

def write_conf_url(url):
    cf = ConfigParser.ConfigParser()
    cf.read(conf_file)
    cf.set('url', 'url', url)
    cf.write(open(conf_file, 'r+'))

def read_conf_url():
    cf = ConfigParser.ConfigParser()
    try:
        cf.read(conf_file)
        url = cf.get("url", "url")
        return url
    except Exception as e:
        raise e

def read_conf_account():
    cf = ConfigParser.ConfigParser()
    try:
        cf.read(conf_file)
        username = cf.get("account", "username")
        password = cf.get("account", "password")
        return (username, password)
    except Exception as e:
        raise e


if __name__ == '__main__':
    get_post_url()

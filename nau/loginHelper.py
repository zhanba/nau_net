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

import requests, re, configparser
from bs4 import BeautifulSoup

if __name__ == '__main__':
    get_post_url()

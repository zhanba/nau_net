# http://172.16.0.3/

#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from nau_net.loginHelper import read_conf_url

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

if __name__ == '__main__':
    logout()

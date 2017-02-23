#!/usr/bin/python
# -*- coding: utf-8 -*-
from pkg_resources import resource_filename, resource_exists
import configparser


def get_config_parser():
    return configparser.ConfigParser()

def get_config_file():
    is_existed = resource_exists(__name__, "conf.ini")
    if is_existed:
        return resource_filename(__name__, "conf.ini")
    else:
        print("configuration file not exist.")

def get_config_status():
    cf = get_config_parser()
    try:
        cf.read(get_config_file())
        username = cf.get("account", "username")
        return username
    except Exception as e:
        return None

def add_user(username, password):
    cf = get_config_parser()
    cf.read(get_config_file())
    if 'account' not in cf.sections():
        cf.add_section('account')
    cf.set('account', 'username', username)
    cf.set('account', 'password', password)
    with open(get_config_file(), 'w') as configfile:
        cf.write(configfile)

def remove_user():
    cf = get_config_parser()
    cf.read(get_config_file())
    cf.remove_section('account')
    with open(get_config_file(), 'w') as configfile:
        cf.write(configfile)

def write_conf_url(url):
    cf = get_config_parser()
    cf.read(get_config_file())
    if 'url' not in cf.sections():
        cf.add_section('url')
    cf.set('url', 'url', url)
    cf.write(open(get_config_file(), 'r+'))

def read_conf_url():
    cf = get_config_parser()
    try:
        cf.read(get_config_file())
        url = cf.get("url", "url")
        return url
    except Exception as e:
        raise e

def read_conf_account():
    cf = get_config_parser()
    try:
        cf.read(get_config_file())
        username = cf.get("account", "username")
        password = cf.get("account", "password")
        return (username, password)
    except Exception as e:
        raise e

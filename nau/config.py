#!/usr/bin/python
# -*- coding: utf-8 -*-
from pkg_resources import resource_filename, resource_exists
import configparser


class Config(object):

    def __init__(self):
        pass

    @staticmethod
    def get_config_file():
        is_existed = resource_exists(__name__, "conf.ini")
        if is_existed:
            return resource_filename(__name__, "conf.ini")
        else:
            print("configuration file not exist.")

    @staticmethod
    def get_config_parser():
        return configparser.ConfigParser()

    @staticmethod
    def add_user(username, password):
        cf = Config.get_config_parser()
        cf['account']['username'] = username
        cf['account']['password'] = password
        with open(Config.get_config_file(), 'w') as configfile:
            cf.write(configfile)

    @staticmethod
    def remove_user():
        cf = Config.get_config_parser()
        cf['account'] = {}
        with open(Config.get_config_file(), 'w') as configfile:
            cf.write(configfile)

    @staticmethod
    def write_conf_url(url):
        cf = Config.get_config_parser()
        cf.read(Config.get_config_file())
        cf.set('url', 'url', url)
        cf.write(open(Config.get_config_file(), 'r+'))

    @staticmethod
    def read_conf_url():
        cf = Config.get_config_parser()
        try:
            cf.read(Config.get_config_file())
            url = cf.get("url", "url")
            return url
        except Exception as e:
            raise e

    @staticmethod
    def read_conf_account():
        cf = Config.get_config_parser()
        try:
            cf.read(Config.get_config_file())
            username = cf.get("account", "username")
            password = cf.get("account", "password")
            return (username, password)
        except Exception as e:
            raise e

    @staticmethod
    def get_config_status():
        cf = Config.get_config_parser()
        try:
            cf.read(Config.get_config_file())
            username = cf.get("account", "username")
            return username
        except Exception as e:
            return null

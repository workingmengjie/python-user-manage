# _*_ coding: UTF-8 _*_

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config(object):
    """Base config class"""
    # 版本
    VERSION = 'beta 0.1'
    # 项目名称
    PROJECTNAME = 'flask test'
    # 端口
    PORT = 10101

    SECRET_KEY = '1234567890!@#$%^&*()'

class ProdConfig(Config):
    """Production config class"""

    # 是否开启调试
    DEBUG = False
    # 主机IP地址
    HOST = '0.0.0.0'

class SitConfig(Config):
    """Development config class"""
    # Open the DEBUG
    # 是否开启调试
    DEBUG = True
    # 主机ip地址
    HOST = '127.0.0.1'


class DevConfig(Config):
    pass


# Default using Config settings, you can write if/else for different env
config = SitConfig()
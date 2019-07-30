#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import time
import datetime
import arrow
import json
import requests
import pinyin
import re
import platform
from PackRoute import Singleton


class BaseUtils(Singleton):

    @staticmethod
    def RunPosition():
        system = platform.system()
        if system == "Windows":
            env_type = "default"
        else:
            env_type = "slave1"
        return env_type

    @staticmethod
    def getMd5(value):
        m = hashlib.md5()
        m.update(value.encode('utf8'))
        return m.hexdigest()

    @staticmethod
    def MorningTime():
        today = datetime.date.today()
        today_time = int(time.mktime(today.timetuple()))
        return today_time

    @staticmethod
    def localtime():
        local_time = arrow.now().format("YYYYMMDD")
        return local_time


if __name__ == '__main__':
    Object = BaseUtils()
    Object.getMd5(value="madin")
    # O1 = Object.MorningTime()
    # print(O1)

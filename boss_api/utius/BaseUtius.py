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
from DataBases.dbfactory.dbfactory import dbfactory


class BaseUtils(object):

    @staticmethod
    def RunPosition():
        systemType = platform.system()
        if systemType == "Windows":
            env_type = "default"
        else:
            env_type = "slave1"
        return env_type

    def getMd5(self, value):
        m = hashlib.md5()
        m.update(value)
        return m.hexdigest()

    @staticmethod
    def MorningTime():
        today = datetime.date.today()
        today_time = int(time.mktime(today.timetuple()))
        return today_time

    @staticmethod
    def localtime():
        LicalTody2 = arrow.now().format("YYYYMMDD")
        return LicalTody2


if __name__ == '__main__':
    Object = BaseUtils()
    O1 = Object.MorningTime()
    print(O1)






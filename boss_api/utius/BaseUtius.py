#!/usr/bin/env python
# -*- coding: utf-8 -*-
#纯属理解copy
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
    @staticmethod
    def CityHouseData(**kwargs):
        rnv_type = BaseUtils.RunPosition()
        RedisConn = dbfactory.db_redis(conf_name=kwargs.get("conf_name", "sell"), link_type=rnv_type)
        for k,v in kwargs.items():
            HouseCity_Data = RedisConn.hget("GetCityinfo",k)
            if HouseCity_Data:
                HouseCity_Data = json.loads(str(HouseCity_Data.decode()))
                return HouseCity_Data[v]

    def getMd5(value):
        m = hashlib.md5()
        m.update(value.encode("utf8"))
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
    pass




    # Object = BaseUtils()
    # O1 = Object.MorningTime()
    # print(O1)

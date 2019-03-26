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
#根据source,type获取 该渠道下所有城市信息
class GetChannelHouseData():
    @staticmethod
    def GetChannelData(source_data):
        channel_type = {"sell":1,"new":2,"rent":3,"apartment":4,"ask":5}
        url = "http://broker.dapi.zhugefang.com/broker/detail/sourceForTheQuery"
        for k,v in source_data.items():
            servie_type = channel_type[v]
            body = {
                    "service_type": str(servie_type),
                    "source_id": str(k)
            }
            chann_result = requests.post(url,json=body)
            if chann_result.status_code == 200:
                chann_data = json.loads(chann_result.text)["data"]
                if chann_data:
                    return chann_data
                else:
                    print("响应信息!!!",chann_data)
            else:
                print("响应码返回错误!!!!")

    # 获取城市渠道信息
    @staticmethod
    def GetChannelDmInfo(city_fpy, channel, type):
        type_dict = {"sell": 1, "new": 2, "rent": 3, "apartment": 4, "ask": 5, "press": 6}
        Body = {
            "city_en": str(city_fpy),
            "source_en": str(channel),
            "service_type": type_dict.get(type),
            "all": "",
            "type": "string"
        }
        city_channel_url = "http://broker.dapi.zhugefang.com/channel/detail/getChannelDmInfo"
        result = requests.post(city_channel_url, data=json.dumps(Body))
        result_data = json.loads(result.text)['data'][0]
        return result_data




if __name__ == '__main__':
    city = "wuxi"
    channel = "Kufang"
    type = "sell"
    channe = GetChannelHouseData()

    O2 = channe.GetChannelDmInfo(city,channel,type)
    print(O2)





    # Object = BaseUtils()
    # O1 = Object.MorningTime()
    # print(O1)

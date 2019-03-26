import json
from utius.BaseUtius import BaseUtils
from DataBases.dbfactory.dbfactory import dbfactory

class HouseSellDiosService():
    def __init__(self,*args,**kwargs):
        self.redisconn = dbfactory.db_redis(conf_name=kwargs.get("conf_name", "sell"),link_type=BaseUtils.RunPosition())

    def DiosHouseData(self,city,channel_data):
        City_spyData = BaseUtils.CityHouseData(City_spy=city)
        RedisKey = f"{City_spyData['city_fpy']}-{channel_data['channel_name']}_{BaseUtils.MorningTime()}"
        result_channel_data = self.redisconn.hget("DiosEcharts",RedisKey)
        if result_channel_data:
            return json.loads(str(result_channel_data.decode()))
        else:
            return {}
    def DiosCountBackup(self,city,channel_dat):
        City_spyData = BaseUtils.CityHouseData(City_spy=city)
        RedisKey = f"{City_spyData['city_fpy']}-{channel_data['channel_name']}_{BaseUtils.MorningTime()}"
        result_channel_data = self.redisconn.hget("DiosEcharts",RedisKey)
        if result_channel_data:
            return json.loads(str(result_channel_data.decode()))
        else:
            return {}




if __name__ == '__main__':
    city = "heb"
    channel_data = {"channel_name":"Yihe"}
    Object = HouseSellDiosService()
    Object.DiosHouseData(city,channel_data)







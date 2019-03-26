

import json
from PackRoute import BaseController
from PackRoute import Route
from apps.zhuge_dios.service.detail.HouseSellDiosService import HouseSellDiosService

from apps.zhuge_dios.controller.basecontroller import Permission

route = Route()
@route("/hello")
#  Hellow = route(Hellow)
class Hellow(BaseController):
    print(route)
    # @Permission(pms=['signature'])
    def get(self,*args, **kwargs):
        self.write({"hello": "欢迎来到诸葛对接!!!!"})

# #对接渠道详情
# @route("/(?P<city>\w*)/detail/GetChannel/HouseData")
# class DiosEcharts(BaseController):
#     HouseSellDiosService = HouseSellDiosService()
#
#     # def post(self, *args, **kwargs):
#     #     data = yield self.GetChannelHouseData(*args, **kwargs)
#     #     return data
#     #
#     # def GetChannelHouseData(self, *args, **kwargs):
#     #     channel_data = json.loads(self.request.body)
#     #     print(channel_data)
#     def post(self, *args, **kwargs):
#         self.result = {"message": "success", "code": "200"}
#         try:
#             city = kwargs.get("city")
#             channel_data = json.loads(self.request.body)
#             if channel_data:
#                 result_data = self.HouseSellDiosService.DiosHouseData(city,channel_data)
#                 if result_data:
#                     self.result["data"] = result_data
#                 else:
#                     self.result["message"] = "未查询到该渠道信息!!!"
#             else:
#                 self.result["message"] = "请检查参数是否正确!!!"
#         except Exception as e:
#             print(e)
#             self.result["message"] = "请检查参数是否正确!!!"
#         self.write(self.result)
#
# #对接渠道详情
# @route("/(?P<city>\w*)/detail/GetChannel/Backup")
# class DiosEcharts(BaseController):
#     HouseSellDiosService = HouseSellDiosService()
#
#     # def post(self, *args, **kwargs):
#     #     data = yield self.GetChannelHouseData(*args, **kwargs)
#     #     return data
#     #
#     # def GetChannelHouseData(self, *args, **kwargs):
#     #     channel_data = json.loads(self.request.body)
#     #     print(channel_data)
#     def post(self, *args, **kwargs):
#         self.result = {"message": "success", "code": "200"}
#         try:
#             city = kwargs.get("city")
#             channel_data = json.loads(self.request.body)
#             if channel_data:
#                 result_data = self.HouseSellDiosService.DiosCountBackup(city,channel_data)
#                 if result_data:
#                     self.result["data"] = result_data
#                 else:
#                     self.result["message"] = "未查询到该渠道信息!!!"
#             else:
#                 self.result["message"] = "请检查参数是否正确!!!"
#         except Exception as e:
#             print(e)
#             self.result["message"] = "请检查参数是否正确!!!"
#         self.write(self.result)



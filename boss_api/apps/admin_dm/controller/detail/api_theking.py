import json
from PackRoute import BaseController
from PackRoute import Route
from apps.admin_dm.service.detail.LoginService import LoginService
from apps.admin_dm.controller.basecontroller import Permission


route = Route()
@route("/hello")
class Hellow(BaseController):

    # @Permission(pms=['signature'])
    def get(self, *args, **kwargs):
        self.write({"hello": "欢迎使用Api!!!!"})

# 前端 登陆 验证
@route("/lgn/login_info")
class LoIng(BaseController):
    LoginServices = LoginService()

    def post(self, *args, **kwargs):

        result = {"message": "success", "state": "ok", "code": True}

        try:
            user_info = json.loads(self.request.body)
            if not user_info:
                result["message"] = "账号信息获取失败!!!"
            result_data = self.LoginServices.login(user_info)

            if not result_data:
                result["message"] = "账号信息验证失败!!!"
            else:
                result["data"] = "账号信息验证成功!!!"
                result["state"] = "ok"

        except Exception as e:
            self.result["message"] = "账号信息获取失败!!!"

        self.write(self.result)
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


@route("/login")
class Login(BaseController):
    LoginServices = LoginService()

    # @Permission(pms=['signature'])
    def post(self, *args, **kwargs):
        result = {"message": "success", "state": True, "code": "200"}
        try:
            user_info = json.loads(self.request.body)
            res_user_info = self.LoginServices.login(user_info)
            if not res_user_info:
                result["state"] = False
                result["code"] = "40001"
                result["success"] = "账号信息获取失败"
                print(res_user_info)

        except Exception as e:
            result["message"] = "账号信息异常"
            result["state"] = False
            result["code"] = "40005"
        self.write(result)




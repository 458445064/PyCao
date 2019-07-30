import json
from PackRoute import BaseController
from PackRoute import Route
from apps.admin_dm.service.detail.LoginService import LoginService
# from apps.admin_dm.controller.basecontroller import Permission
from apps.admin_dm.api_error.error_test import error_text

route = Route()



@route("/hello")
class Hellow(BaseController):

    # @Permission(pms=['signature'])
    def get(self, *args, **kwargs):
        self.write({"hello": "欢迎使用Api!!!!"})


@route("/login")
class Login(BaseController):
    LoginServices = LoginService()

    # @Permission(pms=['signature'])
    def post(self, *args, **kwargs):
        try:
            user_detail = str(self.request.body, encoding="utf-8")
            result = self.LoginServices.login(user_detail)
        except Exception as e:
            result = error_text().exception
        self.write(result)

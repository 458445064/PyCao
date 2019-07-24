import json
from PackRoute import BaseController
from PackRoute import Route
from apps.admin_dm.service.detail.LoginService import LoginService
# from apps.admin_dm.controller.basecontroller import Permission
from apps.admin_dm.api_error.error_test import error_text

route = Route()

error_obj = error_text()


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
        result = error_obj.ok
        try:
            user_detail = str(self.request.body, encoding="utf-8")
            if not user_detail:
                result = error_text.params

            user_info = eval(user_detail)
            res_user_info = self.LoginServices.login(user_info)
            if not res_user_info:
                result = error_obj.notfound
        except Exception as e:
            result = error_obj.exception
        self.write(result)

import json
from PackRoute import BaseController
from PackRoute import Route
from apps.admin_dm.service.detail.LoginService import LoginService, CreateUserService, SendCodeService
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
    """
    admin 登录接口
    """
    LoginServices = LoginService()

    # @Permission(pms=['signature'])
    def post(self, *args, **kwargs):
        try:
            info = str(self.request.body, encoding="utf-8")
            result = self.LoginServices.login(info)
        except Exception as e:
            print("error: [{0}]".format(e))
            result = error_text().exception
        self.write(result)


@route("/create/user")
class CreateUserInfo(BaseController):
    """
    admin 用户创建
    """
    CreateService = CreateUserService()

    # @Permission(pms=['signature'])
    def post(self, *args, **kwargs):
        try:
            info = str(self.request.body, encoding="utf-8")
            result = self.CreateService.create_user(info)
        except Exception as e:
            print("error: [{0}]".format(e))
            result = error_text().exception
        self.write(result)


@route("/send/code")
class Send_code(BaseController):
    """
    admin 发送验证码
    """
    SendCode = SendCodeService()

    # @Permission(pms=['signature'])
    def post(self, *args, **kwargs):
        try:
            info = str(self.request.body, encoding="utf-8")
            result = self.SendCode.send_code(info)
        except Exception as e:
            print("error: [{0}]".format(e))
            result = error_text().exception
        self.write(result)

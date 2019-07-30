from apps.admin_dm.service.base_service import BaseConn
from utius.BaseUtius import BaseUtils
from apps.admin_dm.api_error.error_test import error_text


class LoginService(object):

    def __init__(self):
        self.base_conn = BaseConn(conf_name="admin_vue", db_type="db_redis")

    def login(self, user_detail):
        if not user_detail:
            return error_text().params
        user_info = eval(user_detail)
        # user_info = user_detail
        user_name = user_info.get("username")
        password = user_info.get("password")

        res_user_info = self.base_conn.redis_conn_hget(key="user_cache", data=user_name)
        if not res_user_info:
            return error_text().notfound

        if not any([password == str(res_user_info, encoding="utf-8")]):
            return error_text().password_error

        return error_text().ok


if __name__ == '__main__':
    loginservice = LoginService()
    user_info = {
        "username": "admin",
        "password": "123456"
    }
    res = loginservice.login(user_info)
    print(res)

from apps.admin_dm.service.base_service import BaseConn
from utius.BaseUtius import BaseUtils, send_code
from apps.admin_dm.api_error.error_test import error_text


class CreateUserService(object):
    """
    创建用户
    """

    def __init__(self):
        self.base_conn_redis = BaseConn(conf_name="admin_vue", db_type="db_redis", db=1)
        self.base_conn_mongo = BaseConn(conf_name="admin_vue", db_name="admin_dm", db_type="db_mongo")

    def create_user(self, info):
        redis_conn = self.base_conn_redis
        mongo_conn = self.base_conn_mongo

        docs = eval(info)
        user_name = docs.get("username")
        user_phone = docs.get("phone")
        password = docs.get("password")
        sms_code = docs.get("code")

        if not all([user_name, user_phone, password]):
            return error_text().params

        res_user_info = redis_conn.redis_conn_hget(key="user_cache", value=user_name)
        if res_user_info:
            return error_text().data_exists

        if not BaseUtils.check_phone(user_phone):
            return error_text(message="手机号格式错误.", code="40007").default_error

        check_code = redis_conn.redis_conn_hget(key="user_phone_sms_check", value=user_phone)
        if check_code is None or str(check_code, encoding="utf-8") != sms_code:
            return error_text(message="验证码校验失败.", code="40006").default_error

        md5_password = BaseUtils.getMd5(password)
        redis_conn.redis_conn_hset(name="user_cache", key=user_name, value=md5_password)

        doc = {
            "user_name": docs.get("username"),
            "user_phone": docs.get("phone"),
            "password": md5_password,
            "create_time": BaseUtils.localtime(),
            "update_time": BaseUtils.localtime()
        }
        # mongo 时间需要改一下
        res_value = mongo_conn.mongo_conn_insert(doc=doc, table="user")
        if not res_value:
            return error_text(message="系统内部错误.", code="45555").default_error

        return error_text().ok


class SendCodeService(object):
    """
    发送验证码
    """

    def __init__(self):
        self.base_conn_redis = BaseConn(conf_name="admin_vue", db_type="db_redis", db=1)

    def send_code(self, info):
        redis_conn = self.base_conn_redis

        docs = eval(info)
        phone = docs.get("phone")
        if not BaseUtils.check_phone(phone):
            return error_text(message="手机号格式错误.", code="40007").default_error

        res_code = send_code(phone=phone)
        print("this is send code", res_code)
        if not res_code:
            return error_text(message="验证码发送失败.", code="40008").default_error
        res = redis_conn.redis_conn_hset(name="check_phone_code", key=phone, value=res_code, expired_time=30)
        print(res, "添加完过期时间值", res)




        return error_text().ok



class LoginService(object):
    """
    用户登录
    """

    def __init__(self):
        self.base_conn = BaseConn(conf_name="admin_vue", db_type="db_redis")

    def login(self, info):
        if not info:
            return error_text().params
        user_info = eval(info)
        # user_info = user_detail
        user_name = user_info.get("username")
        password = user_info.get("password")

        res_user_info = self.base_conn.redis_conn_hget(key="user_cache", value=user_name)
        if not res_user_info:
            return error_text().notfound

        if not any([password == str(res_user_info, encoding="utf-8")]):
            return error_text().password_error

        return error_text().ok


# if __name__ == '__main__':
#     loginservice = LoginService()
#     user_info = {
#         "username": "admin",
#         "password": "123456"
#     }
#     res = loginservice.login(user_info)
#     print(res)

from DataBases.dbfactory.dbfactory import dbfactory


class LoginService(object):

    def __init__(self, *args, **kwargs):
        self.conn = dbfactory.create_db(conf_name="admin_vue", db_name="admin_dm", db_type="db_mysql")

    def login(self, user_info):

        user_name = user_info.get("username")
        password = user_info.get("password")
        sql = f"""
        select  user_name from user where user_name = '{user_name}' and password = '{password}' and state = 1
        """

        with self.conn.get_conn() as cursor:
            cursor.execute(sql)
            res = cursor.fetchall()
            return res




if __name__ == '__main__':
    loginservice = LoginService()
    user_info = {
        "user_name": "admin",
        "password": "123456"
    }
    res = loginservice.login(user_info)
    print(res)






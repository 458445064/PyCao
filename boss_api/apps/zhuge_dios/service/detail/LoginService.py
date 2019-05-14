import json
from utius.BaseUtius import BaseUtils
from DataBases.dbfactory.dbfactory import dbfactory

class LoginService():
    def __init__(self,*args,**kwargs):
        self.conn = dbfactory.create_db(conf_name=kwargs.get("conf_name","vue"),db_name="test", db_type="db_mysql")


    def LoginAuthentication(self,user_info):
        user_name = user_info.get("user_name")
        user_password = user_info.get("password")

        sql = f"""
        select user_name from user_info where user_name = "{user_name}" and user_password = "{user_password}"
        """
        with self.conn.get_conn() as cursor:
            cursor.execute(sql)
            res = cursor.fetchall()
            if res:
                return res[0]



if __name__ == '__main__':
    pass






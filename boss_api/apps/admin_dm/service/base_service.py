# -*- coding: utf-8 -*-
# @Author : Caojunliang
# @Time : 2019-07-30 10:52
# @File : base_service.py
from PackRoute import Singleton
from DataBases.dbfactory.dbfactory import dbfactory


class BaseConn(Singleton):

    def __init__(self, conf_name=None, db_name=None, db_type="db_mysql", db=1):
        self.mysql_conn = dbfactory.create_db(conf_name=conf_name, db_name=db_name, db_type=db_type)
        self.redis_conn = dbfactory.create_db(conf_name=conf_name, db=db, db_type=db_type)

    def mysql_conn_find(self, sql):
        with self.mysql_conn.get_conn() as cursor:
            cursor.execute(sql)
            res = cursor.fetchall()
            return res

    def redis_conn_hget(self, key, data):
        with self.redis_conn.get_conn() as cursor:
            res = cursor.hget(key, data)
            return res


if __name__ == '__main__':
    obj2 = BaseConn(db_type="db_redis", conf_name="admin_vue")
    obj2.redis_conn_hget(data='21232f297a57a5a743894a0e4a801fc3')
#     sql = f"""
#     select  user_name from user where user_name = 'admin' and password = '123456' and state = 1
#     """
#
#     obj1 = BaseConn(conf_name="admin_vue", db_name="admin_dm", db_type="db_mysql")
#     obj1.mysql_conn_find(sql)

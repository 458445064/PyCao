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
        self.mongo_conn = dbfactory.create_db(conf_name=conf_name, db_name=db_name, db_type=db_type)

    def mysql_conn_find(self, sql):
        with self.mysql_conn.get_conn() as cursor:
            cursor.execute(sql)
            res = cursor.fetchall()
            return res

    def redis_conn_hget(self, key, value):
        with self.redis_conn.get_conn() as cursor:
            res = cursor.hget(key, value)
            return res

    def redis_conn_hset(self, name, key, value, expired_time=0):
        with self.redis_conn.get_conn() as cursor:
            res = cursor.hset(name, key, value)
            if expired_time:
                cursor.expire(name, expired_time)
                print("添加过期时间.", expired_time)
            return res

    def mongo_conn_insert(self, doc, table):
        with self.mongo_conn.get_conn() as cursor:
            insert_value = cursor[table].insert_one(doc)
            return insert_value


if __name__ == '__main__':
    mongo = BaseConn(conf_name="admin_vue", db_name="admin_dm", db_type="db_mongo")
    mongo.mongo_conn_insert({"name": "zhengxiaofei"}, table="user")
    # obj2 = BaseConn(db_type="db_redis", conf_name="admin_vue")
    # obj2.redis_conn_hset(name="user_phone_sms_check", key="17611406012", value="55555")
#     sql = f"""
#     select  user_name from user where user_name = 'admin' and password = '123456' and state = 1
#     """
#
#     obj1 = BaseConn(conf_name="admin_vue", db_name="admin_dm", db_type="db_mysql")
#     obj1.mysql_conn_find(sql)

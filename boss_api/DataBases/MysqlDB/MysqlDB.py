# -*- coding: UTF-8 -*-

import pymysql
from apps.config.Config import mysql_conf
import contextlib
import logging
class MysqlDB(object):
    def __init__(self, *args, **kwargs):
        self.conf_name = kwargs.get("conf_name")
        self.db_name = kwargs.get("db_name")



    @contextlib.contextmanager
    def get_conn(self, *args, **kwargs):
        # 获取主从连接
        self.conf = mysql_conf.get(self.conf_name)
        conf = self.conf.get(kwargs.get("link_type", 'default'))
        host = conf.get("host")
        port = conf.get("port")
        user = conf.get("user")
        passwd = conf.get("password")
        conn = pymysql.connect(host=host, port=port, user=user, password=passwd, db=self.db_name, charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            yield cursor
            conn.commit()
        except Exception as e:
            conn.rollback()
            logging.error(e)
        finally:
            cursor.close()
            conn.close()


    def get_connection(self, *args, **kwargs):
        # 获取主从连接
        conf = self.conf.get(kwargs.get("link_type", 'default'))
        city = kwargs.get("city")
        host = conf.get("host")
        port = conf.get("port")
        user = conf.get("user")
        passwd = conf.get("passwd")

        db_name = get_db(type=self.conf_name, city=city)
        conn = pymysql.connect(host=host, port=port, user=user, password=passwd, db=db_name, charset="utf8")
        return conn
# -*- coding: utf-8 -*- 
# @Author : Caojunliang 
# @Time : 2019-07-31 11:05 
# @File : MongoDB.py
import pymongo
import contextlib
from apps.config.Config import mongo_conf


class MongoDB(object):

    def __init__(self, **kwargs):
        self.conf_name = kwargs.get("conf_name")
        self.db_name = kwargs.get("db_name")
        self.link_type = kwargs.get("link_type", "local")
        self.db_table = kwargs.get("db_table")

    @contextlib.contextmanager
    def get_conn(self):
        conf_info = mongo_conf.get(self.conf_name)
        conf = conf_info.get(self.link_type)
        client = pymongo.MongoClient(
            host=conf["host"],
            port=conf["port"]
        )
        cursor = client[self.db_name]

        yield cursor


if __name__ == '__main__':
    mongo = MongoDB(conf_name="admin_vue", db_name="admin_dm", link_type="local")
    with mongo.get_conn() as cursor:
        value = cursor['user'].find_one({"name": "asd"})
        print(value)

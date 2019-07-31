# -*- coding: utf-8 -*-
from DataBases.MysqlDB.MysqlDB import MysqlDB
from DataBases.RedisDB.RedisDB import RedisDB
from DataBases.MongoDB.MondoDB import MongoDB


class dbfactory():
    @staticmethod
    def create_db(**kwargs):
        db_type = kwargs.get("db_type")
        return getattr(dbfactory, db_type)(**kwargs)

    @staticmethod
    def db_mysql(*args, **kwargs):
        return MysqlDB(**kwargs)

    # @staticmethod
    # def db_tidb(*args, **kwargs):
    #     return TiDB(**kwargs)
    #
    @staticmethod
    def db_mongo(*args, **kwargs):
        return MongoDB(**kwargs)
    #
    # @staticmethod
    # def db_es(*args, **kwargs):
    #     return EsDB(**kwargs)

    @staticmethod
    def db_redis(*args, **kwargs):
        return RedisDB(**kwargs)
    #
    # @staticmethod
    # def db_pika(*args, **kwargs):
    #     return PikaDB.getPikaConn(**kwargs)
    #
    # @staticmethod
    # def db_rabbitmq(*args, **kwargs):
    #     return Rabbitmq(**kwargs)

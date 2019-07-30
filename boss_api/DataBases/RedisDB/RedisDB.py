# -*- coding: utf-8 -*-s
import redis
import contextlib
from apps.config.Config import redis_conf


class RedisDB(object):
    def __init__(self, **kwargs):
        self.conf_name = kwargs.get("conf_name")
        self.db = kwargs.get("db")
        self.link_type = kwargs.get("link_type", "default")

    @contextlib.contextmanager
    def get_conn(self, **kwargs):
        conf_info = redis_conf.get(self.conf_name)
        conf = conf_info.get(self.link_type)
        pool = redis.ConnectionPool(
            host=conf["host"],
            port=conf["port"],
            password=conf["password"],
            db=self.db
        )  # 连接池
        redis_cursor = redis.Redis(connection_pool=pool)

        yield redis_cursor

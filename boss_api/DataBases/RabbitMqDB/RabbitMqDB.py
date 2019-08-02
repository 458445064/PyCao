# -*- coding: utf-8 -*- 
# @Author : Caojunliang 
# @Time : 2019-08-02 10:59 
# @File : RabbitMqDB.py 


import pika
import contextlib
from apps.config.Config import rabbit_mq_conf


class RabbitMqDB(object):

    def __init__(self, **kwargs):
        self.queue = kwargs.get("queue_name")

    @contextlib.contextmanager
    def conn(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=rabbit_mq_conf["host"]
            )
        )
        channel = connection.channel()

        try:
            yield channel
        except Exception as e:
            print("rabbit cursor error:[{0}]".format(e))
        finally:
            channel.close()


if __name__ == '__main__':
    test_mq = RabbitMqDB()
    test_mq.conn()
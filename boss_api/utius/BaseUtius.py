#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import arrow
import re
import platform
import nexmo
import string
import random
from PackRoute import Singleton


class BaseUtils(Singleton):

    @staticmethod
    def RunPosition():
        """
        判断运行环境 mac:slave1
        :return:
        """
        system = platform.system()
        if system == "Windows":
            env_type = "default"
        else:
            env_type = "slave1"
        return env_type

    @staticmethod
    def getMd5(value):
        """
        MD5 加密
        :param value:
        :return:
        """
        m = hashlib.md5()
        m.update(value.encode('utf8'))
        return m.hexdigest()

    @staticmethod
    def localtime():
        """
        获取本地时间 2019-07-31 16:45:47
        :return:
        """
        local_time = arrow.now().format("YYYY-MM-DD HH:mm:ss")
        return local_time

    @staticmethod
    def check_phone(phone):
        """
        正则校验 手机格式
        :return:
        """
        pattern_phone = r"^1(?:3\d|4[4-9]|5[0-35-9]|6[567]|7[013-8]|8\d|9\d)\d{8}$"
        if re.match(pattern_phone, phone):
            return True


    @staticmethod
    def check_card(card):
        """
        正则校验 身份证 格式
        :param card:
        :return:
        """
        pattern_card = r"^(^[1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}$)|(^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])((\d{4})|\d{3}[xX])$)$"
        if not re.match(pattern_card, card):
            return False


def send_code(phone):
    client = nexmo.Client(key='9e6881d8', secret='EfmTX6rrUe64X3RE')
    seeds = string.digits
    random_str = random.choices(seeds, k=4)
    code = "".join(random_str)

    res_send_code = client.send_message({
        'from': 'admin_vue',
        'to': f'86{phone}',
        'text': f'admin_vue 验证码:{code}',
    })
    # send_state = res_send_code.get("messages")[0].get("status")
    print(res_send_code)
    return code
    # if send_state is None or send_state != '0':
    #     return False
    # else:
    #     return code

    # if not res_send_code:
    #     return False
    # else:


if __name__ == '__main__':
    # Object = BaseUtils()
    send_code(phone="17611406012")
    # Object.getMd5(value="madin")
    # O1 = Object.check_phone(phone="17611406012")

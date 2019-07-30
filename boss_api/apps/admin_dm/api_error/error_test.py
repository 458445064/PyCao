from PackRoute import Singleton


class error_text(Singleton):
    """
    api 接口返回文本
    """

    def __init__(self):
        self.__ok = {"message": "success", "code": "200", "name": True}
        self.__notfound = {"message": "该账号不存在", "code": "40001", "name": False}
        self.__exception = {"message": "账号异常", "code": "40002", "name": False}
        self.__params = {"message": "参数异常", "code": "40003", "name": False}

    @property
    def ok(self):
        """
        成功
        :return:
        """
        return self.__ok

    @property
    def notfound(self):
        """
        账号不存在
        :return:
        """
        return self.__notfound

    @property
    def exception(self):
        """
        账号异常
        :return:
        """
        return self.__exception

    @property
    def params(self):
        return self.__params

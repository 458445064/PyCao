from PackRoute import Singleton


class error_text(Singleton):
    """
    api 接口返回文本
    """

    def __init__(self, message='', code='4444'):
        self.__ok = {"message": "success", "code": "200", "name": True}
        self.__notfound = {"message": "该账号不存在", "code": "40001", "name": False}
        self.__exception = {"message": "状态异常", "code": "40002", "name": False}
        self.__params = {"message": "参数异常", "code": "40003", "name": False}
        self.__password_error = {"message": "密码错误", "code": "40004", "name": False}
        self.__data_exists = {"message": "数据已存在", "code": "40005", "name": False}
        self.__default_error = {"message": message, "code": code, "name": False}

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
        状态异常
        :return:
        """
        return self.__exception

    @property
    def params(self):
        """
        参数错误
        :return:
        """
        return self.__params

    @property
    def password_error(self):
        """
        密码错误
        :return:
        """
        return self.__password_error

    @property
    def data_exists(self):
        """
        数据已存在
        :return:
        """
        return self.__data_exists

    @property
    def default_error(self):
        """
        自定义 message
        :return:
        """
        return self.__default_error


if __name__ == '__main__':
    # obj = error_text()
    ok = error_text().ok
    print(ok)

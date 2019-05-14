
import time
import arrow


class RequestUtius():
    @staticmethod
    def LocalTime():
        localtime = time.time()
        LicalTody = arrow.now().format("YYYYMMDD")
        return LicalTody


if __name__ == '__main__':
    Object = RequestUtius()
    is_result = Object.LocalTime()
    print(is_result)
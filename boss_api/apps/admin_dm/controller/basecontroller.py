import json
import re


def Permission(*Fargs, **Fkwargs):
    # {"pms": [xxx]}

    def wrapper(func):
        def wrapper_(*args, **kwargs):
            request = args[0]
            path = request.request.path
            # sign = Fkwargs["pms"]
            # sdk = re.findall(r"", path)
            # signature
            # result = {"message": "签名验证失败", "code": "4001", "state": False}
            # request.write(json.dumps(result))
            func(*args, **kwargs)

        return wrapper_

    return wrapper
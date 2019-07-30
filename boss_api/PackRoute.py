import tornado.web
import time
import json


class Singleton(object):
    _instance = None

    @classmethod
    def instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance


class Route(object):
    def __init__(self):
        self.urls = []

    def __call__(self, url, *args, **kwargs):
        def wrapper(cls):
            self.urls.append((url, cls))
            return cls

        return wrapper


def catch_yield(*dargs, **dkwargs):
    def wrapper(func):
        @tornado.gen.coroutine
        def _wrapper(*args, **kargs):
            request = args[0]
            try:
                st = time.time()
                result = {"message": "success", "code": 200}
                fun = yield func(*args, **kargs)
                et = time.time() - st
                result["time"] = et
                result["page"] = fun.get("page", {})
                result["data"] = fun.get("data", [])
                result["code"] = fun.get("code", 200)
                if fun.get("total") or 0:
                    result["total"] = fun.get("total", 0)
                if fun.get("message"):
                    result["message"] = fun.get("message")
                request.write(json.dumps(result))
            except Exception as e:
                result = {"message": str(e), "code": 500}
                request.write(json.dumps(result))

        return _wrapper

    return wrapper


class BaseController(tornado.web.RequestHandler):
    # executor = Executor()
    #
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    # @catch_yield()
    # @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        data = yield self.gethandle(*args, **kwargs)
        return data

    # @catch_yield()
    # @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        data = yield self.posthandle(*args, **kwargs)
        return data
    # @catch_yield()
    # @tornado.gen.coroutine
    # def head(self, *args, **kwargs):
    #     data = yield self.headhandle(*args, **kwargs)
    #     return data

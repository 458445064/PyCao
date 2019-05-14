import sys
sys.path.append("../../../")
import tornado.ioloop
from PackRoute import Route
from apps.zhuge_dios.controller.detail.api_theking import route as route1



if __name__ == '__main__':
    routes = route1.urls
    application = tornado.web.Application(routes)
    application.listen(3361)
    tornado.ioloop.IOLoop.instance().start()


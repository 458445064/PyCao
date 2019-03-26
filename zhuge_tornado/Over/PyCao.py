
#装饰器

#
# import time
# def warp(func):
#     print(func)
#     def warp1_(*args,**kwargs):
#         func()
#         print(time.clock())
#     return warp1_
#
#
# @warp
# def text1():
#     num = 1 + 1
#     print(num)
#
# if __name__ == '__main__':
#     text1()



#Tornado refoul



class Start_api():
    def __init__(self):
        self.list = []
    def __call__(self,url, *args, **kwargs):
        print("__call__运行")
        def warp(func):
            print(func,"调用装饰器")
            self.list.append((url,func))
            print(self.list)
            return func
        return warp

route = Start_api()

@route("/hellow")
class Hellow():
    pass
Object = Hellow()
print(Object,"is_ok")
print(route.list)






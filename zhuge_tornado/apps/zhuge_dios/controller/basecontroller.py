
import json
#小接口

def Permission(*Fargs,**Fkwargs):

    def wrapper(func):
        def wrapper_(*args,**kwargs):
            request = args[0]
            path = request.request.path
            print(path,"uri")
            func(*args,**kwargs)
            # result = {"message": "诸葛!!!", "code": 999, "data": []}
            # request.write(json.dumps(result))
        return wrapper_
    return wrapper
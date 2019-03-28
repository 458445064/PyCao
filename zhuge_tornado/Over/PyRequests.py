
import requests
import time
class ObjRequest():
    def __init__(self):
        pass
    def ReGet(self,url,hander):
        pass

    def RePosh(self,url,hander):
        pass

    def Run(self):
        is_time = int(time.time())
        print(is_time)
        # start_url = "https://passport.lagou.com/login/login.html?"
        start_url = "https://passport.lagou.com/login/login.json"
        body = {
            "isValidate":True,
            "username":17611406012,
            "password":"8951975d0ce677ffb11f47f968ef5130",
            "request_form_verifyCode":"",
            "submit":"",
            "challenge":"8b1d5d79184afa83b86926ea09b504f4"
        }
        hander = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "154",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie":f"""
_ga=GA1.2.1878069029.1553489289;user_trace_token=20190325124807-2f3a5d80-4eb9-11e9-b4ac-5254005c3644;LGUID=20190325124807-2f3a62ab-4eb9-11e9-b4ac-5254005c3644;index_location_city=%%E5%%85%%A8%%E5%%9B%%BD;_ga=GA1.3.1878069029.1553489289;JSESSIONID=ABAAABAAAHAAAFDCAF7115D76DAEF9EE57AB8E7B60CB3D2;_gid=GA1.2.53899997.1553654667;LGSID=20190327104425-3bb7503d-503a-11e9-b755-5254005c3644;Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1553489289,1553654667,1553654727;sensorsdata2015jssdkcross=%%7B%%22distinct_id%%22%%3A%%22169b32d70af976-014eda45415a84-47e1f32-3686400-169b32d70b0940%%22%%2C%%22%%24device_id%%22%%3A%%22169b32d70af976-014eda45415a84-47e1f32-3686400-169b32d70b0940%%22%%2C%%22props%%22%%3A%%7B%%22%%24latest_traffic_source_type%%22%%3A%%22%%E7%%9B%%B4%%E6%%8E%%A5%%E6%%B5%%81%%E9%%87%%8F%%22%%2C%%22%%24latest_referrer%%22%%3A%%22%%22%%2C%%22%%24latest_referrer_host%%22%%3A%%22%%22%%2C%%22%%24latest_search_keyword%%22%%3A%%22%%E6%%9C%%AA%%E5%%8F%%96%%E5%%88%%B0%%E5%%80%%BC_%%E7%%9B%%B4%%E6%%8E%%A5%%E6%%89%%93%%E5%%BC%%80%%22%%7D%%7D;TG-TRACK-CODE=undefined;_gat=1;login=false;unick="";_putrc="";LG_LOGIN_USER_ID="";LGRID=20190327111620-b14bd3c8-503e-11e9-b759-5254005c3644;Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6={is_time}            """,
            "Host": "passport.lagou.com",
            "Origin": "https://passport.lagou.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"

        }
        lagou_result = requests.post(start_url,json=body,headers=hander)
        print(lagou_result.status_code)
        print(lagou_result.text)
        print(lagou_result.encoding)



if __name__ == '__main__':
    Obj = ObjRequest()
    Obj.Run()

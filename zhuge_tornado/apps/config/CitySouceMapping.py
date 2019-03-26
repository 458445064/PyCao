#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 下午1:55
# @Author  : janguo@zhugefang.com
# @Site    : 
# @File    : CitySouceMapping.py
# @Software: PyCharm



def get_db(type, city):
    not_bj = {"borough": "spider", "plathouse": "spider", "sell": "spider", "rent": "rent"}
    bj = {"brokerhouse": "brokerhouse", "complex": "newhouse", "building": "building" ,"brokerbd":"brokerswarehouse", "broker":"brokers"}
    mag = {"zhuge_dm": "zhuge_dm", "comphousemag": "comphousemag", "brokers": "brokers" ,"hidden_etl": "count","hidden_new": "count", "operation":"operation", "newhouse_dock":"newhouse_dock"}
    if type in bj:
        db = bj.get(type) + "_" + city
        return db
    elif type in not_bj:
        db = not_bj.get(type) if city == "bj" else not_bj.get(type) + "_" + city
        return db
    elif type in mag:
        return mag.get(type)

sell_old=['bj','bd','cc','cd','cq','cs','cz','dg','dl','fz','guilin','gy','gz','heb','hf','hhht','hn','huizhou','hz','jh','jm','jn','km','ks','lf','ly','lz','nb','nc','nj','nn','nt','qd','qhd','qz','sh','sjz','su','sx','sy','sz','taiyuan','taizhou','tj','ts','weihai','wf','wh','wx','xa','xaxq','xm','xz','yc','yinchuan','yt','yz','zh','zs','zz']

sell_new=['fs', 'jx', 'wz','xianyang','jiujiang', 'wlmq', 'bh', 'lyg','tz','zhenjiang','huzhou','yancheng','st','hd','wuhu','bt','chengde','dali','ganzhou','huaian','liuzhou','ls','mianyang','nanyang','qujing','sq','xn','xx','zhangjiakou','zhuzhou']

def getConfigName(city, type):
    if "sell" == type:
        if city in sell_old:
            return "sell"
        else:
            return "new_sell"
    return type

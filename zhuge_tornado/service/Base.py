#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-13 上午10:49
# @Author  : jianguo@zhugefang.com
# @Desc    :
class Base(object):

    # @LocalCache()
    # def getByPageFilter(self,city,page,fields={},condition={}):
    #     return self.dao.getByPageFilter(city,page,fields,condition)

    def getByTreeData(self, city, show_field=(), condition={}):
        recordCount = self.dao.getByTreeData(city, show_field, condition)
        return recordCount


def select():
    pass
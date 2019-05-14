
from dao.BaseDao.BaseMysql import BaseMysql
from apps.zhuge_sell.model.detail.HouseSellGov import HouseSellGov
import time

class HouseSellGovDao(BaseMysql):
    def __init__(self, *args, **kwargs):
        super().__init__(conf_name=kwargs.get("conf_name", "sell"), model=kwargs.get("model", HouseSellGov))

    def update_dial_num(self, *args, **kwargs):
        id = kwargs.get('id')
        sql = "update %s set dial_time = dial_time+1,updated = %s where id = %d" % (self.table, int(time.time()), id)
        return self.exe_u_sql(city=kwargs.get('city'), sql={'sql': sql})

    def getGovIds(self, *args, **kwargs):
        city = kwargs.get('city')
        house_ids = kwargs.get('house_ids')
        sql = "select id,gov_id from %s where gov_id in (%s)"%(self.table,house_ids)
        resultList = self.exe_s_sqls(city=city, sql={"sql":sql})
        return resultList

    def getExUrl(self, *args, **kwargs):
        city = kwargs.get("city")
        expireTime = kwargs.get("expireTime")
        source = kwargs.get("source")
        company_id = kwargs.get("company_id")
        source_owner = kwargs.get("source_owner")
        link_type = kwargs.get('link_type', 'default')
        if source_owner == "0":
            sql = f"select source_url from house_sell_gov where source = {source} and company_id = {company_id} and refresh_time < {expireTime}"
        else:
            sql = f"select source_url from house_sell_gov where source = {source} and company_id = {company_id} and source_owner = {source_owner} and refresh_time < {expireTime}"
        return self.exe_s_sqls(city=city, sql={"sql":sql},link_type=link_type)

    def getHiddenUrl(self, *args, **kwargs):
        city = kwargs.get("city")
        source = kwargs.get("source")
        company_id = kwargs.get("company_id")
        source_owner = kwargs.get("source_owner")
        link_type = kwargs.get('link_type', 'default')
        if source_owner == "0":
            sql = "select source_url from house_sell_gov where source=%s and company_id=%s limit 10" %(source,company_id)
        else:
            sql = "select source_url from house_sell_gov where source=%s and company_id=%s and source_owner=%s" %(source,company_id,source_owner)
        return self.exe_s_sqls(city=city, sql={"sql": sql}, link_type=link_type)

    def get_by_filter(self, *args, **kwargs):
        city = kwargs.get("city")
        link_type = kwargs.get('link_type', 'default')
        filter = kwargs.get('filter', '1=1')
        field = ",".join(kwargs.get('field', ['*']))
        sql = f"SELECT {field} FROM city WHERE {filter}"
        data = self.exe_s_sqls(link_type=link_type, city=city, sql={'sql': sql})
        return data

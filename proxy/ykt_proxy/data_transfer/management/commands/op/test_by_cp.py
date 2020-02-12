# -*- encoding:utf-8 -*-
"""
导入省份城市信息, 最开始建库的时候用,后期不再用
"""
from django.core.management import BaseCommand

from data_transfer.module_managers.hcnu_manager import hcnu_get_department_data


class Command(BaseCommand):
    def __init__(self):
        super(Command, self).__init__()

    def handle(self, *args, **optionds):
        """
        python manage.py exec test_by_cp
        """
        a = [1, 2, 3]
        b = [11, 22, 33]
        c = dict(zip(a, b))
        ret_data = hcnu_get_department_data()
        print ret_data



        # conn = psycopg2.connect(database="datacenter", user="readonly", password="readonly", host="10.155.10.180", port="5432")
        # cursor = conn.cursor()
        # cursor.execute("select xymc from data_jw.jx_xy")
        #
        # cursor.execute("select * from data_out.v_ids")
        #
        # rows = cursor.fetchall()
        # print rows
        #
        #
        #
        # statement = "select XH,  XM,  YXSH,  ZYM,  SZBH,  SZNJ,  RXNY,  XZ,  XSDQZTM from icdc_gx.V_XSJBXX_BKS"
        # ret_list = []
        # data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
        # for data in data_list:
        #     keys_list = ["number", "name", 'department_code', 'major_code', 'tra_class_code', 'term',
        #                  'come_in_year', 'xuezhi', 'current_status_code']
        #     ret_list.append(query_data_to_dict(data, keys=keys_list))
        #
        # print ret_list


from data_transfer.data_proxy_utils import OracleTransferHandler


def query_data_to_dict_list(query_data_list_of_tuple, keys_list):
    final_list = []
    for tuple_item in query_data_list_of_tuple:
        tmp_dict = dict(zip(keys_list, tuple_item))
        final_list.append(tmp_dict)
    return final_list


def get_client(func):
    """
    """

    def wrapper():
        conn = OracleTransferHandler(connect_str="gzsf_jwgl/gzsf_jwgl123@192.168.0.94:1521/orcl")
        return func(conn)

    return wrapper


@get_client
def zufe_get_bks_data(db):
    statement = "select XH,  XM,  YXSH,  ZYM,  SZBH,  SZNJ,  RXNY,  XZ,  XSDQZTM from icdc_gx.V_XSJBXX_BKS"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["number", "name", 'department_code', 'major_code', 'tra_class_code', 'term',
                 'come_in_year', 'xuezhi', 'current_status_code']
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data



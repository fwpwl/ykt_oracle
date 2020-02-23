# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR


def get_db_client():
    """
    数据库连接
    """
    db_client = OracleTransferHandler(connect_str="yjs_ykt_share/yjs_ykt_share123456@202.197.122.25:1522/sdorcl")
    return db_client


def is_valid_request(key):
    """
    key校验
    """
    if not key or key != cal_md5(get_now_datetime_str(FORMAT_DATE_WITHOUT_SEPARATOR)):
        return False
    return True


def query_data_to_dict_list(query_data_list_of_tuple, keys_list):
    final_list = []
    for tuple_item in query_data_list_of_tuple:
        tmp_dict = dict(zip(keys_list, tuple_item))
        final_list.append(tmp_dict)
    return final_list


def hnnuyjs_get_department_data():
    statement = "select xymc from hunnu_share.yks_ykt_xyxxb"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", ]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

def hnnuyjs_get_tra_data():
    # statement = "select ssxy, ZY, bjmc, RXNJ from hunnu_share.yks_ykt_xyxxb"
    # data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    # keys_list = ["department_name", "major", 'tra_classroom_name', "year"]
    # final_info_list = query_data_to_dict_list(data_list, keys_list)
    return []

def hnnuyjs_get_user_data():
    statement = "select SSXY, XM, XH, SF, RXNY from hunnu_share.yks_ykt_rysj"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", 'name', 'number', 'user_type', 'year']
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

def hnnuyjs_get_course_data(year, term):
    statement = "select SSXY, kch, kcmc, xkh, kcbjmc, jsgh, jsxm, KKXN, KKXQ from hunnu_share.yjs_ykt_kc where KKXN='{}' and KKXQ='{}'".format(year, term)
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "course_code", "course_name", 'classroom_code', "classroom_name", 
        "teacher_number", "teacher_name", "year", "term"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

def hnnuyjs_get_choose_data(year, term):
    statement = "select BJID, XH from hunnu_share.yjs_ykt_xk where KKXN='{}' and KKXQ='{}'".format(year, term)
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["classroom_code", "student_number"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

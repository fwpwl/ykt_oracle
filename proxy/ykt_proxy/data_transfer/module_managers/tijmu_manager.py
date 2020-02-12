# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR


def get_db_client():
    """

    """
    db_client = OracleTransferHandler(connect_str="tjykdx123/tjykdx123@202.113.53.229:1521/orcl")
    return db_client


def is_valid_request(key):
    """

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


# -----------------------  选课 数据 -----------------------
def tijmu_get_user_data():
    statement = "select SSXY, XZBJMC, XM, XH, SF, RXXN from xxcyb"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "tra_class_name", 'name', 'number', 'user_type', 'year']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def tijmu_get_teacher_data():
    statement = "select SSXY, JSGH, XM, SF from jscyb"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "teacher_number", 'teacher_name', 'user_type']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def tijmu_get_course_data(year='2019-2020-1'):
    statement = "select KCMC, KCH, KXH, JSGH, SKJSMC, KKXY, JYS, XNXQ from bxqkkxxb where XNXQ='{}'".format(year)
    print(statement)

    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["KCMC", "KCH", 'KXH', "JSGH", "SKJSMC",
                 "KKXY", "JYS", "XNXQ", ]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def tijmu_get_choose_data():
    statement = "select KXH, XH from bxqxksjb"

    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["KXH", "XH"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list

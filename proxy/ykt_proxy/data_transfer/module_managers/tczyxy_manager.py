# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR


def get_db_client():
    """

    """
    db_client = OracleTransferHandler(connect_str="LY_XTZX/LY_XTZX@10.0.2.90:1521/ORCL")
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
def tczyxy_get_user_data():
    statement = "select SSXY, BJMC, XM, XH, RXXN,SF from LY_XTZX.LY_QTCYB"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "tra_class_name", 'name', 'number', 'year', 'role']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def tczyxy_get_course_data(year='2019-2020', term='1'):
    statement = "select KCMC, KCBJMC, KCH, XKH, JSGH, SSXY, KKXN, KKXQ from LY_XTZX.LY_BXQKKXXB where KKXN='{}' and KKXQ='{}'".format(
        year, term)
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["course_name", 'classroom_name', 'course_code', 'classroom_code', 'teacher_number', 'department',
                 'year', 'term']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def tczyxy_get_choose_data():
    """

    """
    statement = "select XKH, XH from LY_XTZX.LY_BXQXKSJB"

    print(statement)

    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["classroom_code", 'student_number']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list

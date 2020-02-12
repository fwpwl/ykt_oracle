# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR


def get_db_client():
    """

    """
    db_client = OracleTransferHandler(connect_str="zf_jk_ykt/zf_jk_ykt@202.194.133.103:1521/sdnydx")
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
def sdau_get_department_data():
    statement = "select xymc from xyxxb"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def sdau_get_tradition_class_data():
    statement = "select ssxy, zy, bjmc, rxxn from xzbjb"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "major", "tradition_classroom_name", "year"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def sdau_get_user_map_data():
    statement = "select ssxy, xzbjmc, xm, xh, rxxn, sf from qtcyb"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "tradition_classroom_name", "name", "number", "year", "user_type", ]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def sdau_get_course_class_data(year='2019', term='1'):
    statement = "select ssxy, kcmc, kch, jsgh, JSXM, KKXN, KKXQ, JXBMC from bxqkkxxb where KKXN='{}' and KKXQ='{}'".format(year, term)
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "course_name", "course_code", "teacher_number", "teacher_name", "year", "term", "JXBMC"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def sdau_get_choose_course_data(year='2019', term='1'):
    statement = "select JXB_ID, XH_ID, XKXN, XKXQ from bxqxkxxb WHERE XKXN='{}' and XKXQ='{}'".format(year, term)
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["classroom_code", "number", "year", "term"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list

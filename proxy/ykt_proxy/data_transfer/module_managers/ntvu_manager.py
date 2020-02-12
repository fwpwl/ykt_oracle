# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR


def get_db_client():
    """

    """
    db_client = OracleTransferHandler(connect_str="usr_ykt/R4Odp0Vi@172.20.3.197:1521/jwxt")
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


def ntvu_get_department_data():
    statement = "select xymc from v_xyxxb"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", ]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def ntvu_get_tra_class_data():
    statement = "select ssxy, bjmc, rxxn, rxxq from v_xzbjb"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", 'name', 'year']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def ntvu_get_user_data():
    statement = "select ssxy, asxzbjmc, xm, xh, sf,rxxn from v_qtcyb"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "tra_class_name", 'name', 'number', 'user_type', 'year']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def ntvu_get_course_data(year='2019-2020', term='1'):
    statement = "select ssxy, kch, kcmc, kxh, kcbjmc, jsgh, kkxn, kkxq from v_bxqkkxxb where kkxn='{}' and kkxq='{}'".format(year, term)
    print(statement)

    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "course_code", "course_name", 'classroom_code', "classroom_name", "teacher_number",
                 "year", "term"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def ntvu_get_choose_data():
    statement = "select kxh, xh from v_bxqxksjb"

    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["classroom_code", "student_number"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list

# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR


def get_db_client():
    """

    """
    db_client = OracleTransferHandler(connect_str="zfykt_jk/zfykt_jk20191112@202.199.155.17:1521/orcl")
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


def dlu_get_department_data():
    statement = "select xymc from ykt_xyxx"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", ]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def dlu_get_tra_class_data():
    statement = "select xy, zy, xzb, nj from ykt_bjxx"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "major", 'name', 'year']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def dlu_get_user_data():
    statement = "select xy, xzb, xm, xh, sf, dqszj from ykt_xsjsxx"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "tra_class_name", 'name', 'number', 'user_type', 'year']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def dlu_get_course_data(year='2019-2020', term='1'):
    statement = "select kkxy, kcmc, kcdm, xkkh, bjmc, jszgh, jsxm,  xn, xq from ykt_kkxx where xn='{}' and xq='{}'".format(year, term)
    print(statement)

    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "course_name", "course_code", 'classroom_code', "classroom_name", "teacher_number",
                 "teacher_name", "year", "term"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def dlu_get_choose_data(year='2019-2020', term='1'):
    statement = "select xn,xq,xkkh,xh from ykt_xkxx where xn='{}' and xq='{}'".format(year, term)

    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["year", "term", "classroom_code", "student_number"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list

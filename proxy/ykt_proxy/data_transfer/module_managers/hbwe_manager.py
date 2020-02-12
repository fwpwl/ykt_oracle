# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR


def get_db_client():
    """

    """
    db_client = OracleTransferHandler(connect_str="kczx/kczx123@183.196.112.18:7000/ORCL")
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
def hbwe_get_student_data():
    statement = "select XY, XZB, XM,XH  from XS_KCZX"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "tra_class_name", 'name', 'number']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def hbwe_get_teacher_data():
    statement = "select BM, XM, ZGH  from JZG_KCZX"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", 'name', 'number']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def hbwe_get_course_data():
    statement = "select KCDM, KKJG from KC_KCZX "
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["course_code", 'department_name']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def hbwe_get_classroom_data(year='2019-2020', term='1'):
    statement = "select KCDM, KCMC, JSZGH, JSXM, KKKH, XN, XQ from KB_KCZX where XN='{}' and XQ='{}'".format(year, term)
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["course_code", 'course_name', 'teacher_number', "teacher_name", "classroom_code", "year", "term"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def hbwe_get_choose_data(year='2019-2020', term='1'):
    statement = "select XKKH, XH, XN, XQ from XSXK_KCZX where XN='{}' and XQ='{}'".format(year, term)
    print(statement)

    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["classroom_code", "student_number", 'year', 'term']
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list

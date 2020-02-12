# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR


def get_db_client():
    """

    """
    db_client = OracleTransferHandler(connect_str="JW_VIEW/jwview123@10.248.24.15:1521/hitszdb")
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


def hitsz_get_student_data():
    statement = "select YMC, BJMC, XM, XH, NJM from T_XJ_XSXXB"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "tra_class_name", 'name', 'number', 'year']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def hitsz_get_teacher_data():
    statement = "select GLYXMC, JSXM, ZGH from T_SZ_JSXXB"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", 'name', 'number']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def hitsz_get_course_data(year='2019-2020', term='1'):
    statement = "select KKYXMC, KCDM, KCMC, RWH,DGBJMC, DGJSDM, DGJSMC, XN, XQ from T_RW_RWAPB where XN='{}' and XQ='{}'".format(year, term)
    print(statement)

    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "course_code", "course_name", 'classroom_code', "classroom_name", "teacher_number",
                 "teacher_name", "year", "term"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def hitsz_get_choose_data(year='2019-2020', term='1'):
    statement = "select RWH, XH from T_XK_XSXKXXB where XN='{}' and XQ='{}'".format(year, term)

    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["classroom_code", "student_number"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list

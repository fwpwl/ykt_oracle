# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR


def get_db_client():
    """

    """
    db_client = OracleTransferHandler(connect_str="xj_yukt/xj_yukt@192.168.205.6:1521/jhpt")
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
def xijing_get_user_data():
    statement = "select XYMC, BJMC, XM, WYSBH, SF, RXXN from V_RYJBXX"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "tra_class_name", 'name', 'number', 'user_type', 'year']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def xijing_get_course_data(year=2019, term=1):
    statement = "select XYMC, KCDM, JXBH, JSGH, XM, KCMC, JXBMC, XN, XQ from V_KKXX where XN={} and XQ={}".format(year,
                                                                                                                  term)
    print(statement)

    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department", "course_code", 'classroom_code', "teacher_number", "teacher_name",
                 "course_name", "classroom_name", "year", 'term']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def xijing_get_choose_data(year_str='2019-2020-1'):
    statement = "select KCDM, XH, XN, JSGH, JXBH from V_XKXX where XN={}".format(year_str)
    print(statement)

    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["course_code", "student_number", 'year', 'teacher_number', 'classroom_code']
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list

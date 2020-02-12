# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR


def get_db_client():
    """
    
    """
    db_client = OracleTransferHandler(connect_str="usr_third/sdfithird@210.44.128.83:1521/urpdb")
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
def sdufe_get_department_data():
    statement = "select ID, DEPTNAME from TRA_DEPT"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "department_name"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def sdufe_get_tra_class_data():
    statement = "select BJDM, BJMC, NJ, YXSH from T_ZXBZ_XZB"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["tra_class_code", "tra_class_name", "year", "department_code"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def sdufe_get_student_data():
    statement = "select YXSH, BJDM ,XM, XH, XZNJ from V_YD_BZKS"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "tra_class_name", 'name', 'number', 'year']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def sdufe_get_teacher_data():
    statement = "select DWMC, ZGH, XM  from T_JZG"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", 'number', 'name']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def sdufe_get_course_data(year='2018-2019-2'):
    statement = "select KKXY, XKKH, JSZGH, JSXM, KCMC, BJMC, XNXQ from V_JSKCB where XNXQ='{}'".format(year)
    print(statement)

    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department", "classroom_code", "teacher_number", "teacher_name",
                 "course_name", "classroom_name", "year"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def sdufe_get_choose_data(year='2018-2019-2'):
    statement = "select XH, JXBH from T_BZKS_XSXK where NJYQ='{}'".format(year)
    print(statement)

    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["student_number", 'classroom_code']
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list

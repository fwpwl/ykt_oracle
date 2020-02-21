# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR


department_dict = {}

def get_db_client():
    """
    数据库连接
    """
    db_client = OracleTransferHandler(connect_str="JW_V_YKT/hit2020ykt@219.217.228.105:1521/hitdb1")
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


def hit_get_department_data():
    statement = "select YXDM, YXMC from xyxxb"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ['department_code', "department_name", ]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    for k in final_info_list:
        department_dict[k['department_code']] = k['department_name']
    return final_info_list

def hit_get_tra_data():
    hit_get_department_data()
    statement = "select GLYX, ZYMC, BJMC, NJ from xzbjb"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "major", 'tra_classroom_name', "year"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    for k in final_info_list:
        k['department_name'] = department_dict[k['department_code']]
    return final_info_list

def get_teacher_data():
    """
    教师表
    """
    hit_get_department_data()
    statement = "select XYDM, JSXM, ZGH from jsb"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", 'name', 'number']
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    for k in final_info_list:
        k['user_type'] = 2
        k['department_name'] = department_dict[k['department_code']]
        k['year'] = 0
    return final_info_list

def hit_get_user_data():
    hit_get_department_data()
    teacher_list = get_teacher_data()
    statement = "select GLYX, BJDM, XM, XH, NJ from xsb"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "tra_class_name", 'name', 'number', 'year']
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    for k in final_info_list:
        k['user_type'] = 3
        k['department_name'] = department[k['department_code']]
    return final_info_list + teacher_list

def hit_get_course_data(year, term):
    hit_get_department_data()
    statement = "select KKYX, KCDM, KCMC, RWH, DGJSDM, DGJSMC, XN, XQ from bxqkkxxb where XN='{}' and XQ='{}'".format(year, term)
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "course_code", "course_name", 'classroom_code', 
        "teacher_number", "teacher_name", "year", "term"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    for k in final_info_list:
        k['department_name'] = department_dict[k['department_code']]
    return final_info_list

def hit_get_choose_data(year, term):
    statement = "select RWH, XH from bxqxkxxb where XN='{}' and XQ='{}'".format(year, term)
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["classroom_code", "student_number"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

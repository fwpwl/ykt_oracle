# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR


def get_db_client():
    """
    数据库连接
    """
    db_client = OracleTransferHandler(connect_str="ykt/ykt@172.32.32.4:1521/orcl")
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


def get_department():
    department_dict = {}
    statement = "select xymc, DWH from LY_YKT_VIEW_XYXXB"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "ID"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    for k in final_info_list:
        department_dict[k['ID']] = k['department_name']
    return department_dict

def hnit_get_department_data():
    statement = "select xymc, DWH from LY_YKT_VIEW_XYXXB"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "ID"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

def hnit_get_tra_data():
    department_dict = get_department()
    statement = "select SSYX, ZY, BJMC, RXXN from LY_YKT_VIEW_XZBJB"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_id", "major", 'tra_classroom_name', "year"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    for k in final_info_list:
        if k['department_id'] == '99':
            continue
        k['department_name'] = department_dict[k['department_id']]
    return final_info_list

def hnit_get_user_data():
    department_dict = get_department()
    teachers = get_teacher_data()
    statement = "select SSXY, xzbjmc, XM, XH, sf, rxxn from LY_YKT_VIEW_XSYHXX"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_id", "tra_class_name", 'name', 'number', 'user_type', 'year']
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    for k in final_info_list + teachers:
        if k['department_id'] == '99':
            continue
        if not k['department_id']:
            k['department_name'] = None
        else:
            k['department_name'] = department_dict[k['department_id']]
    return final_info_list + teachers

def get_teacher_data():
    statement = "select SSXY, XM, XH, sf from LY_YKT_VIEW_JZGJBXX"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_id", 'name', 'number', 'user_type']
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    for k in final_info_list:
        k['tra_classroom_name'] = None
        k['year'] = 0
    return final_info_list

def hnit_get_course_data(year, term):
    department_dict = get_department()
    statement = "select SSXY, kch, kcmc, xkh, kcbjmc, jsgh, jsxm, KKXN, KKXQ from LY_YKT_VIEW_BXQKKXXB where KKXN='{}' and KKXQ='{}'".format(year, term)
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_id", "course_code", "course_name", 'classroom_code', "classroom_name", 
        "teacher_number", "teacher_name", "year", "term"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    for k in final_info_list:
        if k['department_id'] == '99':
            continue
        k['department_name'] = department_dict[k['department_id']]
    return final_info_list

def hnit_get_choose_data(year, term):
    statement = "select XKH, XH from LY_YKT_VIEW_BXQXKXXB where KKXN='{}' and KKXQ='{}'".format(year, term)
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["classroom_code", "student_number"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

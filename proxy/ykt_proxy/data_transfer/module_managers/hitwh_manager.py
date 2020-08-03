# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR


def get_db_client():
    db_client = OracleTransferHandler(connect_str="HITWH_YKT/hitwh#YKT#2020@172.26.24.24:1521/gxsjzx1")
    return db_client

def is_valid_request(key):
    if not key or key != cal_md5(get_now_datetime_str(FORMAT_DATE_WITHOUT_SEPARATOR)):
        return False
    return True

def query_data_to_dict_list(query_data_list_of_tuple, keys_list):
    final_list = []
    for tuple_item in query_data_list_of_tuple:
        tmp_dict = dict(zip(keys_list, tuple_item))
        final_list.append(tmp_dict)
    return final_list


def hitwh_get_department_data():
    statement = "select xsh, xymc from xyxxb"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "department_name"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

def get_department_data():
    department_dict = {}
    statement = "select xsh, xymc from xyxxb"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "department_name"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    for k in final_info_list:
        department_dict[k['department_code']] = k['department_name']
    return department_dict

def hitwh_get_tra_data():
    statement = "select XSM, ZYM, BJH, RXNJ from xzbjb"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "major", 'tra_classroom_name', "year"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

def hitwh_get_user_data():
    statement = "select SSXY, xzbjmc, XM, XH, sf, rxxn from qtcyb"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "tra_class_name", 'name', 'number', 'user_type', 'year']
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

def hitwh_get_course_data(year, term):
    department_dict = get_department_data()
    statement = "select KKXSH, kch, kcmc, xkh, kcbjmc, jsgh, jsxm, KKXN, KKXQ from bxqkkxxb where KKXN='{}' and KKXQ='{}'".format(year, term)
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "course_code", "course_name", 'classroom_code', "classroom_name", 
        "teacher_number", "teacher_name", "year", "term"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    for k in final_info_list:
        k['department_name'] = department_dict[k['department_code']]
    return final_info_list

def hitwh_get_choose_data(year, term):
    statement = "select XKH, XH from bxqxkxxb where KKXN='{}' and KKXQ='{}'".format(year, term)
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["classroom_code", "student_number"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

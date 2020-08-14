# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR


def get_db_client():
    """
    数据库连接
    """
    db_client = OracleTransferHandler(connect_str="sjzx/JwcQZ5270@211.70.149.150:1521/orcl")
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


def ahut_get_department_data():
    statement = "select xymc from Vykt_xyxxb"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", ]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

def ahut_get_tra_data():
    statement = "select ssxy, ZY, bjmc, RXXN from Vykt_xzbjb"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "major", 'tra_classroom_name', "year"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

def ahut_get_student_data():
    statement = "select YXMC, bjmc, XM, XH, RXNY from Vykt_xsjbxxb"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "tra_class_name", 'name', 'number', 'year']
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    for k in final_info_list:
        k['user_type'] = 3
    return final_info_list

def ahut_get_teacher_data():
    statement = "select DWMC, XM, JGH from Vykt_jzgxxb"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", 'name', 'number']
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    for k in final_info_list:
        k['user_type'] = 2
    return final_info_list

def ahut_get_user_data():
    return ahut_get_student_data() + ahut_get_teacher_data()

def ahut_get_course_data(year, term):
    statement = "select DWMC, KCDM, KCMC, XKKH, JSZGH, JSXM from Vykt_kkxx where KKXN='{}' and KKXQ='{}'".format(year, term)
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "course_code", "course_name", 'classroom_code', 
        "teacher_number", "teacher_name"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

def ahut_get_choose_data(year, term):
    statement = "select XKKH, XH from Vykt_xsxkxx where XN='{}' and XQ='{}'".format(year, term)
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["classroom_code", "student_number"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

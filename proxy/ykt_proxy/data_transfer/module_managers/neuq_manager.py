# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR


def get_db_client():
    """
    数据库连接
    """
    db_client = OracleTransferHandler(connect_str="ykt/ykt@202.206.20.173:1521/neuq")
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


def neuq_get_department_data():
    statement = "select jgmc from jgxx"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", ]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

def neuq_get_tra_data():
    statement = "select jgmc, zymc, bj, njdm from xzbxx"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "major", 'tra_classroom_name', "year"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list


def neuq_get_teacher_data():
    statement = "select jgmc, xm, jgh from jsjbxx"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", 'name', 'number']
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

def neuq_get_user_data():
    statement = "select jgmc, bj, XM, XH, rxxn from xsjbxx"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "tra_class_name", 'name', 'number', 'year']
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

def neuq_get_course_data(year, term):
    statement = "select jsbm, kch, kcmc, jxb_id, jxbmc, jgh, jsmc, xnmc, xqmc from kkxx where XNMC='{}' and XQMC='{}'".format(year, term)
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "course_code", "course_name", 'classroom_code', "classroom_name", 
        "teacher_number", "teacher_name", "year", "term"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

def neuq_get_choose_data(year, term):
    statement = "select jxb_id, XH from xsxkxx where XNMC='{}' and XQMC='{}'".format(year, term)
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["classroom_code", "student_number"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

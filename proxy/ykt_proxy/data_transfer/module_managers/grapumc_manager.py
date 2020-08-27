# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR


def get_db_client():
    """
    数据库连接
    """
    db_client = OracleTransferHandler(connect_str="graduate_view/kuz2GaFSRjMu@124.17.100.85:1521/gbk")
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


def grapumc_get_department_data():
    statement = "select DEPNAME from V_YXZYSZ"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

def grapumc_get_tra_data():
    statement = "select DEPNAME, MAJORNAME, MAJORNAME from V_YXZYSZ"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "major", 'tra_classroom_name']
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

def grapumc_get_student_data():
    statement = "select DEPNAME, REALNAME, USERNAME, GRADENAME, MAJORNAME from V_YJS"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", 'name', 'number', 'year', 'tra_class_name']
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    for k in final_info_list:
        k['user_typer'] = 3
    return final_info_list

def grapumc_get_teacher_data():
    statement = "select DEPNAME, REALNAME, USERNAME from V_JS"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", 'name', 'number']
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    for k in final_info_list:
        k['user_typer'] = 2
    return final_info_list

def grapumc_get_user_data():
    return grapumc_get_student_data() + grapumc_get_teacher_data()

def grapumc_get_course_data(year, term):
    if term == 1:
        term = "秋"
    elif term == 2:
        term = "春"
    statement = "select DEPNAME, PCOURSEID, COURSENAME, CSEQ, TEACHERNO, TEACHERNAME, YEAR, TERM from V_KKXX where YEAR='{}' and TERM='{}'".format(year, term)
    print(statement)
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "course_code", "course_name", 'classroom_code', 
        "teacher_number", "teacher_name", "year", "term"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

def grapumc_get_choose_data(year, term):
    if term == 1:
        term = "秋"
    elif term == 2:
        term = "春"
    statement = "select CSEQ, USERNAME, PCOURSEID from V_XK where YEAR='{}' and TERM='{}'".format(year, term)
    print(statement)
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["classroom_code", "student_number", "course_code"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR


def get_db_client():
    """

    """
    db_client = OracleTransferHandler(connect_str="ydlcykt/ydlcykt20191104@172.17.0.17:1521/orcl")
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
def tmucmc_verify_user_pwd(number, pwd):
    statement = "select swjw.des3('{}', a.username || '---' || a.id || '+++') from swjw.v_users a where a.username='{}'".format(number, pwd)
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["cal_pwd"]
    cal_pwd_list = query_data_to_dict_list(data_list, keys_list)

    real_pwd_statement = "select PASSWORD from swjw.v_users where username='{}'".format(number)
    data_list = get_db_client().get_raw_data_by_statement(statement=real_pwd_statement, var_tuple=None)
    keys_list = ["real_pwd"]
    real_pwd_list = query_data_to_dict_list(data_list, keys_list)
    result_list = [cal_pwd_list, real_pwd_list]
    print('*'*100)
    print(result_list)
    return result_list


def tmucmc_get_user_data():
    statement = "select SSXY, XZBJMC, XM, XH, SF, NJ from swjw.v_xxcyb"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "tra_class_name", 'name', 'number', 'user_type', 'year']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def tmucmc_get_teacher_data():
    statement = "select SSXY, JSGH, XM, SF from swjw.v_jscyb"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "teacher_number", 'teacher_name', 'user_type']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def tmucmc_get_course_data(year='2019-2020-1'):
    statement = "select KCMC, KCH, KXH, KCBJMC, JSGH,  SSXY, XNXQ from swjw.v_bxqkkxxb where XNXQ='{}'".format(year)
    print(statement)

    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["course_name", "course_code", 'classroom_code', "classroom_name", "teacher_number",
                 "department", "year"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def tmucmc_get_choose_data(year='2019-2020-1'):
    statement = "select KXH, XH, XNXQ from swjw.v_bxqxksjb where XNXQ='{}'".format(year)

    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["classroom_code", "student_number", "year"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list

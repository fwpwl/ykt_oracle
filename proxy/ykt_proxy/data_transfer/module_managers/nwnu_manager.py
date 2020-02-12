# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler


def query_data_to_dict_list(query_data_list_of_tuple, keys_list):
    final_list = []
    for tuple_item in query_data_list_of_tuple:
        tmp_dict = dict(zip(keys_list, tuple_item))
        final_list.append(tmp_dict)
    return final_list


def get_client(func):
    """
    """

    def wrapper():
        conn = OracleTransferHandler(connect_str="usr_nwnu_miduser/nwnu730000miduser@210.26.110.115:1521/db")
        return func(conn)

    return wrapper


@get_client
def nwnu_get_department_data(db):
    statement = "select DWH,  DWMC from T_SJZJ_YXSDWJBSJ"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "department_name"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list


@get_client
def nwnu_get_teacher_data(db):
    statement = "select DWH,  GH, XM , DQZTM from T_SJZJ_JZGJCSJ"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "teacher_number", "teacher_name", 'status']
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list


@get_client
def nwnu_get_course_choose_data(db):
    statement = "select KCKSDWH, KCH,KCMC ,JXBH ,JXBMC,KKXND, KKXQM, JSGH, JSXM, XH from T_XB_BKSJW_XSGRKB"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "course_code", "course_name", "classroom_code", "classroom_name", "year", "term",
                 "teacher_number", "teacher_name", 'student_number']
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list


@get_client
def nwnu_get_tra_classroom_data(db):
    statement = "select BH,  BJMC from T_SJZJ_BJSJ"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["tra_classroom_code", "classroom_name"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def nwnu_get_student_name_data(db):
    statement = "select XH, XM from T_SJZJ_XSJBSJ"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["student_number", "student_name"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def nwnu_get_student_data(db):
    statement = "select XH, SZBH, SZNJ, YXSH, XSDQZTM from T_SJZJ_XJJBSJ"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["student_number", "classroom_code", "year", "department_code", 'status']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list

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
        conn = OracleTransferHandler(connect_str="gzsf_jwgl/gzsf_jwgl123@192.168.0.94:1521/orcl")
        return func(conn)

    return wrapper


@get_client
def gznc_get_department_data(db):
    statement = "select XYDM, XYMC from XYXXB"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "department_name"]
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data


@get_client
def gznc_get_tra_classroom_data(db):
    statement = "select BJMC,  SSXY, RXXN from XZBJB"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["name", "department", 'year']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def gznc_get_student_data(db):
    statement = "select SSXY,  ZY,  XZBJMC, XH, XM, RXNF, ZXZT from QTCYB_STU"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department", "major", "tra_classroom", "number", 'name', 'year', 'status']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def gznc_get_teacher_data(db):
    statement = "select XYH,  GH,  XM from QTCYB_TEA"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "number", 'name']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def gznc_get_course_data(db):
    statement = "select KCH, KCMC, KXH, KCBJMC, JSGH, SSXY, KKXN, KKXQ, KKM from BXQKKXXB"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["course_code", "course_name", 'classroom_series_code', 'classroom_name',
                 'teacher_number', 'department', 'year', 'term', 'classroom_id']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def gznc_get_choose_data(db):
    statement = "select XH, KCH, KKM from BXQXKSJB"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["student_number", "course_code", 'classroom_id']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list

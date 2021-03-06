# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR


def is_valid_request(key):
    """

    """
    if key != cal_md5(get_now_datetime_str(FORMAT_DATE_WITHOUT_SEPARATOR)):
        return False
    return True


def query_data_to_dict_list(query_data_list_of_tuple, keys_list):
    final_list = []
    for tuple_item in query_data_list_of_tuple:
        tmp_dict = dict(zip(keys_list, tuple_item))
        final_list.append(tmp_dict)
    return final_list


def get_client():
    """
    """

    conn = OracleTransferHandler(connect_str="VIEW_RC/SDDXsjzx_RC@202.194.14.34:1521/orcl")
    return conn



def sdu_get_department_data():
    statement = "select DWH, DWMC from VIEW_ZJK.V_RC_XYXX"
    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "department_name"]
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data



def sdu_get_student_data():
    statement = "select XH, XM, DWMC, SF, RXXN, RXXQ, SZBH from VIEW_ZJK.V_RC_XSXX"
    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["number", "name", 'department_name', 'user_type', 'year', 'term',
                 'tra_class_name']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list



def sdu_get_teacher_data():
    statement = "select GH, XM, DWMC, SF from VIEW_ZJK.V_RC_JZGXX"
    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["number", "name", "department", "user_type"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


# -----------------------  选课 数据 -----------------------

def sdu_get_course_data():
    statement = "select KCH, KCMC, KXH, JSGH, DWMC, KKXND, KKXQ from VIEW_ZJK.V_RC_BXQKKXXB"

    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["course_code", "course_name", 'classroom_code', "teacher_number", "department", "year", "term"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list



def sdu_get_choose_data():
    statement = "select KXH, KCH, XH from VIEW_ZJK.V_RC_BXQXKSJB"

    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["classroom_code", "course_code", 'student_number']
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list

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
    conn = OracleTransferHandler(connect_str="HCXY_YKTZYB/HCXY_a123@10.10.16.199:1521/kfptdb")
    return conn


def hcnu_get_department_data():
    statement = "select DWDM, DWMC from usr_zsj.v_yktzyb_dwdm"
    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "department_name"]
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data



def hcnu_get_tradition_class_data():
    statement = "select XYMC, ZYMC, XZBJMC, RXNF from usr_zsj.v_yktzyb_bjdm"
    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "major", "tradition_classroom_name", 'year']
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data



def hcnu_get_student_data():
    statement = "select XYMC, XZBJMC, XM, XH, SF, RXXN, RXXQ from usr_zsj.v_yktzyb_xs"
    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ['department_name', 'tra_class_name', "name", "number", 'user_type', 'year', 'term']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list



def hcnu_get_teacher_data():
    statement = "select XYMC, XM, GH, SF from usr_zsj.v_yktzyb_jzg"
    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department", "name", "number", "user_type"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


# -----------------------  选课 数据 -----------------------

def hcnu_get_course_data():
    statement = "select XYMC, KKH, KXH, KKLSGH, KKLSXM, KCMC, KCBJM, KXXN, KXXQ from usr_zsj.v_yktzyb_KKB"

    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department", "course_code", 'classroom_code', "teacher_number", "teacher_name",
                 "course_name", "classroom_name", "year", "term"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list



def hcnu_get_choose_data():
    statement = "select KXH, XH from usr_zsj.v_yktzyb_xkxxb"

    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["classroom_code", 'student_number']
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list

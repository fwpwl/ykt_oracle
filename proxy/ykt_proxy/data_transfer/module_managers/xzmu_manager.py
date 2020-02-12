# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR


def get_db_client():
    """

    """
    db_client = OracleTransferHandler(connect_str="xcb_yiban/xcb_yiban@202.200.16.46:1521/ora")
    return db_client


def get_course_client():
    """

    """
    db_client = OracleTransferHandler(connect_str="drcom/drcom@202.200.16.42:1521/ora")
    return db_client


def is_valid_request(key):
    """

    """
    if not key or key != cal_md5(get_now_datetime_str(FORMAT_DATE_WITHOUT_SEPARATOR)):
        return False
    return True


def get_term_by_chinese_name(term_str):
    """

    """
    if not term_str:
        return ''
    if int(term_str) == 1:
        return '第一学期'
    elif int(term_str) == 2:
        return '第二学期'
    return ''


def query_data_to_dict_list(query_data_list_of_tuple, keys_list):
    final_list = []
    for tuple_item in query_data_list_of_tuple:
        tmp_dict = dict(zip(keys_list, tuple_item))
        final_list.append(tmp_dict)
    return final_list


# -----------------------  选课 数据 -----------------------
def xzmu_get_student_data():
    statement = "select XYMC, BJMC, XM, XH, NJ from xgb_zfxg.xx_v_yiban"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "tra_class_name", 'name', 'number', 'year']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def xzmu_get_teacher_data():
    statement = "select BMMC, XM, GH from rsc.v_z_teacher_yiban"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", 'name', 'number']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def xzmu_get_teacher_course_data(year=2019, term='1'):
    """

    """
    term = get_term_by_chinese_name(term)
    statement = "select XN,XQ, GH, JSXM, SKBJ, ZC, JC, DSZ, XQJ, KCMC, SKDD,KCDM, BJMC, KSDW from V_ly_kcb_js where XN='{}' and XQ='{}'".format(year, term)

    print(statement)

    data_list = get_course_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["year", 'term', "teacher_number", "teacher_name", 'classroom',
                 'zc', 'jc', 'dsz', 'xqj', 'course_name', 'site', 'course_code', 'classroom_name', 'department']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def xzmu_get_student_course_data(year=2019, term='1'):
    term = get_term_by_chinese_name(term)
    statement = "select XN, XQ, KCDM, KCMC, XH, JSGH, ZC, JC, SKDD, DSZ,BJMC, bjid  from V_ly_kcb_xs where XN='{}' and XQ='{}'".format(
        year, term)
    print(statement)

    data_list = get_course_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["year", "term", 'course_code', "course_name", "student_number", "teacher_number", 'week', 'jc',
                 'site', 'dsz', 'classroom_name', 'classroom']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list

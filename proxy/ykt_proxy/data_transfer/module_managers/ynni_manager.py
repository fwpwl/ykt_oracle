# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR


def get_db_client():
    """

    """
    db_client = OracleTransferHandler(connect_str="hikvision/Ykt@2019@192.168.10.103:1521/tymhdb")
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
def ynni_get_tra_class_data():
    statement = "select ssxymc, bjmc, jsgh, jsjs, xw, bjrxnf, bjrxq from v_xzbjsj"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "tradition_class_name", 'teacher_number', 'role', 'grade', 'join_year', 'join_term']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def ynni_get_user_data():
    statement = "select xm, xgh, rxnf, rxxq, ssxy, bjmc, sf from v_qtrysj"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["name", "number", 'join_year', 'term', 'department_name', 'tradition_class_name', 'user_type']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def ynni_get_teacher_data():
    statement = "select xm, gh, lxrq, dwh, dwmc from dbm.v_js_jcsj"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["name", "number", 'join_year', 'department_code', 'department_name']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def ynni_get_course_data(year='2019', term='1'):
    statement = "select kcmc, kch, kxh, kcbjm, kcssyx, jsgh, kkxn, kkxq, sksj from v_kcjbsj where kkxn='{}' and kkxq='{}'".format(
        year, term)
    print(statement)

    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["course_name", "course_code", 'classroom_code', "classroom_name", "department_name",
                 "teacher_number", "start_year", "start_term", "classroom_time"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def ynni_get_choose_data(year='2019', term='1'):
    statement = "select a.kxh, a.xh from v_xksj a, v_kcjbsj b where a.kxh=b.kxh and b.kkxn='{}' and b.kkxq='{}'".format(
        year, term)

    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["classroom_code", "number"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list

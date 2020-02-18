# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR


def get_db_client():
    """
    """
    db_client = OracleTransferHandler(connect_str="usr_third/sdadathird@172.16.85.12:1521/urpdb")
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

def get_department_data():
    statement = "select mc,dm from v_dw"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "department_code"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    department_dict = {}
    for k in final_info_list:
        department_dict[k['department_code']] = k['department_name']
    return department_dict

def get_class_data():
    statement = "select bjdm, bjmc from v_bj"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["bjdm", "bjmc"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    class_dict = {}
    for k in final_info_list:
        class_dict[k['bjdm']] = k['bjmc']
    return class_dict

def get_zy_data():
    statement = "select zydm, zymc from v_zy"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["zydm", "zymc"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    class_dict = {}
    for k in final_info_list:
        class_dict[k['zydm']] = k['zymc']
    return class_dict

def sdada_get_department_data():
    statement = "select mc,dm from v_dw"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "department_code"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

def sdada_get_tra_data():
    zy = get_zy_data()
    department = get_department_data()
    statement = "select Yxsh, Zydm, bjmc, Nj from v_bj"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "major", 'tra_classroom_name', "year"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    for k in final_info_list:
        k['major'] = zy[k['major']]
        try:
            k['department_name'] = department[k['department_name']]
        except:
            pass
    return final_info_list


def sdada_get_student_data():
    # 学院代码  班级代码 
    department = get_department_data()
    class_dict = get_class_data()
    gra_student = sdada_get_gra_student_data()
    teacher_list = sdada_get_teacher_data()
    statement = "select YXSH, BJDM, XM, XH, XZNJ from v_bzks"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "tra_class_name", 'name', 'number', 'year']
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    for k in final_info_list:
        k['department_name'] = department[k['department_name']]
        k['tra_class_name'] = class_dict[k['tra_class_name']]
        k['user_type'] = 3
    return final_info_list + teacher_list


def sdada_get_gra_student_data():
    # 学院代码  班级代码 
    class_dict = get_class_data()
    statement = "select YXSH, BJDM, XM, XH, XZNJ from v_yjs"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "tra_class_name", 'name', 'number', 'year']
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    for k in final_info_list:
        k['tra_class_name'] = class_dict[k['tra_class_name']]
        k['user_type'] = 3
    return final_info_list


def sdada_get_teacher_data():
    """
    ryzt: 1=在职
    """
    statement = "select DWMC, XM, ZGH from v_jzg where Ryzt=1"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", 'name', 'number']
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    for k in final_info_list:
        k['user_type'] = 2
    return final_info_list


def sdada_get_course_data(year_term):
    """
    jx0404id: 教学班
    Jxbid： 行政班id
    """
    statement = "select jxbid, Kch, Kcm, jx0404id, ktmc, Bh, Xm, Xnxqdm from v_it_kcb_kcbxx where Xnxqdm='{}'".format(year_term)

    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["jxbid", "course_code", "course_name", 'classroom_code', "classroom_name", "teacher_number",
                 "teacher_name", "year_term"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    # for k in final_info_list:
    #     k['department_name'] = 
    return final_info_list



def sdada_get_choose_data(year_term):
    """

    """
    statement = "select jx0404id, XH from v_it_kcb_xxkb where Xnxq='{}'".format(year_term)
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["classroom_code", "student_number"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR


def get_db_client():
    """

    """
    db_client = OracleTransferHandler(connect_str="edudata_out_ykt/jwc*^72$@8+9)2#*59@172.16.47.251:1433/edumis")
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
def ecjtu_get_student_data():
    statement = "select Name, StudentID, ClassName, DepartMent from V_Out_StudentInfo"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["name", "number", "tradition_classroom_name", "department"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def ecjtu_get_teacher_data():
    statement = "select TeacherID, Name, DepartmentID from V_Out_TeacherInfo"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["teacher_number", "teacher_name", "department_id"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def ecjtu_get_teacher_choose():
    statement = "select TeachTaskID, TeacherID, TeachType from V_Out_TeachTaskTeacher"
    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["classroom_code", "teacher_number", "teacher_type"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def ecjtu_get_course_data(term='2018.2'):
    statement = "select TeachTaskID, Term, CourseID, PriDepart, TeachClassCaption, UniteClass from V_Out_TeachTask".format(
        term)
    print(statement)

    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["classroom_code", "term", "course_code", "department_name", "course_name", "classroom_name"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def ecjtu_student_choose(year_str='2018.2'):
    statement = "select TeachTaskID, StudentID, Term from V_Out_TeachTaskStudent WHERE Term = {}".format(year_str)
    print(statement)

    data_list = get_db_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["classroom_code", "student_number", 'term']
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list

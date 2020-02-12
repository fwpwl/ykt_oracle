# coding: utf-8

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
        conn = OracleTransferHandler(connect_str="usr_third/Wisedu#2020@10.99.5.103:1521:usr_zsj")
        return func(conn)

    return wrapper


@get_client
def sdcit_get_department_info_data(cursor):
    statement = "select xymc from usr_zsj.v_xszx_dw"

    data_list = cursor.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def sdcit_get_tradition_class_info(cursor):
    statement = "select ssxy, zy, bjmc, rxxn from usr_zsj.v_xszx_xzb"

    data_list = cursor.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "zy", "tradition_class_name", "year"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def sdcit_get_user_info(cursor):
    keys_list = ["number", "name", "year", 'department_code',
                 'tra_class_code', "user_type"]
    student_statement = "select xh, xm, rxxn, ssxy, xzbjmc, sf from usr_zsj.v_xszx_xsjbxx"
    student_data_list = cursor.get_raw_data_by_statement(statement=student_statement, var_tuple=None)
    student_list = query_data_to_dict_list(student_data_list, keys_list)
    teacher_statement = "select xh, xm, rxxn, ssxy, xzbjmc, sf from usr_zsj.v_xszx_jzgjbxx"
    teacher_data_list = cursor.get_raw_data_by_statement(statement=teacher_statement, var_tuple=None)
    teacher_list = query_data_to_dict_list(teacher_data_list, keys_list)
    final_info_list = student_list + teacher_list
    return final_info_list


@get_client
def sdcit_get_course_info(cursor):
    """

    """
    statement = "select kch, kcmc, kcbjmc, ssxy, kkxn, kkxq, jsgh, jsxm, xkh from usr_zsj.v_xszx_kkxx"

    data_list = cursor.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["course_code", "course_name", "classroom_name", "department_code",
                 "year", 'term', 'teacher_number', 'teacher_name', 'classroom_code']
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def sdcit_get_choose_info(cursor):
    """

    """
    statement = "select xh, xkh, kkxn, kkxq from usr_zsj.v_xszx_xsxk"

    data_list = cursor.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["student_number", "course_code", "year", "term"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list

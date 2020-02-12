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
        conn = OracleTransferHandler(connect_str="usr_yuketang/Cidp#2019@10.159.241.4:1521/KFPTDB")
        return func(conn)

    return wrapper


@get_client
def cidp_get_department_info_data(cursor):
    statement = "select XYDM, XYMC  from USR_YUKETANG.XYXXB"

    data_list = cursor.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "department_name"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def cidp_get_tradition_class_info(cursor):
    statement = "select BJDM, BJMC, SSXY, NJ from USR_YUKETANG.XZBJB"

    data_list = cursor.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["tradition_class_code", "tradition_class_name", "department_code", "year", ]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def cidp_get_user_info(cursor):
    """

    """
    statement = "select XH, XM, XZNJ, SSXY, BJDM, SF from USR_YUKETANG.QTCYB"

    data_list = cursor.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["number", "name", "year", 'department_code',
                 'tra_class_code', "user_type"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def cidp_get_course_info(cursor):
    """

    """
    statement = "select KCH, KEMC, JXBID, KKDW, KKXN, KKXQ, JSGH, JIAOSHIMINGCHEN, " \
                "JIAOXUEFANGSHI, KEXUHAO from USR_YUKETANG.BXQKKXXB"

    data_list = cursor.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["course_code", "course_name", "classroom_name", "department_code",
                 "year", 'term', 'teacher_number', 'teacher_name', 'classroom_type',
                 'classroom_series_code']
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def cidp_get_choose_info(cursor):
    """

    """
    statement = "select XH, KECHENGHAO, JXBID from USR_YUKETANG.BXQXKSJB"

    data_list = cursor.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["student_number", "course_code", "classroom_name"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list

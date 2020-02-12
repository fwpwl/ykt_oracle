# coding: utf-8
"""
中国医科大学
"""
import cx_Oracle


def query_data_to_dict_list(query_data_list_of_tuple, keys_list):
    final_list = []
    for tuple_item in query_data_list_of_tuple:
        tmp_dict = dict(zip(keys_list, tuple_item))
        final_list.append(tmp_dict)
    return final_list


def get_raw_data_by_statement(statement, var_tuple):
    conn = cx_Oracle.connect(
        "icdc_yuketang/icdc_2iu1xvfB@192.168.199.81:1521/icdc", encoding="UTF-8",
        nencoding="UTF-8"
    )
    cursor = conn.cursor()
    if var_tuple:
        cursor.execute(statement, var_tuple)
    else:
        cursor.execute(statement)
    data_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return data_list


def get_department_data(*args, **kwargs):
    """
    院系
    """
    sql = "select XYID, XYMC  from cmu_views.yukt_xyxxb"

    qs_cursor = get_raw_data_by_statement(statement=sql, var_tuple=None)
    keys_list = ("department_code", "department_name")

    final_info_list = query_data_to_dict_list(qs_cursor, keys_list)

    return final_info_list


def get_tra_classroom_data(*args, **kwargs):
    """
    行政班数据
    """
    sql = "select SSXY, ZY, BJMC, RXXN from cmu_views.yukt_xzbjb"
    qs_cursor = get_raw_data_by_statement(statement=sql, var_tuple=None)
    keys_list = ("department_name", "specialty_name", "tradition_class_name", "year")
    classroom_list = query_data_to_dict_list(qs_cursor, keys_list)

    return classroom_list


def get_user_data(*args, **kwargs):
    """
    用户信息
    """
    sql = "select SSXY, XZBJMC, XM, XH, RXXN, SF from cmu_views.yukt_qtcyb"
    qs_cursor = get_raw_data_by_statement(statement=sql, var_tuple=None)
    keys_list = ("department_name", "tradition_class_name", "name", "number", "year", "user_type")

    user_list = query_data_to_dict_list(qs_cursor, keys_list)
    return user_list


def get_course_data(year="2019-2020", term=1, *args, **kwargs):
    """
    老师开课课程信息
    """
    sql = """
        select SSXY, KCBJMC, KCMC, KCH, XKH, JSGH, JSXM, KKXN, KKXQ
        from cmu_views.yukt_bxqkkxxb
        where KKXN=:1 and KKXQ=:2
        """

    qs_cursor = get_raw_data_by_statement(statement=sql, var_tuple=(year, term))
    keys_list = ("department_name", "classroom_name", "course_name", "course_code",
                 "classroom_code", "teacher_number", "teacher_name", "year", "term")
    course_list = query_data_to_dict_list(qs_cursor, keys_list)

    return course_list


def get_choose_data(year="2019-2020", term=1, *args, **kwargs):
    """
    学生选课
    """
    sql = "select XKH, XH, KKXN, KKXQ from cmu_views.yukt_bxqxkxxb where KKXN=:1 and KKXQ=:2"

    qs_cursor = get_raw_data_by_statement(statement=sql, var_tuple=(year, term))
    keys_list = ("classroom_code", "student_number", "year", 'term')
    final_info_list = query_data_to_dict_list(qs_cursor, keys_list)

    return final_info_list

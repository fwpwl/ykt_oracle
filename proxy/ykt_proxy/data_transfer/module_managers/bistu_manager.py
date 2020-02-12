# coding: utf-8
"""
北京信息科技大学
"""
import cx_Oracle


def query_data_to_dict_list(query_data_list_of_tuple, keys_list):
    final_list = []
    for tuple_item in query_data_list_of_tuple:
        tmp_dict = dict(zip(keys_list, tuple_item))
        final_list.append(tmp_dict)
    return final_list


def get_raw_data_by_statement(statement, var_tuple):
    conn = cx_Oracle.connect("fy_user_chaoxing/IxiTI4FrmYAz@10.1.100.148:1521/orcl")
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
    statement = "select XYDM, XYMC  from xydmb"

    data_list = get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ("department_code", "department_name")

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def get_tra_classroom_data(*args, **kwargs):
    """
    行政班数据
    """
    sql = "select BJDM, BJMC, SSXYDM, SSZYDM, NJ from bjdmb"
    # 专业
    specialty_sql = "select ZYDM, ZYMC from zydmb"
    specialty_data = get_raw_data_by_statement(statement=specialty_sql, var_tuple=None)
    specialty_map = {r[0]: r[1] for r in specialty_data}

    data_list = get_raw_data_by_statement(statement=sql, var_tuple=None)
    classroom_list = []
    for item in data_list:
        classroom_list.append({
            "tradition_class_code": item[0],
            "tradition_class_name": item[1],
            "department_code": item[2],
            "specialty_code": item[3],
            "specialty_name": specialty_map.get(item[3], ""),
            "year": item[4]
        })

    return classroom_list


def get_user_data(*args, **kwargs):
    """
    用户信息
    """
    teacher_sql = "select ZGH, XM, XB, BM from jsxxb"
    teacher_cursor = get_raw_data_by_statement(statement=teacher_sql, var_tuple=None)
    user_list = []
    for tuple_item in teacher_cursor:
        user_list.append(dict(
            number=tuple_item[0],
            name=tuple_item[1],
            sex=tuple_item[2],
            department_name=tuple_item[3],
            specialty_name="",
            tradition_class_name="",
            user_type=2,
            year=None
        ))

    student_sql = "select XH, XM, XB, XY, ZYMC, XZB, DQSZJ from xsjbxxb"
    student_cursor = get_raw_data_by_statement(statement=student_sql, var_tuple=None)
    for tuple_item in student_cursor:
        user_list.append(dict(
            number=tuple_item[0],
            name=tuple_item[1],
            sex=tuple_item[2],
            department_name=tuple_item[3],
            specialty_name=tuple_item[4],
            tradition_class_name=tuple_item[5],
            user_type=3,
            year=tuple_item[6]
        ))

    return user_list


def get_course_data(year="2019-2020", term=1, *args, **kwargs):
    """
    老师开课课程信息
    """
    sql = """
        select JXJHH, XN, XQ, KCDM, KCMC, KKXY, JSZGH, JSXM, XKKH, BJMC, JXBMC 
        from jxrwb
        where XN=:1 and XQ=:2
        """

    data_list = get_raw_data_by_statement(statement=sql, var_tuple=(year, term))
    course_list = []
    for item in data_list:
        jxbmc = item[10] if item[10] and item[10] not in ("无", "???") else ""
        if item[9] and item[9] not in ("无", "???"):
            classroom_name = "%s-%s" % (item[9], item[0])
        elif jxbmc:
            classroom_name = "%s-%s" % (jxbmc, item[0])
        else:
            classroom_name = "%s-%s" % (item[4], item[0])

        course_list.append({
            "year": item[1],
            'term': item[2],
            "course_code": item[3],
            "course_name": item[4],
            "department_name": item[5],
            "teacher_number": item[6],
            "teacher_name": item[7],
            "classroom_code": item[8],
            "classroom_name": classroom_name
        })

    return course_list


def get_choose_data(year="2019-2020", term=1, *args, **kwargs):
    """
    学生选课
    """
    sql = "select XN, XQ, XKKH, XH from xsxkbn where XN=:1 and XQ=:2"

    data_list = get_raw_data_by_statement(statement=sql, var_tuple=(year, term))
    keys_list = ("year", 'term', "classroom_code", "student_number")
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list

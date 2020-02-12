# coding:utf-8

from data_transfer.module_managers.nwnu_manager import nwnu_get_department_data, nwnu_get_teacher_data, \
    nwnu_get_course_choose_data, nwnu_get_tra_classroom_data, nwnu_get_student_data, nwnu_get_student_name_data
from data_transfer.utils.network import json_http_response


def nwnu_get_department_data_view(request):
    """
    URL[GET]:/data/nwnu/get_department_data/
    """
    try:
        ret_data = nwnu_get_department_data()
        result_dict = {
            "success": True,
            "msg": "",
            "data": ret_data
        }
    except Exception as e:
        result_dict = {
            "success": False,
            "msg": str(e),
            "data": {}
        }

    return json_http_response(result_dict)


def nwnu_get_teacher_data_view(request):
    """
    URL[GET]:/data/nwnu/get_teacher_data/
    """
    try:
        ret_data = nwnu_get_teacher_data()
        result_dict = {
            "success": True,
            "msg": "",
            "data": ret_data
        }
    except Exception as e:
        result_dict = {
            "success": False,
            "msg": str(e),
            "data": {}
        }

    return json_http_response(result_dict)


def nwnu_get_course_data_view(request):
    """
    URL[GET]:/data/nwnu/get_course_data/
    """
    try:
        ret_data = nwnu_get_course_choose_data()
        result_dict = {
            "success": True,
            "msg": "",
            "data": ret_data
        }
    except Exception as e:
        result_dict = {
            "success": False,
            "msg": str(e),
            "data": {}
        }

    return json_http_response(result_dict)


def nwnu_get_tra_classroom_data_view(request):
    """
    URL[GET]:/data/nwnu/get_tra_classroom_data/
    """
    try:
        ret_data = nwnu_get_tra_classroom_data()
        result_dict = {
            "success": True,
            "msg": "",
            "data": ret_data
        }
    except Exception as e:
        result_dict = {
            "success": False,
            "msg": str(e),
            "data": {}
        }

    return json_http_response(result_dict)


def nwnu_get_student_name_data_view(request):
    """
    URL[GET]:/data/nwnu/get_student_name_data/
    """
    try:
        ret_data = nwnu_get_student_name_data()
        result_dict = {
            "success": True,
            "msg": "",
            "data": ret_data
        }
    except Exception as e:
        result_dict = {
            "success": False,
            "msg": str(e),
            "data": {}
        }

    return json_http_response(result_dict)


def nwnu_get_student_data_view(request):
    """
    URL[GET]:/data/nwnu/get_student_data/
    """
    try:
        ret_data = nwnu_get_student_data()
        result_dict = {
            "success": True,
            "msg": "",
            "data": ret_data
        }
    except Exception as e:
        result_dict = {
            "success": False,
            "msg": str(e),
            "data": {}
        }

    return json_http_response(result_dict)

# coding:utf-8
from data_transfer.module_managers.ecjtu_manager import ecjtu_get_student_data, ecjtu_get_teacher_data, \
    ecjtu_get_teacher_choose, ecjtu_get_course_data, ecjtu_student_choose
from data_transfer.utils.network import json_http_response, get_para_from_request_safe


def ecjtu_get_student_data_view(request):
    """
    URL[GET]:/data/ecjtu/get_student_data/
    """
    try:
        ret_data = ecjtu_get_student_data()
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


def ecjtu_get_teacher_data_view(request):
    """
    URL[GET]:/data/ecjtu/get_teacher_data/
    """
    try:
        ret_data = ecjtu_get_teacher_data()
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


def ecjtu_get_course_data_view(request):
    """
    URL[GET]:/data/ecjtu/get_course_data/
    """
    try:
        term = get_para_from_request_safe(request, 'term', '2018.2')
        ret_data = ecjtu_get_course_data(term)
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


def ecjtu_get_student_choose_data_view(request):
    """
    URL[GET]:/data/ecjtu/get_student_choose_data/
    """
    try:
        term = get_para_from_request_safe(request, 'term', '2018.2')
        ret_data = ecjtu_student_choose(term)
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


def ecjtu_get_teacher_choose_data_view(request):
    """
    URL[GET]:/data/ecjtu/get_teacher_choose_data/
    """
    try:
        ret_data = ecjtu_get_teacher_choose()
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

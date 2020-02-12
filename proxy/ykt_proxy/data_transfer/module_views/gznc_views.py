# coding:utf-8
from data_transfer.module_managers.gznc_manager import gznc_get_department_data, gznc_get_tra_classroom_data, \
    gznc_get_student_data, gznc_get_teacher_data, gznc_get_course_data, gznc_get_choose_data
from data_transfer.utils.network import json_http_response


def gznc_get_department_data_view(request):
    """
    URL[GET]:/data/gznc/get_department_data/
    """
    ret_data = gznc_get_department_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)


def gznc_get_tra_classroom_data_view(request):
    """
    URL[GET]:/data/gznc/get_tra_classroom_data/
    """
    ret_data = gznc_get_tra_classroom_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)


def gznc_get_student_data_view(request):
    """
    URL[GET]:/data/gznc/get_student_data/
    """
    ret_data = gznc_get_student_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)


def gznc_get_teacher_data_view(request):
    """
    URL[GET]:/data/gznc/get_teacher_data/
    """
    ret_data = gznc_get_teacher_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)


def gznc_get_course_data_view(request):
    """
    URL[GET]:/data/gznc/get_course_data_view/
    """
    ret_data = gznc_get_course_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)


def gznc_get_choose_data_view(request):
    """
    URL[GET]:/data/gznc/get_choose_data_view/
    """
    ret_data = gznc_get_choose_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)

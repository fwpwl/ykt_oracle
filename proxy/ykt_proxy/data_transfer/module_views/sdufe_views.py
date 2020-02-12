# coding:utf-8
from data_transfer.module_managers.sdufe_manager import sdufe_get_department_data, sdufe_get_tra_class_data, \
    sdufe_get_student_data, sdufe_get_teacher_data, sdufe_get_course_data, sdufe_get_choose_data, is_valid_request
from data_transfer.utils.network import json_http_response, get_para_from_request_safe, error_response


def sdufe_get_department_data_view(request):
    """
    URL[GET]:/data/sdufe/sdufe_get_department_data/

    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = sdufe_get_department_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)


def sdufe_get_tra_class_data_view(request):
    """
    URL[GET]:/data/sdufe/sdufe_get_tra_class_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = sdufe_get_tra_class_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)


def sdufe_get_student_data_view(request):
    """
    URL[GET]:/data/sdufe/sdufe_get_student_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = sdufe_get_student_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)


def sdufe_get_teacher_data_view(request):
    """
    URL[GET]:/data/sdufe/sdufe_get_teacher_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = sdufe_get_teacher_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)


def sdufe_get_course_data_view(request):
    """
    URL[GET]:/data/sdufe/sdufe_get_course_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    year = get_para_from_request_safe(request, 'year')

    ret_data = sdufe_get_course_data(year)
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)


def sdufe_get_choose_data_view(request):
    """
    URL[GET]:/data/sdufe/sdufe_get_choose_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    year = get_para_from_request_safe(request, 'year')
    ret_data = sdufe_get_choose_data(year)
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)

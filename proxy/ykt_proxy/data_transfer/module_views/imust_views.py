# coding:utf-8

from data_transfer.module_managers.imust_manager import imust_get_course_data, imust_get_choose_data, \
    is_valid_request, imust_get_student_data, imust_get_teacher_data
from data_transfer.utils.network import success_response, get_para_from_request_safe, error_response


def imust_get_student_data_view(request):
    """
    URL[GET]:/data/imust/get_student_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = imust_get_student_data()
    return success_response(ret_data)


def imust_get_teacher_data_view(request):
    """
    URL[GET]:/data/imust/get_teacher_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = imust_get_teacher_data()
    return success_response(ret_data)


def imust_get_course_data_view(request):
    """
    URL[GET]:/data/imust/get_course_data/
    PARA:
    key
    year
    term
    """
    key = get_para_from_request_safe(request, 'key')
    year = get_para_from_request_safe(request, 'year')
    term = get_para_from_request_safe(request, 'term')

    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = imust_get_course_data(year, term)
    return success_response(ret_data)


def imust_get_choose_data_view(request):
    """
    URL[GET]:/data/imust/get_choose_data/
    PARA:
    key
    year_str
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    year = get_para_from_request_safe(request, 'year')
    term = get_para_from_request_safe(request, 'term')

    ret_data = imust_get_choose_data(year, term)
    return success_response(ret_data)

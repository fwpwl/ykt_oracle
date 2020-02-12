# coding:utf-8

from data_transfer.module_managers.hitsz_manager import hitsz_get_course_data, hitsz_get_choose_data, \
    is_valid_request, hitsz_get_student_data, hitsz_get_teacher_data
from data_transfer.utils.network import success_response, get_para_from_request_safe, error_response


def hitsz_get_student_data_view(request):
    """
    URL[GET]:/data/hitsz/get_student_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = hitsz_get_student_data()
    return success_response(ret_data)


def hitsz_get_teacher_data_view(request):
    """
    URL[GET]:/data/hitsz/get_teacher_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = hitsz_get_teacher_data()
    return success_response(ret_data)


def hitsz_get_course_data_view(request):
    """
    URL[GET]:/data/hitsz/get_course_data/
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

    ret_data = hitsz_get_course_data(year, term)
    return success_response(ret_data)


def hitsz_get_choose_data_view(request):
    """
    URL[GET]:/data/hitsz/get_choose_data/
    PARA:
    key
    year_str
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    year = get_para_from_request_safe(request, 'year')
    term = get_para_from_request_safe(request, 'term')

    ret_data = hitsz_get_choose_data(year, term)
    return success_response(ret_data)

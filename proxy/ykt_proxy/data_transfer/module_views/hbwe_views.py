# coding:utf-8
from data_transfer.module_managers.hbwe_manager import hbwe_get_student_data, hbwe_get_teacher_data, \
    hbwe_get_course_data, hbwe_get_choose_data, hbwe_get_classroom_data
from data_transfer.module_managers.hbwe_manager import is_valid_request
from data_transfer.utils.network import success_response, get_para_from_request_safe, error_response


def hbwe_get_student_data_view(request):
    """
    URL[GET]:/data/hbwe/hbwe_get_student_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = hbwe_get_student_data()
    return success_response(ret_data)


def hbwe_get_teacher_data_view(request):
    """
    URL[GET]:/data/hbwe/hbwe_get_teacher_data/
    PARA:
    key
    year
    term
    """
    key = get_para_from_request_safe(request, 'key')

    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = hbwe_get_teacher_data()
    return success_response(ret_data)


def hbwe_get_course_data_view(request):
    """
    URL[GET]:/data/hbwe/hbwe_get_course_data/
    PARA:
    key
    year_str
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = hbwe_get_course_data()
    return success_response(ret_data)


def hbwe_get_classroom_data_view(request):
    """
    URL[GET]:/data/hbwe/hbwe_get_classroom_data/
    PARA:
    key
    year_str
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    year = get_para_from_request_safe(request, 'year')
    term = get_para_from_request_safe(request, 'term')

    ret_data = hbwe_get_classroom_data(year, term)
    return success_response(ret_data)


def hbwe_get_choose_data_view(request):
    """
    URL[GET]:/data/hbwe/hbwe_get_choose_data/
    PARA:
    key
    year_str
    """
    key = get_para_from_request_safe(request, 'key')
    year_str = get_para_from_request_safe(request, 'year_str')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    year = get_para_from_request_safe(request, 'year')
    term = get_para_from_request_safe(request, 'term')
    ret_data = hbwe_get_choose_data(year, term)
    return success_response(ret_data)

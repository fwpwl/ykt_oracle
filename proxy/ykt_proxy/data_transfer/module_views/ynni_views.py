# coding:utf-8

from data_transfer.module_managers.ynni_manager import ynni_get_course_data, ynni_get_choose_data, \
    is_valid_request, ynni_get_user_data, ynni_get_teacher_data, ynni_get_tra_class_data
from data_transfer.utils.network import success_response, get_para_from_request_safe, error_response


def ynni_get_tra_class_data_view(request):
    """
    URL[GET]:/data/ynni/get_tra_class_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = ynni_get_tra_class_data()
    return success_response(ret_data)


def ynni_get_user_data_view(request):
    """
    URL[GET]:/data/ynni/get_user_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = ynni_get_user_data()
    return success_response(ret_data)


def ynni_get_teacher_data_view(request):
    """
    URL[GET]:/data/ynni/get_user_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = ynni_get_teacher_data()
    return success_response(ret_data)


def ynni_get_course_data_view(request):
    """
    URL[GET]:/data/ynni/get_course_data/
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

    ret_data = ynni_get_course_data(year, term)
    return success_response(ret_data)


def ynni_get_choose_data_view(request):
    """
    URL[GET]:/data/ynni/get_choose_data/
    PARA:
    key
    year_str
    """
    year = get_para_from_request_safe(request, 'year')
    term = get_para_from_request_safe(request, 'term')
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = ynni_get_choose_data(year, term)
    return success_response(ret_data)

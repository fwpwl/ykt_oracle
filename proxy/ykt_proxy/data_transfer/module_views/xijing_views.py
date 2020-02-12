# coding:utf-8

from data_transfer.module_managers.xijing_manager import xijing_get_course_data, xijing_get_choose_data, \
    is_valid_request, xijing_get_user_data
from data_transfer.utils.network import success_response, get_para_from_request_safe, error_response


def xijing_get_user_data_view(request):
    """
    URL[GET]:/data/xijing/get_user_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = xijing_get_user_data()
    return success_response(ret_data)


def xijing_get_course_data_view(request):
    """
    URL[GET]:/data/xijing/get_course_data/
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

    ret_data = xijing_get_course_data(year, term)
    return success_response(ret_data)


def xijing_get_choose_data_view(request):
    """
    URL[GET]:/data/xijing/get_choose_data/
    PARA:
    key
    year_str
    """
    key = get_para_from_request_safe(request, 'key')
    year_str = get_para_from_request_safe(request, 'year_str')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = xijing_get_choose_data(year_str)
    return success_response(ret_data)

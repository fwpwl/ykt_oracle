# coding:utf-8
from data_transfer.module_managers.tczyxy_manager import is_valid_request, tczyxy_get_user_data, tczyxy_get_course_data, \
    tczyxy_get_choose_data
from data_transfer.utils.network import success_response, get_para_from_request_safe, error_response


def tczyxy_get_user_view(request):
    """
    URL[GET]:/data/tczyxy/get_user/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = tczyxy_get_user_data()
    return success_response(ret_data)


def tczyxy_get_course_view(request):
    """
    URL[GET]:/data/tczyxy/get_course/
    """
    key = get_para_from_request_safe(request, 'key')
    year = get_para_from_request_safe(request, 'year')
    term = get_para_from_request_safe(request, 'term')

    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = tczyxy_get_course_data(year, term)
    return success_response(ret_data)


def tczyxy_get_choose_view(request):
    """
    URL[GET]:/data/tczyxy/get_choose/
    PARA:
    key
    year
    term
    """
    key = get_para_from_request_safe(request, 'key')

    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = tczyxy_get_choose_data()
    return success_response(ret_data)

# coding:utf-8

from data_transfer.module_managers.tijmu_manager import tijmu_get_course_data, tijmu_get_choose_data, \
    is_valid_request, tijmu_get_user_data, tijmu_get_teacher_data
from data_transfer.utils.network import success_response, get_para_from_request_safe, error_response


def tijmu_get_user_data_view(request):
    """
    URL[GET]:/data/tijmu/get_user_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = tijmu_get_user_data()
    return success_response(ret_data)


def tijmu_get_teacher_data_view(request):
    """
    URL[GET]:/data/tijmu/get_user_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = tijmu_get_teacher_data()
    return success_response(ret_data)


def tijmu_get_course_data_view(request):
    """
    URL[GET]:/data/tijmu/get_course_data/
    PARA:
    key
    year
    term
    """
    key = get_para_from_request_safe(request, 'key')
    year = get_para_from_request_safe(request, 'year')

    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = tijmu_get_course_data(year)
    return success_response(ret_data)


def tijmu_get_choose_data_view(request):
    """
    URL[GET]:/data/tijmu/get_choose_data/
    PARA:
    key
    year_str
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = tijmu_get_choose_data()
    return success_response(ret_data)

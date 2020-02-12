# coding:utf-8

from data_transfer.module_managers.tmucmc_manager import tmucmc_get_course_data, tmucmc_get_choose_data, \
    is_valid_request, tmucmc_get_user_data, tmucmc_get_teacher_data, tmucmc_verify_user_pwd
from data_transfer.utils.network import success_response, get_para_from_request_safe, error_response


def tmucmc_verify_user_pwd_view(request):
    """
    URL[GET]:/data/tmucmc/verify_user_pwd/
    """
    number = get_para_from_request_safe(request, 'number')
    pwd = get_para_from_request_safe(request, 'pwd')

    ret_data = tmucmc_verify_user_pwd(number, pwd)
    return success_response(ret_data)


def tmucmc_get_user_data_view(request):
    """
    URL[GET]:/data/tmucmc/get_user_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = tmucmc_get_user_data()
    return success_response(ret_data)


def tmucmc_get_teacher_data_view(request):
    """
    URL[GET]:/data/tmucmc/get_user_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = tmucmc_get_teacher_data()
    return success_response(ret_data)


def tmucmc_get_course_data_view(request):
    """
    URL[GET]:/data/tmucmc/get_course_data/
    PARA:
    key
    year
    term
    """
    key = get_para_from_request_safe(request, 'key')
    year = get_para_from_request_safe(request, 'year')

    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = tmucmc_get_course_data(year)
    return success_response(ret_data)


def tmucmc_get_choose_data_view(request):
    """
    URL[GET]:/data/tmucmc/get_choose_data/
    PARA:
    key
    year_str
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')
    year = get_para_from_request_safe(request, 'year')

    ret_data = tmucmc_get_choose_data(year)
    return success_response(ret_data)

# coding:utf-8

from data_transfer.module_managers.ouc_manager import ouc_get_course_data, ouc_get_choose_data, \
    is_valid_request, ouc_get_user_data, ouc_get_department_data, ouc_get_tra_data
from data_transfer.utils.network import success_response, get_para_from_request_safe, error_response



def ouc_get_department_data_view(request):
    """
    URL[GET]:/data/ouc/get_department_data/
    """
    # key = get_para_from_request_safe(request, 'key')
    # if not is_valid_request(key):
    #     return error_response('无效的请求!')

    ret_data = ouc_get_department_data()
    return success_response(ret_data)


def ouc_get_tra_data_view(request):
    """
    URL[GET]:/data/ouc/get_tra_data/
    """
    # key = get_para_from_request_safe(request, 'key')
    # if not is_valid_request(key):
    #     return error_response('无效的请求!')

    ret_data = ouc_get_tra_data()
    return success_response(ret_data)


def ouc_get_user_data_view(request):
    """
    URL[GET]:/data/ouc/get_student_data/
    """
    # key = get_para_from_request_safe(request, 'key')
    # if not is_valid_request(key):
    #     return error_response('无效的请求!')

    ret_data = ouc_get_user_data()
    return success_response(ret_data)


def ouc_get_course_data_view(request):
    """
    URL[GET]:/data/ouc/get_course_data/
    PARA:
    key
    year
    term
    """
    key = get_para_from_request_safe(request, 'key')
    year = get_para_from_request_safe(request, 'year')
    term = get_para_from_request_safe(request, 'term')

    # if not is_valid_request(key):
    #     return error_response('无效的请求!')

    ret_data = ouc_get_course_data(year, term)
    return success_response(ret_data)


def ouc_get_choose_data_view(request):
    """
    URL[GET]:/data/ouc/get_choose_data/
    PARA:
    key
    year_str
    """
    # key = get_para_from_request_safe(request, 'key')
    # if not is_valid_request(key):
    #     return error_response('无效的请求!')

    year = get_para_from_request_safe(request, 'year')
    term = get_para_from_request_safe(request, 'term')

    ret_data = ouc_get_choose_data(year, term)
    return success_response(ret_data)

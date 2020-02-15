# coding:utf-8

from data_transfer.module_managers.sdada_manager import sdada_get_course_data, sdada_get_choose_data, \
    is_valid_request, sdada_get_student_data, sdada_get_teacher_data, sdada_get_department_data, sdada_get_tra_data, sdada_get_gra_student_data
from data_transfer.utils.network import success_response, get_para_from_request_safe, error_response



def sdada_get_department_data_view(request):
    """
    URL[GET]:/data/sdada/get_department_data/
    """
    # key = get_para_from_request_safe(request, 'key')
    # if not is_valid_request(key):
    #     return error_response('无效的请求!')

    ret_data = sdada_get_department_data()
    return success_response(ret_data)


def sdada_get_tra_data_view(request):
    """
    URL[GET]:/data/sdada/get_tra_data/
    """
    # key = get_para_from_request_safe(request, 'key')
    # if not is_valid_request(key):
    #     return error_response('无效的请求!')

    ret_data = sdada_get_tra_data()
    return success_response(ret_data)

def sdada_get_student_data_view(request):
    """
    URL[GET]:/data/sdada/get_student_data/
    """
    # key = get_para_from_request_safe(request, 'key')
    # if not is_valid_request(key):
    #     return error_response('无效的请求!')

    ret_data = sdada_get_student_data()
    return success_response(ret_data)


def sdada_get_gra_student_data_view(request):
    """
    URL[GET]:/data/sdada/get_student_data/
    """
    # key = get_para_from_request_safe(request, 'key')
    # if not is_valid_request(key):
    #     return error_response('无效的请求!')

    ret_data = sdada_get_gra_student_data()
    return success_response(ret_data)


def sdada_get_teacher_data_view(request):
    """
    URL[GET]:/data/sdada/get_teacher_data/
    """
    # key = get_para_from_request_safe(request, 'key')
    # if not is_valid_request(key):
    #     return error_response('无效的请求!')

    ret_data = sdada_get_teacher_data()
    return success_response(ret_data)


def sdada_get_course_data_view(request):
    """
    URL[GET]:/data/sdada/get_course_data/
    PARA:
    key
    year
    term
    """
    # key = get_para_from_request_safe(request, 'key')
    year_term = get_para_from_request_safe(request, 'year_term')

    # if not is_valid_request(key):
    #     return error_response('无效的请求!')

    ret_data = sdada_get_course_data(year, term)
    return success_response(ret_data)


def sdada_get_choose_data_view(request):
    """
    URL[GET]:/data/sdada/get_choose_data/
    PARA:
    key
    year_str
    """
    # key = get_para_from_request_safe(request, 'key')
    # if not is_valid_request(key):
    #     return error_response('无效的请求!')

    year_term = get_para_from_request_safe(request, 'year_term')

    ret_data = sdada_get_choose_data(year_term)
    return success_response(ret_data)

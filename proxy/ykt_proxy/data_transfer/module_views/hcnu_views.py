# coding:utf-8

from data_transfer.module_managers.hcnu_manager import hcnu_get_teacher_data, \
    hcnu_get_department_data, hcnu_get_student_data, hcnu_get_course_data, hcnu_get_choose_data, is_valid_request, \
    hcnu_get_tradition_class_data
from data_transfer.utils.network import success_response, get_para_from_request_safe, error_response


def hcnu_get_department_data_view(request):
    """
    URL[GET]:/data/hcnu/get_department_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = hcnu_get_department_data()
    return success_response(ret_data)


def hcnu_get_tradition_class_data_view(request):
    """
    URL[GET]:/data/hcnu/get_tradition_class_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = hcnu_get_tradition_class_data()
    return success_response(ret_data)


def hcnu_get_student_data_view(request):
    """
    URL[GET]:/data/hcnu/get_student_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = hcnu_get_student_data()
    return success_response(ret_data)


def hcnu_get_teacher_data_view(request):
    """
    URL[GET]:/data/hcnu/get_teacher_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = hcnu_get_teacher_data()
    return success_response(ret_data)


def hcnu_get_course_data_view(request):
    """
    URL[GET]:/data/hcnu/get_course_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = hcnu_get_course_data()
    return success_response(ret_data)


def hcnu_get_choose_data_view(request):
    """
    URL[GET]:/data/hcnu/get_choose_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = hcnu_get_choose_data()
    return success_response(ret_data)

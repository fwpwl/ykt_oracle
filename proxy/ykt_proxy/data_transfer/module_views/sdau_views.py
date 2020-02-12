# coding:utf-8
from data_transfer.module_managers.sdau_manager import is_valid_request
from data_transfer.module_managers.sdau_manager import sdau_get_department_data, sdau_get_tradition_class_data, \
    sdau_get_user_map_data, sdau_get_course_class_data, sdau_get_choose_course_data
from data_transfer.utils.network import success_response, get_para_from_request_safe, error_response


def sdau_get_department_data_view(request):
    """
    URL[GET]:/data/sdau/sdau_get_department_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = sdau_get_department_data()
    return success_response(ret_data)


def sdau_get_tra_class_data_view(request):
    """
    URL[GET]:/data/sdau/sdau_get_teacher_data/
    PARA:
    key
    year
    term
    """
    key = get_para_from_request_safe(request, 'key')

    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = sdau_get_tradition_class_data()
    return success_response(ret_data)


def sdau_get_student_data_view(request):
    """
    URL[GET]:/data/sdau/sdau_get_course_data/
    PARA:
    key
    year_str
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = sdau_get_user_map_data()
    return success_response(ret_data)


def sdau_get_course_data_view(request):
    """
    URL[GET]:/data/sdau/sdau_get_choose_data/
    PARA:
    key
    year_str
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    year = get_para_from_request_safe(request, 'year')
    term = get_para_from_request_safe(request, 'term')
    ret_data = sdau_get_course_class_data(year, term)
    return success_response(ret_data)


def sdau_get_choose_data_view(request):
    """
    URL[GET]:/data/sdau/sdau_get_choose_data/
    PARA:
    key
    year_str
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    year = get_para_from_request_safe(request, 'year')
    term = get_para_from_request_safe(request, 'term')
    ret_data = sdau_get_choose_course_data(year, term)
    return success_response(ret_data)

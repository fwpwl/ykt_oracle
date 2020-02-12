# coding:utf-8
from data_transfer.module_managers.sdcit_manager import sdcit_get_department_info_data, sdcit_get_tradition_class_info, \
    sdcit_get_user_info, sdcit_get_course_info, sdcit_get_choose_info
from data_transfer.utils.network import json_http_response


def sdcit_get_department_info_data_view(request):
    """
    URL[GET]:/data/sdcit/get_department_info_data/
    """
    try:
        ret_data = sdcit_get_department_info_data()
        result_dict = {
            "success": True,
            "msg": "",
            "data": ret_data
        }
    except Exception as e:
        result_dict = {
            "success": False,
            "msg": str(e),
            "data": {}
        }

    return json_http_response(result_dict)


def sdcit_get_tradition_class_info_view(request):
    """
    URL[GET]:/data/sdcit/get_tradition_class_info/
    """
    try:
        ret_data = sdcit_get_tradition_class_info()
        result_dict = {
            "success": True,
            "msg": "",
            "data": ret_data
        }
    except Exception as e:
        result_dict = {
            "success": False,
            "msg": str(e),
            "data": {}
        }

    return json_http_response(result_dict)


def sdcit_get_user_info_view(request):
    """
    URL[GET]:/data/sdcit/get_user_info/
    """
    try:
        ret_data = sdcit_get_user_info()
        result_dict = {
            "success": True,
            "msg": "",
            "data": ret_data
        }
    except Exception as e:
        result_dict = {
            "success": False,
            "msg": str(e),
            "data": {}
        }

    return json_http_response(result_dict)


def sdcit_get_course_info_view(request):
    """
    URL[GET]:/data/sdcit/get_course_info/
    """
    try:
        ret_data = sdcit_get_course_info()
        result_dict = {
            "success": True,
            "msg": "",
            "data": ret_data
        }
    except Exception as e:
        result_dict = {
            "success": False,
            "msg": str(e),
            "data": {}
        }

    return json_http_response(result_dict)


def sdcit_get_choose_info_view(request):
    """
    URL[GET]:/data/sdcit/get_choose_info/
    """
    try:
        ret_data = sdcit_get_choose_info()
        result_dict = {
            "success": True,
            "msg": "",
            "data": ret_data
        }
    except Exception as e:
        result_dict = {
            "success": False,
            "msg": str(e),
            "data": {}
        }

    return json_http_response(result_dict)

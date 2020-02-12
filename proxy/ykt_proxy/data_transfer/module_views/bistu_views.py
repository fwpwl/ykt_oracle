# coding:utf-8

from data_transfer.module_managers import bistu_manager
from data_transfer.utils.network import success_response, error_response


def get_department_data_view(request):
    """
    URL[GET]:/data/bistu/get_department_data/
    """

    ret_data = bistu_manager.get_department_data()
    return success_response(ret_data)


def get_tra_classroom_data_view(request):
    ret_data = bistu_manager.get_tra_classroom_data()
    return success_response(ret_data)


def get_user_data_view(request):
    ret_data = bistu_manager.get_user_data()
    return success_response(ret_data)


def get_course_data_view(request):
    year = request.GET.get("year", "2019-2020")
    term = request.GET.get("term", 1)
    ret_data = bistu_manager.get_course_data(year=year, term=term)
    return success_response(ret_data)


def get_choose_data_view(request):
    year = request.GET.get("year", "2019-2020")
    term = request.GET.get("term", 1)
    ret_data = bistu_manager.get_choose_data(year=year, term=term)
    return success_response(ret_data)

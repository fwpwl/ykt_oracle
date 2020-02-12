# coding:utf-8

from data_transfer.module_managers import cmu_manager
from data_transfer.utils.network import success_response, error_response
from data_transfer.utils.safe import check_signature


def get_department_data_view(request):
    """
    URL[GET]:/data/cmu/get_department_data/
    """
    params = {k: v for k, v in request.GET.items()}
    if not check_signature(**params):
        return error_response('无效的请求!')

    ret_data = cmu_manager.get_department_data()
    return success_response(ret_data)


def get_tra_classroom_data_view(request):
    params = {k: v for k, v in request.GET.items()}
    if not check_signature(**params):
        return error_response('无效的请求!')

    ret_data = cmu_manager.get_tra_classroom_data()
    return success_response(ret_data)


def get_user_data_view(request):
    params = {k: v for k, v in request.GET.items()}
    if not check_signature(**params):
        return error_response('无效的请求!')

    ret_data = cmu_manager.get_user_data()
    return success_response(ret_data)


def get_course_data_view(request):
    params = {k: v for k, v in request.GET.items()}
    if not check_signature(**params):
        return error_response('无效的请求!')

    year = request.GET.get("year", "2019-2020")
    term = request.GET.get("term", 1)
    ret_data = cmu_manager.get_course_data(year=year, term=term)
    return success_response(ret_data)


def get_choose_data_view(request):
    params = {k: v for k, v in request.GET.items()}
    if not check_signature(**params):
        return error_response('无效的请求!')

    year = request.GET.get("year", "2019-2020")
    term = request.GET.get("term", 1)
    ret_data = cmu_manager.get_choose_data(year=year, term=term)
    return success_response(ret_data)

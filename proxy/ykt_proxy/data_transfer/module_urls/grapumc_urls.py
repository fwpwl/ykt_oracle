# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.grapumc_views import grapumc_get_course_data_view, grapumc_get_choose_data_view, \
    grapumc_get_user_data_view, grapumc_get_department_data_view, grapumc_get_tra_data_view

urlpatterns = [
    url(r'^get_department_data/?$', grapumc_get_department_data_view),
    url(r'^get_user_data/?$', grapumc_get_user_data_view),
    url(r'^get_course_data/?$', grapumc_get_course_data_view),
    url(r'^get_choose_data/?$', grapumc_get_choose_data_view),
    url(r'^get_tra_classroom_data/?$', grapumc_get_tra_data_view),

]

# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.xhcom_views import xhcom_get_course_data_view, xhcom_get_choose_data_view, \
    xhcom_get_user_data_view, xhcom_get_department_data_view, xhcom_get_tra_data_view

urlpatterns = [
    url(r'^get_department_data/?$', xhcom_get_department_data_view),
    url(r'^get_user_data/?$', xhcom_get_user_data_view),
    url(r'^get_course_data/?$', xhcom_get_course_data_view),
    url(r'^get_choose_data/?$', xhcom_get_choose_data_view),
    url(r'^get_tra_classroom_data/?$', xhcom_get_tra_data_view),

]

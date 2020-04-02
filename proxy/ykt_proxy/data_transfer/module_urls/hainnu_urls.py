# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.hainnu_views import hainnu_get_course_data_view, hainnu_get_choose_data_view, \
    hainnu_get_user_data_view, hainnu_get_department_data_view, hainnu_get_tra_data_view

urlpatterns = [
    url(r'^get_department_data/?$', hainnu_get_department_data_view),
    url(r'^get_user_data/?$', hainnu_get_user_data_view),
    url(r'^get_course_data/?$', hainnu_get_course_data_view),
    url(r'^get_choose_data/?$', hainnu_get_choose_data_view),
    url(r'^get_tra_classroom_data/?$', hainnu_get_tra_data_view),

]

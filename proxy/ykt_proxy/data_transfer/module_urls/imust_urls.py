# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.imust_views import imust_get_course_data_view, imust_get_choose_data_view, \
    imust_get_user_data_view, imust_get_department_data_view, imust_get_tra_data_view

urlpatterns = [
    url(r'^get_department_data/?$', imust_get_department_data_view),
    url(r'^get_user_data/?$', imust_get_user_data_view),
    url(r'^get_course_data/?$', imust_get_course_data_view),
    url(r'^get_choose_data/?$', imust_get_choose_data_view),
    url(r'^get_tra_classroom_data/?$', imust_get_tra_data_view),

]

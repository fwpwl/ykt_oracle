# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.ztu_views import ztu_get_course_data_view, ztu_get_choose_data_view, \
    ztu_get_user_data_view, ztu_get_department_data_view, ztu_get_tra_data_view

urlpatterns = [
    url(r'^get_department_data/?$', ztu_get_department_data_view),
    url(r'^get_user_data/?$', ztu_get_user_data_view),
    url(r'^get_course_data/?$', ztu_get_course_data_view),
    url(r'^get_choose_data/?$', ztu_get_choose_data_view),
    url(r'^get_tra_classroom_data/?$', ztu_get_tra_data_view),

]

# -*- coding:utf-8 -*-
from django.conf.urls import url

from data_transfer.module_views.sdau_views import sdau_get_department_data_view, sdau_get_course_data_view, \
    sdau_get_choose_data_view
from data_transfer.module_views.sdau_views import sdau_get_student_data_view
from data_transfer.module_views.sdau_views import sdau_get_tra_class_data_view

urlpatterns = [
    url(r'^sdau_get_department_data/$', sdau_get_department_data_view),
    url(r'^sdau_get_tra_class_data/$', sdau_get_tra_class_data_view),
    url(r'^sdau_get_student_data/$', sdau_get_student_data_view),
    url(r'^sdau_get_course_data/$', sdau_get_course_data_view),
    url(r'^sdau_get_choose_data/$', sdau_get_choose_data_view),
]

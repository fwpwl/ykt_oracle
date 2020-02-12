# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.ecjtu_views import ecjtu_get_teacher_data_view, \
    ecjtu_get_course_data_view, ecjtu_get_student_choose_data_view, ecjtu_get_teacher_choose_data_view, \
    ecjtu_get_student_data_view

urlpatterns = [
    url(r'^get_student_data/?$', ecjtu_get_student_data_view),
    url(r'^get_teacher_data/?$', ecjtu_get_teacher_data_view),
    url(r'^get_course_data/?$', ecjtu_get_course_data_view),
    url(r'^get_student_choose_data/?$', ecjtu_get_student_choose_data_view),
    url(r'^get_teacher_choose_data/?$', ecjtu_get_teacher_choose_data_view),
]

# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.hbwe_views import hbwe_get_student_data_view, hbwe_get_teacher_data_view, \
    hbwe_get_course_data_view, hbwe_get_classroom_data_view, hbwe_get_choose_data_view

urlpatterns = [

    url(r'^hbwe_get_student_data/?$', hbwe_get_student_data_view),
    url(r'^hbwe_get_teacher_data/?$', hbwe_get_teacher_data_view),
    url(r'^hbwe_get_course_data/?$', hbwe_get_course_data_view),
    url(r'^hbwe_get_classroom_data/?$', hbwe_get_classroom_data_view),
    url(r'^hbwe_get_choose_data/?$', hbwe_get_choose_data_view),
]

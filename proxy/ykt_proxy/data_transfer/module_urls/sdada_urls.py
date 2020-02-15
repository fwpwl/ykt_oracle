# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.sdada_views import sdada_get_course_data_view, sdada_get_choose_data_view, \
    sdada_get_student_data_view, sdada_get_teacher_data_view, sdada_get_tra_data_view, sdada_get_department_data_view

urlpatterns = [
    url(r'^get_department_data/?$', sdada_get_department_data_view),
    url(r'^get_student_data/?$', sdada_get_student_data_view),
    url(r'^get_teacher_data/?$', sdada_get_teacher_data_view),
    url(r'^get_course_data/?$', sdada_get_course_data_view),
    url(r'^get_choose_data/?$', sdada_get_choose_data_view),
    url(r'^get_tra_classroom_data/?$', sdada_get_tra_data_view),

]

# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.gznc_views import gznc_get_department_data_view, gznc_get_tra_classroom_data_view, \
    gznc_get_student_data_view, gznc_get_teacher_data_view, gznc_get_course_data_view, gznc_get_choose_data_view

urlpatterns = [

    url(r'^get_department_data/?$', gznc_get_department_data_view),
    url(r'^get_tra_classroom_data/?$', gznc_get_tra_classroom_data_view),
    url(r'^get_student_data/?$', gznc_get_student_data_view),
    url(r'^get_teacher_data/?$', gznc_get_teacher_data_view),
    url(r'^get_course_data_view/?$', gznc_get_course_data_view),
    url(r'^get_choose_data_view/?$', gznc_get_choose_data_view),

]

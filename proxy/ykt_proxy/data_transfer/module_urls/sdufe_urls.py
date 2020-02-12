# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.sdufe_views import sdufe_get_department_data_view, sdufe_get_tra_class_data_view, \
    sdufe_get_student_data_view, sdufe_get_teacher_data_view, sdufe_get_course_data_view, sdufe_get_choose_data_view

urlpatterns = [
    url(r'^sdufe_get_department_data/?$', sdufe_get_department_data_view),
    url(r'^sdufe_get_tra_class_data/?$', sdufe_get_tra_class_data_view),
    url(r'^sdufe_get_student_data/?$', sdufe_get_student_data_view),
    url(r'^sdufe_get_teacher_data/?$', sdufe_get_teacher_data_view),
    url(r'^sdufe_get_course_data/?$', sdufe_get_course_data_view),
    url(r'^sdufe_get_choose_data/?$', sdufe_get_choose_data_view),
]

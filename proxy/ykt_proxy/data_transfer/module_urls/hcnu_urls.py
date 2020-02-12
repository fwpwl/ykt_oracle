# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.hcnu_views import hcnu_get_student_data_view, hcnu_get_teacher_data_view, \
    hcnu_get_department_data_view, hcnu_get_course_data_view, hcnu_get_choose_data_view, \
    hcnu_get_tradition_class_data_view

urlpatterns = [
    url(r'^get_department_data/?$', hcnu_get_department_data_view),
    url(r'^get_tradition_class_data/?$', hcnu_get_tradition_class_data_view),
    url(r'^get_student_data/?$', hcnu_get_student_data_view),
    url(r'^get_teacher_data/?$', hcnu_get_teacher_data_view),
    url(r'^get_course_data/?$', hcnu_get_course_data_view),
    url(r'^get_choose_data/?$', hcnu_get_choose_data_view),
]

# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.nwnu_views import nwnu_get_course_data_view, nwnu_get_student_data_view, \
    nwnu_get_department_data_view, nwnu_get_teacher_data_view, nwnu_get_tra_classroom_data_view, \
    nwnu_get_student_name_data_view

urlpatterns = [
    url(r'^get_department_data/?$', nwnu_get_department_data_view),
    url(r'^get_teacher_data/?$', nwnu_get_teacher_data_view),
    url(r'^get_course_data/?$', nwnu_get_course_data_view),
    url(r'^get_tra_classroom_data/?$', nwnu_get_tra_classroom_data_view),
    url(r'^get_student_data/?$', nwnu_get_student_data_view),
    url(r'^get_student_name_data/?$', nwnu_get_student_name_data_view),

]


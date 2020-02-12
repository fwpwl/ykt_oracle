# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.xzmu_views import xzmu_get_student_data_view, xzmu_get_teacher_data_view, \
    xzmu_get_teacher_course_data_view, xzmu_get_student_course_data_view

urlpatterns = [
    url(r'^get_student_data/?$', xzmu_get_student_data_view),
    url(r'^get_teacher_data/?$', xzmu_get_teacher_data_view),
    url(r'^get_teacher_course_data/?$', xzmu_get_teacher_course_data_view),
    url(r'^get_student_course_data/?$', xzmu_get_student_course_data_view),

]

# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.hitsz_views import hitsz_get_course_data_view, hitsz_get_choose_data_view, \
    hitsz_get_student_data_view, hitsz_get_teacher_data_view

urlpatterns = [
    url(r'^get_student_data/?$', hitsz_get_student_data_view),
    url(r'^get_teacher_data/?$', hitsz_get_teacher_data_view),
    url(r'^get_course_data/?$', hitsz_get_course_data_view),
    url(r'^get_choose_data/?$', hitsz_get_choose_data_view),

]

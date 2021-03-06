# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.hit_views import hit_get_course_data_view, hit_get_choose_data_view, \
    hit_get_user_data_view, hit_get_department_data_view, hit_get_tra_data_view

urlpatterns = [
    url(r'^get_department_data/?$', hit_get_department_data_view),
    url(r'^get_user_data/?$', hit_get_user_data_view),
    url(r'^get_course_data/?$', hit_get_course_data_view),
    url(r'^get_choose_data/?$', hit_get_choose_data_view),
    url(r'^get_tra_classroom_data/?$', hit_get_tra_data_view),

]

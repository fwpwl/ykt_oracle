# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.zjxu_views import zjxu_get_course_data_view, zjxu_get_choose_data_view, \
    zjxu_get_user_data_view, zjxu_get_department_data_view, zjxu_get_tra_data_view

urlpatterns = [
    url(r'^get_department_data/?$', zjxu_get_department_data_view),
    url(r'^get_user_data/?$', zjxu_get_user_data_view),
    url(r'^get_course_data/?$', zjxu_get_course_data_view),
    url(r'^get_choose_data/?$', zjxu_get_choose_data_view),
    url(r'^get_tra_classroom_data/?$', zjxu_get_tra_data_view),

]

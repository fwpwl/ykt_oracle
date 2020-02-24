# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.cipuc_views import cipuc_get_course_data_view, cipuc_get_choose_data_view, \
    cipuc_get_user_data_view, cipuc_get_department_data_view, cipuc_get_tra_data_view

urlpatterns = [
    url(r'^get_department_data/?$', cipuc_get_department_data_view),
    url(r'^get_user_data/?$', cipuc_get_user_data_view),
    url(r'^get_course_data/?$', cipuc_get_course_data_view),
    url(r'^get_choose_data/?$', cipuc_get_choose_data_view),
    url(r'^get_tra_classroom_data/?$', cipuc_get_tra_data_view),

]

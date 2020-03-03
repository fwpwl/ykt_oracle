# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.hnit_views import hnit_get_course_data_view, hnit_get_choose_data_view, \
    hnit_get_user_data_view, hnit_get_department_data_view, hnit_get_tra_data_view

urlpatterns = [
    url(r'^get_department_data/?$', hnit_get_department_data_view),
    url(r'^get_user_data/?$', hnit_get_user_data_view),
    url(r'^get_course_data/?$', hnit_get_course_data_view),
    url(r'^get_choose_data/?$', hnit_get_choose_data_view),
    url(r'^get_tra_classroom_data/?$', hnit_get_tra_data_view),

]

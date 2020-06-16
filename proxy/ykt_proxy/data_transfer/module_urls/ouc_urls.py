# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.ouc_views import ouc_get_course_data_view, ouc_get_choose_data_view, \
    ouc_get_user_data_view, ouc_get_department_data_view, ouc_get_tra_data_view

urlpatterns = [
    url(r'^get_department_data/?$', ouc_get_department_data_view),
    url(r'^get_user_data/?$', ouc_get_user_data_view),
    url(r'^get_course_data/?$', ouc_get_course_data_view),
    url(r'^get_choose_data/?$', ouc_get_choose_data_view),
    url(r'^get_tra_classroom_data/?$', ouc_get_tra_data_view),

]

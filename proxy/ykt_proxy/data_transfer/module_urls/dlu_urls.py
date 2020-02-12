# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.dlu_views import dlu_get_course_data_view, dlu_get_choose_data_view, \
    dlu_get_user_data_view, dlu_get_department_data_view, \
    dlu_get_tra_class_data_view

urlpatterns = [
    url(r'^get_department_data/?$', dlu_get_department_data_view),
    url(r'^get_tra_class_data/?$', dlu_get_tra_class_data_view),
    url(r'^get_user_data/?$', dlu_get_user_data_view),
    url(r'^get_course_data/?$', dlu_get_course_data_view),
    url(r'^get_choose_data/?$', dlu_get_choose_data_view),

]

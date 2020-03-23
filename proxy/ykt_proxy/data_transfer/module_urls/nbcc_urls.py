# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.nbcc_views import nbcc_get_course_data_view, nbcc_get_choose_data_view, \
    nbcc_get_user_data_view, nbcc_get_department_data_view, nbcc_get_tra_data_view

urlpatterns = [
    url(r'^get_department_data/?$', nbcc_get_department_data_view),
    url(r'^get_user_data/?$', nbcc_get_user_data_view),
    url(r'^get_course_data/?$', nbcc_get_course_data_view),
    url(r'^get_choose_data/?$', nbcc_get_choose_data_view),
    url(r'^get_tra_classroom_data/?$', nbcc_get_tra_data_view),

]

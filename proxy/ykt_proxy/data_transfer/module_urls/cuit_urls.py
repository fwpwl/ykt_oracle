# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.cuit_views import cuit_get_course_data_view, cuit_get_choose_data_view, \
    cuit_get_user_data_view, cuit_get_department_data_view, cuit_get_tra_data_view

urlpatterns = [
    url(r'^get_department_data/?$', cuit_get_department_data_view),
    url(r'^get_user_data/?$', cuit_get_user_data_view),
    url(r'^get_course_data/?$', cuit_get_course_data_view),
    url(r'^get_choose_data/?$', cuit_get_choose_data_view),
    url(r'^get_tra_classroom_data/?$', cuit_get_tra_data_view),

]

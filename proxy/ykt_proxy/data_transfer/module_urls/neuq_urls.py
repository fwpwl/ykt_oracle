# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.neuq_views import neuq_get_course_data_view, neuq_get_choose_data_view, \
    neuq_get_user_data_view, neuq_get_department_data_view, neuq_get_tra_data_view

urlpatterns = [
    url(r'^get_department_data/?$', neuq_get_department_data_view),
    url(r'^get_user_data/?$', neuq_get_user_data_view),
    url(r'^get_course_data/?$', neuq_get_course_data_view),
    url(r'^get_choose_data/?$', neuq_get_choose_data_view),
    url(r'^get_tra_classroom_data/?$', neuq_get_tra_data_view),

]

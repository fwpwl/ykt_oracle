# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.hebau_views import hebau_get_course_data_view, hebau_get_choose_data_view, \
    hebau_get_user_data_view, hebau_get_department_data_view, hebau_get_tra_data_view

urlpatterns = [
    url(r'^get_department_data/?$', hebau_get_department_data_view),
    url(r'^get_user_data/?$', hebau_get_user_data_view),
    url(r'^get_course_data/?$', hebau_get_course_data_view),
    url(r'^get_choose_data/?$', hebau_get_choose_data_view),
    url(r'^get_tra_classroom_data/?$', hebau_get_tra_data_view),

]

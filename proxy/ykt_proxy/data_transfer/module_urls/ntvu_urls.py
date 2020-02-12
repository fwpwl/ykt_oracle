# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.ntvu_views import ntvu_get_course_data_view, ntvu_get_choose_data_view, \
    ntvu_get_user_data_view, ntvu_get_department_data_view, \
    ntvu_get_tra_class_data_view

urlpatterns = [
    url(r'^get_department_data/?$', ntvu_get_department_data_view),
    url(r'^get_tra_class_data/?$', ntvu_get_tra_class_data_view),
    url(r'^get_user_data/?$', ntvu_get_user_data_view),
    url(r'^get_course_data/?$', ntvu_get_course_data_view),
    url(r'^get_choose_data/?$', ntvu_get_choose_data_view),

]

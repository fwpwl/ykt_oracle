# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.ahut_views import ahut_get_course_data_view, ahut_get_choose_data_view, \
    ahut_get_user_data_view, ahut_get_department_data_view, ahut_get_tra_data_view

urlpatterns = [
    url(r'^get_department_data/?$', ahut_get_department_data_view),
    url(r'^get_user_data/?$', ahut_get_user_data_view),
    url(r'^get_course_data/?$', ahut_get_course_data_view),
    url(r'^get_choose_data/?$', ahut_get_choose_data_view),
    url(r'^get_tra_classroom_data/?$', ahut_get_tra_data_view),

]
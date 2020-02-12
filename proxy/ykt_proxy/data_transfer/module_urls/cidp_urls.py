# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.cidp_views import cidp_get_department_info_data_view, \
    cidp_get_tradition_class_info_view, \
    cidp_get_user_info_view, cidp_get_course_info_view, cidp_get_choose_info_view

urlpatterns = [
    url(r'^get_department_info_data/?$', cidp_get_department_info_data_view),
    url(r'^get_tradition_class_info/?$', cidp_get_tradition_class_info_view),
    url(r'^get_user_info/?$', cidp_get_user_info_view),
    url(r'^get_course_info/?$', cidp_get_course_info_view),
    url(r'^get_choose_info/?$', cidp_get_choose_info_view),

]

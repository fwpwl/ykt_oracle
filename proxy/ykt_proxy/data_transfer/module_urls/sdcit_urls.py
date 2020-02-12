# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.sdcit_views import sdcit_get_department_info_data_view, \
    sdcit_get_tradition_class_info_view, \
    sdcit_get_user_info_view, sdcit_get_course_info_view, sdcit_get_choose_info_view

urlpatterns = [
    url(r'^get_department_info_data/?$', sdcit_get_department_info_data_view),
    url(r'^get_tradition_class_info/?$', sdcit_get_tradition_class_info_view),
    url(r'^get_user_info/?$', sdcit_get_user_info_view),
    url(r'^get_course_info/?$', sdcit_get_course_info_view),
    url(r'^get_choose_info/?$', sdcit_get_choose_info_view),

]

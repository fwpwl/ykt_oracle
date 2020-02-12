# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.xijing_views import xijing_get_course_data_view, xijing_get_choose_data_view, \
    xijing_get_user_data_view

urlpatterns = [

    url(r'^get_user_data/?$', xijing_get_user_data_view),
    url(r'^get_course_data/?$', xijing_get_course_data_view),
    url(r'^get_choose_data/?$', xijing_get_choose_data_view),

]

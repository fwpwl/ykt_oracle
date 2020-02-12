# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.tczyxy_views import tczyxy_get_user_view, tczyxy_get_course_view, tczyxy_get_choose_view

urlpatterns = [
    url(r'^get_user/?$', tczyxy_get_user_view),
    url(r'^get_course/?$', tczyxy_get_course_view),
    url(r'^get_choose/?$', tczyxy_get_choose_view),

]

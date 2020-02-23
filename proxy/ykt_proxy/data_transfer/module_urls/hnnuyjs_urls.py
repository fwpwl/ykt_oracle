# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.hnnuyjs_views import hnnuyjs_get_course_data_view, hnnuyjs_get_choose_data_view, \
    hnnuyjs_get_user_data_view, hnnuyjs_get_department_data_view, hnnuyjs_get_tra_data_view

urlpatterns = [
    url(r'^get_department_data/?$', hnnuyjs_get_department_data_view),
    url(r'^get_user_data/?$', hnnuyjs_get_user_data_view),
    url(r'^get_course_data/?$', hnnuyjs_get_course_data_view),
    url(r'^get_choose_data/?$', hnnuyjs_get_choose_data_view),
    url(r'^get_tra_classroom_data/?$', hnnuyjs_get_tra_data_view),

]

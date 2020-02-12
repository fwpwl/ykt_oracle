# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.tmucmc_views import tmucmc_get_course_data_view, tmucmc_get_choose_data_view, \
    tmucmc_get_user_data_view, tmucmc_get_teacher_data_view, tmucmc_verify_user_pwd_view

urlpatterns = [
    url(r'^verify_user_pwd/?$', tmucmc_verify_user_pwd_view),
    url(r'^get_user_data/?$', tmucmc_get_user_data_view),
    url(r'^get_teacher_data/?$', tmucmc_get_teacher_data_view),
    url(r'^get_course_data/?$', tmucmc_get_course_data_view),
    url(r'^get_choose_data/?$', tmucmc_get_choose_data_view),

]

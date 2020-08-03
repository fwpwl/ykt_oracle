# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.hitwh_views import hitwh_get_course_data_view, hitwh_get_choose_data_view, \
    hitwh_get_user_data_view, hitwh_get_department_data_view, hitwh_get_tra_data_view

urlpatterns = [
    url(r'^get_department_data/?$', hitwh_get_department_data_view),
    url(r'^get_user_data/?$', hitwh_get_user_data_view),
    url(r'^get_course_data/?$', hitwh_get_course_data_view),
    url(r'^get_choose_data/?$', hitwh_get_choose_data_view),
    url(r'^get_tra_classroom_data/?$', hitwh_get_tra_data_view),

]

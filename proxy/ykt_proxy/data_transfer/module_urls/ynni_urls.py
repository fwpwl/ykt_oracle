# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.ynni_views import ynni_get_course_data_view, ynni_get_choose_data_view, \
    ynni_get_user_data_view, ynni_get_teacher_data_view, ynni_get_tra_class_data_view

urlpatterns = [

    url(r'^get_tra_class_data/?$', ynni_get_tra_class_data_view),
    url(r'^get_user_data/?$', ynni_get_user_data_view),
    url(r'^get_teacher_data/?$', ynni_get_teacher_data_view),
    url(r'^get_course_data/?$', ynni_get_course_data_view),
    url(r'^get_choose_data/?$', ynni_get_choose_data_view),

]

# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.jwxt_views import jwxt_get_course_data_view, jwxt_get_choose_data_view, \
    jwxt_get_user_data_view, jwxt_get_department_data_view, jwxt_get_tra_data_view

urlpatterns = [
    url(r'^get_department_data/?$', jwxt_get_department_data_view),
    url(r'^get_user_data/?$', jwxt_get_user_data_view),
    url(r'^get_course_data/?$', jwxt_get_course_data_view),
    url(r'^get_choose_data/?$', jwxt_get_choose_data_view),
    url(r'^get_tra_classroom_data/?$', jwxt_get_tra_data_view),

]

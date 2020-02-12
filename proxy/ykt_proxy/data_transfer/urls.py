# -*- coding:utf-8 -*-
from django.conf.urls import url, include

from data_transfer.views import test_server

urlpatterns = [

    url(r'^test_server/?$', test_server),
]

# 分层各模块URL
urlpatterns += [
    # 学校教务系统验证模块
    url(r"^zufe/", include("data_transfer.module_urls.zufe_urls")),
    url(r"^gznc/", include("data_transfer.module_urls.gznc_urls")),
    url(r"^xijing/", include("data_transfer.module_urls.xijing_urls")),
    url(r"^hbwe/", include("data_transfer.module_urls.hbwe_urls")),
    url(r"^sdufe/", include("data_transfer.module_urls.sdufe_urls")),
    url(r"^sdau/", include("data_transfer.module_urls.sdau_urls")),
    url(r"^xzmu/", include("data_transfer.module_urls.xzmu_urls")),
    url(r"^tczyxy/", include("data_transfer.module_urls.tczyxy_urls")),
    url(r"^tijmu/", include("data_transfer.module_urls.tijmu_urls")),
    url(r"^ynni/", include("data_transfer.module_urls.ynni_urls")),
    url(r"^tmucmc/", include("data_transfer.module_urls.tmucmc_urls")),
    url(r"^dlu/", include("data_transfer.module_urls.dlu_urls")),
    url(r"^ntvu/", include("data_transfer.module_urls.ntvu_urls")),
    url(r"^hitsz/", include("data_transfer.module_urls.hitsz_urls")),
    url(r"^hcnu/", include("data_transfer.module_urls.hcnu_urls")),
    url(r"^sdu/", include("data_transfer.module_urls.sdu_urls")),
    url(r"^nwnu/", include("data_transfer.module_urls.nwnu_urls")),
    url(r"^cidp/", include("data_transfer.module_urls.cidp_urls")),
    url(r"^sdcit/", include("data_transfer.module_urls.sdcit_urls")),
    # 北京信息科技大学
    url(r"^bistu/", include("data_transfer.module_urls.bistu_urls")),
    # 中国医科大学
    url(r"^cmu/", include("data_transfer.module_urls.cmu_urls")),
]

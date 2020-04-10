# -*- coding:utf-8 -*-
from django.conf.urls import url, include

from data_transfer.views import test_server

urlpatterns = [

    url(r'^test_server/?$', test_server)
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

    # 冯武鹏新增
    # 山东工艺
    url(r"^sdada/", include("data_transfer.module_urls.sdada_urls")),
    # 内蒙古科技大学
    url(r"^imust/", include("data_transfer.module_urls.imust_urls")),
    # 昭通学院
    url(r"^ztu/", include("data_transfer.module_urls.ztu_urls")),
    # 成都信息工程大学
    url(r"^cuit/", include("data_transfer.module_urls.cuit_urls")),
    # 哈尔滨工业大学
    url(r"^hit/", include("data_transfer.module_urls.hit_urls")),
    # 湖南师范大学研究生院
    url(r"^hnnuyjs/", include("data_transfer.module_urls.hnnuyjs_urls")),
    # 中国刑事警察学院
    url(r"^cipuc/", include("data_transfer.module_urls.cipuc_urls")),
    # 湖南工学院
    url(r"^hnit/", include("data_transfer.module_urls.hnit_urls")),
    # 嘉兴学院
    url(r"^zjxu/", include("data_transfer.module_urls.zjxu_urls")),
    # 河北农业大学
    url(r"^hebau/", include("data_transfer.module_urls.hebau_urls")),
    # 宁波城市职业技术学院
    url(r"^nbcc/", include("data_transfer.module_urls.nbcc_urls")),
    # 海南师范大学
    url(r"^hainnu/", include("data_transfer.module_urls.hainnu_urls")),
    # 东北大学秦皇岛分校
    url(r"^neuq/", include("data_transfer.module_urls.neuq_urls")),
    # 星海音乐学院
    url(r"^xhcom/", include("data_transfer.module_urls.xhcom_urls")),

]

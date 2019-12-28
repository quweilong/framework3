# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from django.conf.urls import patterns
from django.conf.urls import url
from . import views



urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    (r'^dev-guide/$', 'dev_guide'),
    (r'^contactus/$', 'contactus'),
    url(r'^home_page/$', views.home_page),  # 主机详情页面
    url(r'^save_info/$', views.save_info),  # 保存信息
    url(r'^all_info/$', views.all_info),  # 保存信息
    url(r'^get_profile_information/$', views.get_profile_information),  # 获取列表
    url(r'^delInfo/$', views.delInfo),  # 删除数据
    url(r'^getEditInfo/$', views.getEditInfo),  # 获取编辑数据
    url(r'^get_list/$', views.get_list),  # 获取编辑数据

)

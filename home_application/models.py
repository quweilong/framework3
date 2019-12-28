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
from django.db import models


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        abstract = True

class UserInfo(BaseModel):
    resume_date = models.CharField(max_length=50)   # 简历日期
    user_name = models.CharField(max_length=50)  # 用户名
    phone = models.CharField(max_length=50)  # 手机号
    education_background = models.CharField(max_length=50) # 学历
    professional = models.CharField(max_length=100) # 专业
    working_years = models.CharField(max_length=50)          # 工作年限
    specialty = models.CharField(max_length=500)        # 特长
    jobs =  models.CharField(max_length=200)        # 求职岗位
    source = models.CharField(max_length=200)  # 来源
    use_department = models.CharField(max_length=200)  # 用人部门
    convention_interview_date = models.CharField(max_length=50) # 预约面试日期
    keep_situation = models.CharField(max_length=200) # 守约情况
    the_interviewer = models.CharField(max_length=200) # 面试人员
    use_department_score = models.CharField(max_length=50) # 用人部门打分
    hr_score = models.CharField(max_length=50) # hr打分
    employment_status = models.CharField(max_length=50) # 录用状态
    work_time = models.CharField(max_length=50) # 到岗时间
    use_department_bk = models.CharField(max_length=500) # 用人部门备注
    hr_bk = models.CharField(max_length=500) # hr备注
    bk =  models.CharField(max_length=500) # 备注

